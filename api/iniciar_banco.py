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
        ('Minimalista', 'O minimalismo valoriza a essência. Peças com corte limpo, cores neutras e tecidos de alta qualidade. Menos é mais — cada peça tem propósito e sobra espaço para respirar.',
         '• Invista em peças básicas de alta qualidade (camisetas de malha grossa, calças retas)\n• Paleta de cores: preto, branco, cinza, bege, marrom\n• Evite estampas e acessórios excessivos\n• Priorize qualidade sobre quantidade\n• Tecidos naturais: algodão, linho, lã',
         '◻'),
        ('Streetwear', 'O streetwear nasceu da cultura urbana e do skate. É ousado, descontraído e cheio de atitude. Gráficos chamativos, tênis como destaque e atitude de sobra.',
         '• Tênis é a peça mais importante do look\n• Mix de gráficos, logos e cores ousadas\n• Layering com camisetas, moletons e jaquetas\n• Acessórios: boné, corrente, relógio oversized\n• Marcas de referência: Supreme, Stüssy, Nike SB',
         '🛹'),
        ('Classico', 'O estilo clássico é atemporal e sofisticado. Cortes tradicionais, tecidos nobres e uma elegância natural que nunca sai de moda. É o estilo dos que sabem que verdadeira elegância não tem data de validade.',
         '• Invista em terno bem cortado e peças estruturadas\n• Cores sólidas: azul-marinho, marrom, cinza, branco\n• Tecidos premium: lã, seda, algodão egípcio\n• Acessórios clássicos: relógio discreto, cinto de couro\n• Evite tendências passageiras',
         '🎩'),
        ('Boho', 'O estilo boho é livre, artístico e cheio de texturas. Mistura estampas etnicas, tecidos naturais e acessórios artesanais para um visual autêntico e acolhedor.',
         '• Misture estampas etnicas e florais com moderação\n• Tecidos naturais: linho, malha, sarja\n• Acessórios artesanais: brincos de macramê, colares de contas\n• Cores terrosas: terracota, mostarda, verde-oliva\n• Cabelo solto e natural',
         '🌿'),
        ('Casual Chic', 'O casual chic é a arte de parecer desleixado de forma proposital. Combina conforto com estilo em um equilíbrio perfeito — como se você não tivesse se esforçado, mas estivesse impecável.',
         '• Mix de peças casuais com peças mais refinadas\n• Jeans de qualidade + blazer ou cardigan\n• Tênis-clean ou mocassim\n• Cores neutras com toques de cor\n• Acessórios minimalistas mas marcantes',
         '✨'),
    ]
    cursor.executemany(
        'INSERT INTO quiz_estilos (nome, descricao, dicas, icone) VALUES (?, ?, ?, ?)',
        estilos
    )

    perguntas = [
        (1, 'Qual dessas combinações de calçado + bolsa mais combina com você?'),
        (2, 'Se o seu estilo fosse um destino de viagem, para onde você iria?'),
        (3, 'Qual é a sua relação com estampas?'),
        (4, 'Na hora de escolher acessórios (brincos, colares, relógios), você prefere:'),
        (5, 'Qual paleta de cores faz seus olhos brilharem?'),
        (6, 'Como você passa a maior parte da sua semana?'),
        (7, 'O que não pode faltar em um look para o seu dia a dia?'),
        (8, 'Quando você tem um evento à noite direto do trabalho, o que você faz?'),
        (9, 'Qual é a sua frequência de uso de sapatos de salto alto?'),
        (10, 'Qual é o seu nível de paciência para passar roupas?'),
        (11, 'Qual frase você mais diz (ou pensa) ao se olhar no espelho?'),
        (12, 'Como costumam ser as suas compras de roupas?'),
        (13, 'Qual é a sua maior queixa sobre as roupas que você já tem?'),
        (14, 'Qual é o seu maior medo ao contratar um estilista/consultor?'),
        (15, 'O que mudou na sua vida recentemente para você buscar mudar de estilo?'),
        (16, 'Se você ganhasse um vale-compras livre agora, qual seria a sua prioridade?'),
        (17, 'Qual dessas peças é o verdadeiro "coração" do seu armário hoje?'),
        (18, 'Como está a organização do seu guarda-roupa hoje?'),
        (19, 'Ao escolher uma roupa, o que vem em primeiro lugar na sua decisão?'),
        (20, 'Qual dessas metas de estilo parece o "paraíso" para você?'),
    ]
    cursor.executemany(
        'INSERT INTO quiz_perguntas (ordem, texto) VALUES (?, ?)',
        perguntas
    )

    opcoes = [
        (1, 'Sapatilha sutil de traço limpo + bolsa lisa sem divisórias.', '{"Minimalista": 3}'),
        (1, 'Bota tratorada ou tênis de sola alta + bolsa transversal com correntes.', '{"Streetwear": 3}'),
        (1, 'Scarpin clássico de bico fino + bolsa estruturada de couro legítimo.', '{"Classico": 3}'),
        (1, 'Sandália de salto bloco de couro + bolsa artesanal de palha ou franjas.', '{"Boho": 3}'),
        (1, 'Tênis branco casual moderno + bolsa de ombro contemporânea e elegante.', '{"Casual Chic": 3}'),

        (2, 'Copenhague: design limpo, foco na arquitetura, silhuetas retas e funcionalidade.', '{"Minimalista": 3}'),
        (2, 'Nova York: ritmo acelerado, cultura urbana, grafites e muito tênis no asfalto.', '{"Streetwear": 3}'),
        (2, 'Londres: tradição, alfaiataria impecável, elegância clássica e sobriedade.', '{"Classico": 3}'),
        (2, 'Ibiza ou Tulum: peças fluidas, contato com a natureza e uma vibe artesanal.', '{"Boho": 3}'),
        (2, 'Paris: meio-termo perfeito, parecendo arrumada e chique sem esforço.', '{"Casual Chic": 3}'),

        (3, 'Evito ao máximo. Prefiro focar estritamente em blocos de cores lisas.', '{"Minimalista": 3}'),
        (3, 'Gosto de estampas gráficas, logos marcantes ou camuflados modernos.', '{"Streetwear": 3}'),
        (3, 'Prefiro as tradicionais, como risca de giz sutil, xadrez clássico ou poá.', '{"Classico": 3}'),
        (3, 'Adoro estampas da natureza, como florais rústicos ou desenhos étnicos.', '{"Boho": 3}'),
        (3, 'Prefiro listras finas horizontais bem limpas ou geométricos discretos.', '{"Casual Chic": 3}'),

        (4, 'Quase não uso, prefiro manter o visual o mais limpo e livre possível.', '{"Minimalista": 3}'),
        (4, 'Bonés, correntes pesadas e brincos geométricos bem marcantes.', '{"Streetwear": 3}'),
        (4, 'Peças tradicionais e atemporais, como pérolas e relógio de metal estruturado.', '{"Classico": 3}'),
        (4, 'Maxicolares artesanais, argolas grandes e anéis de prata envelhecida.', '{"Boho": 3}'),
        (4, 'Um mix discreto de argolas finas modernas e óculos de sol sofisticados.', '{"Casual Chic": 3}'),

        (5, 'Totalmente monocromática: apenas preto, branco e cinza.', '{"Minimalista": 3}'),
        (5, 'Contraste urbano: tons escuros misturados com pontos de neon ou azul bic.', '{"Streetwear": 3}'),
        (5, 'Cores sóbrias tradicionais: azul-marinho, vinho, bege e preto.', '{"Classico": 3}'),
        (5, 'Tons terrosos e quentes: terracota, mostarda, verde-oliva e marrom.', '{"Boho": 3}'),
        (5, 'Tons neutros sofisticados: azul-claro, rosa quartz, cinza mescla e cáqui.', '{"Casual Chic": 3}'),

        (6, 'Em uma rotina prática e rápida, onde padronizo minhas roupas para ganhar tempo.', '{"Minimalista": 3}'),
        (6, 'Em ambientes criativos e dinâmicos (agências, rua, eventos) onde posso ousar.', '{"Streetwear": 3}'),
        (6, 'Em um ambiente de trabalho corporativo tradicional com código de vestimenta formal.', '{"Classico": 3}'),
        (6, 'Em locais descontraídos, ao ar livre ou estúdios voltados à arte e bem-estar.', '{"Boho": 3}'),
        (6, 'Em esquema híbrido ou reuniões casuais, alternando entre escritório e lazer.', '{"Casual Chic": 3}'),

        (7, 'Linhas limpas e peças básicas certeiras que não exigem esforço para combinar.', '{"Minimalista": 3}'),
        (7, 'Liberdade total de movimento, caimento oversized e bolsos funcionais utilitários.', '{"Streetwear": 3}'),
        (7, 'Caimento impecável que transmita respeito, seriedade e profissionalismo imediatos.', '{"Classico": 3}'),
        (7, 'Tecidos leves, naturais e texturas que tragam uma sensação de liberdade e conforto.', '{"Boho": 3}'),
        (7, 'Um toque refinado combinado com peças confortáveis, unindo o chique ao despojado.', '{"Casual Chic": 3}'),

        (8, 'Só mudo o batom, pois minhas roupas de traço reto já servem para qualquer hora.', '{"Minimalista": 3}'),
        (8, 'Troco o sapato do dia por uma bota marcante e adiciono uma jaqueta corta-vento.', '{"Streetwear": 3}'),
        (8, 'Levo um look formal completo na bolsa ou no carro para me trocar do zero.', '{"Classico": 3}'),
        (8, 'Prefiro ir para casa me arrumar para mudar totalmente a proposta para algo fluido.', '{"Boho": 3}'),
        (8, 'Vou com a mesma roupa do dia, apenas adicionando um blazer ou trocando o acessório.', '{"Casual Chic": 3}'),

        (9, 'Nunca uso, sou do time das flats e calçados sem salto de design minimalista.', '{"Minimalista": 3}'),
        (9, 'Não uso de jeito nenhum, minha rotina exige tênis confortáveis no pé o dia todo.', '{"Streetwear": 3}'),
        (9, 'Uso quase todos os dias, scarpins e saltos finos fazem parte da minha identidade.', '{"Classico": 3}'),
        (9, 'Raramente uso, e quando uso prefiro saltos grossos de madeira ou botas rústicas.', '{"Boho": 3}'),
        (9, 'Uso apenas em reuniões importantes, priorizando sapatilhas de bico fino ou saltos blocos.', '{"Casual Chic": 3}'),

        (10, 'Zero paciência. Prefiro tecidos tecnológicos que saem do varal prontos para o corpo.', '{"Minimalista": 3}'),
        (10, 'Não passo. Gosto do caimento despojado de moletons e camisetas de algodão grosso.', '{"Streetwear": 3}'),
        (10, 'Faço questão de passar tudo perfeitamente para manter as linhas e dobras alinhadas.', '{"Classico": 3}'),
        (10, 'Passo apenas o essencial, aceitando o amassado natural de tecidos rústicos como o linho.', '{"Boho": 3}'),
        (10, 'Passo apenas peças-chave de alfaiataria leve, combinando-as com malhas práticas.', '{"Casual Chic": 3}'),

        (11, '"Minhas roupas são funcionais, mas parece que estou sempre com a mesma cara."', '{"Minimalista": 3}'),
        (11, '"Gosto de roupas urbanas, mas sinto medo de parecer muito infantil ou desleixada."', '{"Streetwear": 3}'),
        (11, '"Estou alinhada, mas sinto que meu visual está muito rígido ou parado no tempo."', '{"Classico": 3}'),
        (11, '"Estou elegante para o trabalho, mas sinto que não sou eu mesma nessas roupas formais."', '{"Boho": 3}'),
        (11, '"Amo peças básicas e casuais, mas tenho dificuldade em deixá-las com cara de chique."', '{"Casual Chic": 3}'),

        (12, 'Sou fria e calculista: compro apenas reposições planejadas de itens essenciais.', '{"Minimalista": 3}'),
        (12, 'Compro por impulso lançamentos de marcas modernas ou coleções exclusivas.', '{"Streetwear": 3}'),
        (12, 'Compro de forma tradicional, focando apenas quando tenho um evento formal agendado.', '{"Classico": 3}'),
        (12, 'Adoro garimpar com calma em brechós vintage, feiras locais ou lojas artesanais.', '{"Boho": 3}'),
        (12, 'Procuro promoções de boas marcas contemporâneas para investir em itens curinga.', '{"Casual Chic": 3}'),

        (13, 'Elas perdem a cor ou a estrutura rapidamente por não serem de alta durabilidade.', '{"Minimalista": 3}'),
        (13, 'São muito casuais e não consigo usá-las em um jantar ou evento sério.', '{"Streetwear": 3}'),
        (13, 'Ficaram caretas demais e não transmitem dinamismo ou modernidade.', '{"Classico": 3}'),
        (13, 'Estão muito presas a uma estação e são difíceis de adaptar no inverno/verão.', '{"Boho": 3}'),
        (13, 'Faltam terceiras peças interessantes para dar um acabamento elegante ao jeans.', '{"Casual Chic": 3}'),

        (14, 'Que ele tente me fazer comprar acessórios desnecessários e acumular coisas.', '{"Minimalista": 3}'),
        (14, 'Que ele tire minha autenticidade urbana e me obrigue a usar roupas de escritório.', '{"Streetwear": 3}'),
        (14, 'Que ele queira propor tendências passageiras e estrague meu estilo atemporal.', '{"Classico": 3}'),
        (14, 'Que ele não entenda meu apego afetivo a peças antigas e mande jogar tudo fora.', '{"Boho": 3}'),
        (14, 'Que ele complique meu processo e crie looks difíceis e desconfortáveis.', '{"Casual Chic": 3}'),

        (15, 'Mudei de corpo ou estilo de vida e preciso de uma base de roupas ultra funcional.', '{"Minimalista": 3}'),
        (15, 'Entrei para um ambiente criativo/artístico e quero que minhas roupas mostrem atitude.', '{"Streetwear": 3}'),
        (15, 'Subi de cargo na minha empresa e preciso passar mais respeito, seriedade e liderança.', '{"Classico": 3}'),
        (15, 'Passei por grandes mudanças internas e quero resgatar minha essência livre e artística.', '{"Boho": 3}'),
        (15, 'Comecei a trabalhar de forma híbrida e preciso equilibrar o conforto de casa com a elegância.', '{"Casual Chic": 3}'),

        (16, 'Uma marca autoral focada em cortes geométricos limpos e peças sem logotipos.', '{"Minimalista": 3}'),
        (16, 'Uma loja conceitual para comprar tênis raros (sneakers) e jaquetas de forte identidade.', '{"Streetwear": 3}'),
        (16, 'Uma camisaria ou alfaiataria premium para encomendar um blazer sob medida.', '{"Classico": 3}'),
        (16, 'Um ateliê artesanal ou brechó famoso por suas túnicas, lenços e acessórios únicos.', '{"Boho": 3}'),
        (16, 'Uma boutique contemporânea para comprar blusas de seda e calças jeans perfeitas.', '{"Casual Chic": 3}'),

        (17, 'Uma camiseta branca impecável de algodão egípcio e corte reto.', '{"Minimalista": 3}'),
        (17, 'Uma jaqueta bomber, moletom pesado de capuz ou corta-vento marcante.', '{"Streetwear": 3}'),
        (17, 'Um blazer estruturado tradicional ou uma calça social de alfaiataria.', '{"Classico": 3}'),
        (17, 'Um vestido longo fluido estampado ou uma bata bordada confortável.', '{"Boho": 3}'),
        (17, 'Uma terceira peça estilosa (como um trench coat leve ou cardigan fino) sobre o jeans.', '{"Casual Chic": 3}'),

        (18, 'Extremamente enxuto: tenho pouquíssimas peças, mas todas se combinam entre si.', '{"Minimalista": 3}'),
        (18, 'Cheio de roupas confortáveis misturadas com bonés, tênis em caixas e moletons.', '{"Streetwear": 3}'),
        (18, 'Separado rigorosamente por cores, tipos de cabide e roupas sociais engomadas.', '{"Classico": 3}'),
        (18, 'Um pouco bagunçado, repleto de tecidos fluidos, texturas diferentes e lenços pendurados.', '{"Boho": 3}'),
        (18, 'Visualmente arrumado, mas sinto que falta uma conexão melhor entre as peças casuais e as chiques.', '{"Casual Chic": 3}'),

        (19, 'A durabilidade e a ausência de excessos visuais no design da peça.', '{"Minimalista": 3}'),
        (19, 'A exclusividade do modelo urbano e o impacto da marca no cenário de rua.', '{"Streetwear": 3}'),
        (19, 'O corte tradicional, o alinhamento das costuras e o ar de sofisticação.', '{"Classico": 3}'),
        (19, 'A origem do tecido (natural como algodão/linho) e o toque artesanal do acabamento.', '{"Boho": 3}'),
        (19, 'A versatilidade: saber se consigo usar a peça tanto de tênis quanto de salto.', '{"Casual Chic": 3}'),

        (20, 'Conseguir me arrumar impecavelmente em menos de 5 minutos escolhendo peças neutras.', '{"Minimalista": 3}'),
        (20, 'Dominar o uso de sobreposições de rua sem perder a minha essência despojada.', '{"Streetwear": 3}'),
        (20, 'Entrar em qualquer reunião de negócios sabendo que minha imagem transmite autoridade máxima.', '{"Classico": 3}'),
        (20, 'Montar looks cheios de personalidade expressiva, texturas rústicas e de forma muito livre.', '{"Boho": 3}'),
        (20, 'Viajar apenas com uma mala pequena e ter combinações elegantes para qualquer ocasião.', '{"Casual Chic": 3}'),
    ]
    cursor.executemany(
        'INSERT INTO quiz_opcoes (pergunta_id, texto, estilos_pontos) VALUES (?, ?, ?)',
        opcoes
    )

if __name__ == "__main__":
    inicializar_banco()
