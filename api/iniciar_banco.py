import os
import sqlite3

def inicializar_banco():
    caminho_base = os.path.dirname(os.path.abspath(__file__))
    pasta_db = os.path.join(caminho_base, 'db')
    os.makedirs(pasta_db, exist_ok=True)
    caminho_banco = os.path.join(pasta_db, 'landing.db')

    conexao = sqlite3.connect(caminho_banco)
    cursor = conexao.cursor()

    cursor.executescript('''
        CREATE TABLE IF NOT EXISTS leads (
            id                  INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_completo       TEXT    NOT NULL,
            email               TEXT    NOT NULL,
            telefone_whatsapp   TEXT    NOT NULL,
            mensagem            TEXT    DEFAULT NULL,
            data_cadastro       TEXT    DEFAULT (datetime('now','localtime')),
            status_atendimento  TEXT    DEFAULT 'novo'
                                        CHECK(status_atendimento IN ('novo','contatado','convertido','perdido'))
        );
        CREATE INDEX IF NOT EXISTS idx_leads_email ON leads(email);
        CREATE INDEX IF NOT EXISTS idx_leads_status ON leads(status_atendimento);

        CREATE TABLE IF NOT EXISTS quiz_estilos (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            nome        TEXT    NOT NULL UNIQUE,
            descricao   TEXT    NOT NULL,
            dicas       TEXT    NOT NULL,
            icone       TEXT    DEFAULT '✨'
        );

        CREATE TABLE IF NOT EXISTS quiz_perguntas (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            texto   TEXT    NOT NULL,
            ordem   INTEGER NOT NULL
        );

        CREATE TABLE IF NOT EXISTS quiz_opcoes (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            pergunta_id     INTEGER NOT NULL,
            texto           TEXT    NOT NULL,
            estilos_pontos  TEXT    NOT NULL,
            FOREIGN KEY (pergunta_id) REFERENCES quiz_perguntas(id)
        );

        CREATE TABLE IF NOT EXISTS quiz_respostas (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            sessao_id       TEXT    NOT NULL,
            pergunta_id     INTEGER NOT NULL,
            opcao_id        INTEGER NOT NULL,
            data_resposta   TEXT    DEFAULT (datetime('now','localtime')),
            FOREIGN KEY (pergunta_id) REFERENCES quiz_perguntas(id),
            FOREIGN KEY (opcao_id) REFERENCES quiz_opcoes(id)
        );

        CREATE INDEX IF NOT EXISTS idx_quiz_opcoes_pergunta ON quiz_opcoes(pergunta_id);
        CREATE INDEX IF NOT EXISTS idx_quiz_respostas_sessao ON quiz_respostas(sessao_id);
    ''')

    _popular_dados_quiz(conexao)

    conexao.commit()
    conexao.close()
    print("Banco de dados inicializado com sucesso no SQLite (Python).")


