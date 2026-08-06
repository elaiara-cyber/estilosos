import json
import uuid
from fastapi import Response, status
from fastapi.responses import JSONResponse
from ..config.conexao_banco import obter_conexao


def listar_perguntas_controlador():
    conexao = obter_conexao()
    try:
        cursor = conexao.cursor()
        cursor.execute('SELECT id, texto, ordem FROM quiz_perguntas ORDER BY ordem')
        perguntas = cursor.fetchall()

        for p in perguntas:
            cursor.execute(
                'SELECT id, texto FROM quiz_opcoes WHERE pergunta_id = ? ORDER BY id',
                (p['id'],)
            )
            p['opcoes'] = cursor.fetchall()
    finally:
        conexao.close()

    return {
        'sucesso': True,
        'dados': perguntas,
        'total': len(perguntas)
    }


def listar_estilos_controlador():
    conexao = obter_conexao()
    try:
        cursor = conexao.cursor()
        cursor.execute('SELECT id, nome, descricao, dicas, icone FROM quiz_estilos ORDER BY id')
        estilos = cursor.fetchall()
    finally:
        conexao.close()

    return {
        'sucesso': True,
        'dados': estilos
    }


def calcular_resultado_controlador(sessao_id: str):
    if not sessao_id or len(sessao_id.strip()) < 5:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={
                'sucesso': False,
                'mensagem': 'Sessao invalida.'
            }
        )

    conexao = obter_conexao()
    try:
        cursor = conexao.cursor()
        cursor.execute(
            '''SELECT r.opcao_id, o.estilos_pontos
               FROM quiz_respostas r
               JOIN quiz_opcoes o ON o.id = r.opcao_id
               WHERE r.sessao_id = ?
               ORDER BY r.id''',
            (sessao_id,)
        )
        respostas = cursor.fetchall()

        if len(respostas) == 0:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={
                    'sucesso': False,
                    'mensagem': 'Nenhuma resposta encontrada para esta sessao.'
                }
            )

        pontuacoes = {}
        for r in respostas:
            pontos = json.loads(r['estilos_pontos'])
            for estilo, pts in pontos.items():
                pontuacoes[estilo] = pontuacoes.get(estilo, 0) + pts

        sorted_estilos = sorted(pontuacoes.items(), key=lambda x: x[1], reverse=True)

        nome_principal = sorted_estilos[0][0]
        pontuacao_principal = sorted_estilos[0][1]

        cursor.execute(
            'SELECT id, nome, descricao, dicas, icone FROM quiz_estilos WHERE nome = ?',
            (nome_principal,)
        )
        estilo_principal = cursor.fetchone()

        secundarios = []
        for nome, pts in sorted_estilos[1:3]:
            cursor.execute(
                'SELECT id, nome, icone FROM quiz_estilos WHERE nome = ?',
                (nome,)
            )
            s = cursor.fetchone()
            if s:
                s['pontuacao'] = pts
                secundarios.append(s)

        total_pontos = sum(pontuacoes.values())

    finally:
        conexao.close()

    return {
        'sucesso': True,
        'dados': {
            'sessao_id': sessao_id,
            'total_respostas': len(respostas),
            'estilo_principal': estilo_principal,
            'pontuacao_principal': pontuacao_principal,
            'pontuacao_total': total_pontos,
            'estilos_secundarios': secundarios,
            'todas_pontuacoes': dict(sorted_estilos)
        }
    }


def salvar_resposta_controlador(payload: dict):
    sessao_id = str(payload.get('sessao_id', '')).strip()
    pergunta_id = payload.get('pergunta_id')
    opcao_id = payload.get('opcao_id')

    erros = []
    if not sessao_id or len(sessao_id) < 5:
        erros.append(' sessao_id invalido (minimo 5 caracteres).')
    if not pergunta_id or not isinstance(pergunta_id, int) or pergunta_id < 1:
        erros.append(' pergunta_id invalido.')
    if not opcao_id or not isinstance(opcao_id, int) or opcao_id < 1:
        erros.append(' opcao_id invalido.')

    if erros:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={
                'sucesso': False,
                'mensagem': 'Dados invalidos.',
                'erros': erros
            }
        )

    conexao = obter_conexao()
    try:
        cursor = conexao.cursor()
        cursor.execute('SELECT id FROM quiz_perguntas WHERE id = ?', (pergunta_id,))
        if not cursor.fetchone():
            erros.append('Pergunta nao encontrada.')
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={'sucesso': False, 'mensagem': 'Pergunta nao encontrada.'}
            )

        cursor.execute('SELECT id FROM quiz_opcoes WHERE id = ? AND pergunta_id = ?', (opcao_id, pergunta_id))
        if not cursor.fetchone():
            erros.append('Opcao invalida para esta pergunta.')
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={'sucesso': False, 'mensagem': 'Opcao invalida para esta pergunta.'}
            )

        cursor.execute(
            'DELETE FROM quiz_respostas WHERE sessao_id = ? AND pergunta_id = ?',
            (sessao_id, pergunta_id)
        )

        cursor.execute(
            'INSERT INTO quiz_respostas (sessao_id, pergunta_id, opcao_id) VALUES (?, ?, ?)',
            (sessao_id, pergunta_id, opcao_id)
        )
        conexao.commit()

    finally:
        conexao.close()

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            'sucesso': True,
            'mensagem': 'Resposta salva com sucesso!'
        }
    )


def criar_sessao_controlador():
    sessao_id = str(uuid.uuid4())
    return {
        'sucesso': True,
        'sessao_id': sessao_id,
        'mensagem': 'Sessao do quiz criada.'
    }