def _popular_dados_quiz(conexao):
    cursor = conexao.cursor()

    cursor.execute('SELECT COUNT(*) FROM quiz_estilos')
    if cursor.fetchone()[0] > 0:
        return

    estilos = [
        ('Minimalista', 'O minimalismo valoriza a essencia. Pecas com corte limpo, cores neutras e tecidos de alta qualidade. Menos e mais — cada peca tem proposito e sobra espaco para respirar.',
         '• Investa em pecas basicas de alta qualidade (camisetas de malha grossa, calças retas)\n• Paleta de cores: preto, branco, cinza, bege, marrom\n• Evite estampas e acessorios excessivos\n• Priorize qualidade sobre quantidade\n• Tecidos naturais: algodao, linho, la',
         '◻'),
        ('Streetwear', 'O streetwear nasceu da cultura urbana e do skate. E ousado, descontraído e cheio de atitude. Graficos chamativos, tênis como destaque e atitude de sobra.',
         '• Tênis é a peca mais importante do look\n• Mix de graficos, logos e cores ousadas\n• Layering com camisetas, moletons e jaquetas\n• Acessorios: boné, corrente, relógio oversized\n• Marcas de referencia: Supreme, Stüssy, Nike SB',
         '🛹'),
        ('Classico', 'O estilo classico é atemporal e sofisticado. Cortes tradicionais, tecidos nobres e uma elegancia natural que nunca sai de moda. E o estilo dos que sabem que verdadeira elegancia nao tem data de validade.',
         '• Investe em terno bem cortado e pecas estruturadas\n• Cores sólidas: azul-marinho, marrom, cinza, branco\n• Tecidos premium: la, seda, algodao egípcio\n• Acessorios clássicos: relogio discreto, cinto de couro\n• Evite tendências passageiras',
         '🎩'),
        ('Boho', 'O estilo bohemio é livre, artístico e cheio de texturas. Mistura estampas etnicas, tecidos naturais e acessorios artesanais para um visual autêntico e acolhedor.',
         '• Misture estampas etnicas e florais com moderacao\n• Tecidos naturais: linho, malha, sarja\n• Acessorios artesanais: brincos de macrame, colares de contas\n• Cores terrosas: terracota, mustarde, verde oliva\n• Cabelo solto e natural',
         '🌿'),
        ('Casual Chic', 'O casual chic é a arte de parecer desleixado de forma proposital. Combina conforto com estilo em um equilibrio perfeito — como se voce nao tivesse se esforcado, mas estivesse impecavel.',
         '• Mix de pecas casuais com pecas mais refinadas\n• Jeans de qualidade + blazer ou cardigan\n• Tenis-clean ou mocassim\n• Cores neutras com toques de cor\n• Acessorios minimalistas mas marcantes',
         '✨'),
    ]
    cursor.executemany(
        'INSERT INTO quiz_estilos (nome, descricao, dicas, icone) VALUES (?, ?, ?, ?)',
        estilos
    )

    perguntas = [
        (1, 'Como voce prefere se vestir no dia a dia?'),
        (2, 'Quais cores mais combinam com voce?'),
        (3, 'Para qual ocasiao voce mais se veste?'),
        (4, 'Qual peca e indispensavel no seu guarda-roupa?'),
        (5, 'Como voce escolhe suas roupas?'),
        (6, 'Qual sua vibe predominante?'),
    ]
    cursor.executemany(
        'INSERT INTO quiz_perguntas (ordem, texto) VALUES (?, ?)',
        perguntas
    )

    opcoes = [
        # Pergunta 1: Conforto vs Formalidade
        (1, 'Confortavel e despojado, nada apertado', '{"Streetwear": 3, "Casual Chic": 2}'),
        (1, 'Simples, limpo e sem exageros', '{"Minimalista": 3, "Classico": 1}'),
        (1, 'Elegante e bem estruturado', '{"Classico": 3, "Casual Chic": 1}'),
        (1, 'Livre, com texturas e estampas', '{"Boho": 3, "Streetwear": 1}'),

        # Pergunta 2: Cores
        (2, 'Neutras: preto, branco, cinza, bege', '{"Minimalista": 3, "Classico": 2}'),
        (2, 'Vibrantes e ousadas', '{"Streetwear": 3, "Boho": 1}'),
        (2, 'Terrosas: terracota, mustarde, verde oliva', '{"Boho": 3, "Casual Chic": 1}'),
        (2, 'Classic: azul-marinho, marrom, vinho', '{"Classico": 3, "Minimalista": 1}'),

        # Pergunta 3: Ocasiao
        (3, 'Rua, skate, rolê com amigos', '{"Streetwear": 3, "Boho": 1}'),
        (3, 'Trabalho, reunioes, eventos formais', '{"Classico": 3, "Minimalista": 2}'),
        (3, 'Cafe, shopping, passeio casual', '{"Casual Chic": 3, "Minimalista": 1}'),
        (3, 'Feira, natureza, festival', '{"Boho": 3, "Streetwear": 1}'),

        # Pergunta 4: Peca indispensavel
        (4, 'Tenis ou tenis de grife', '{"Streetwear": 3, "Casual Chic": 2}'),
        (4, 'Camiseta basica de qualidade', '{"Minimalista": 3, "Casual Chic": 1}'),
        (4, 'Bem cortado e social', '{"Classico": 3, "Minimalista": 1}'),
        (4, 'Chaleco, cardigan ou jaqueta de croche', '{"Boho": 3, "Streetwear": 1}'),

        # Pergunta 5: Como escolhe roupas
        (5, 'Por marcadoras e lancamentos', '{"Streetwear": 3, "Classico": 1}'),
        (5, 'Por versatilidade e durabilidade', '{"Minimalista": 3, "Casual Chic": 2}'),
        (5, 'Por pecas atemporais e bem feitas', '{"Classico": 3, "Minimalista": 2}'),
        (5, 'Por pecas unicas e artesanais', '{"Boho": 3, "Streetwear": 1}'),

        # Pergunta 6: Vibe predominante
        (6, 'Atitude e autenticidade urbana', '{"Streetwear": 3, "Casual Chic": 1}'),
        (6, 'Simplicidade e sofisticacao', '{"Minimalista": 3, "Classico": 2}'),
        (6, 'Elegancia natural e polida', '{"Classico": 3, "Casual Chic": 2}'),
        (6, 'Liberdade e conexao com a natureza', '{"Boho": 3, "Streetwear": 1}'),
    ]
    cursor.executemany(
        'INSERT INTO quiz_opcoes (pergunta_id, texto, estilos_pontos) VALUES (?, ?, ?)',
        opcoes
    )

if __name__ == "__main__":
    inicializar_banco()
