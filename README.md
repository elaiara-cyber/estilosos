# Estilosos — Sistema de Recomendação de Estilo Vestuário

## Dados do Projeto

**Nome do Projeto:** Estilosos

**Apresentação:**  
O presente documento descreve as informações fundamentais referentes ao projeto de desenvolvimento de software denominado "Estilosos". O projeto visa abordar a problemática relativa à seleção de vestuário adequado a cada indivíduo, oferecendo uma solução tecnológica orientada às necessidades dos usuários.

**Objetivo do Projeto:**  
Orientar pessoas em relação ao estilo de roupa que mais combina com elas.

**Equipe de Desenvolvimento:**
- Laiara Emanuelly Marinho Barbosa
- Yasmim Ribeiro dos Santos

**Institucional:**
- Instituto: Instituto Federal de Mato Grosso - Campus de Barra do Garças - MT
- Ano Acadêmico: 2026
- Curso: Técnico em Informática
- Série: Terceiro Ano - B

**Orientação Acadêmica:**
- Prof. Carlos David Rocha de Souza

**Contextualização Disciplinar:**
- Disciplina: Desenvolvimento para Web

---

## Sobre o Sistema

O **Estilosos** é um sistema full-stack acadêmico desenvolvido para demonstrar a integração entre uma interface web reativa em React 18 e um servidor de API em Python (FastAPI) com persistência no banco de dados SQLite. O sistema funciona como um recomendador de estilo pessoal, auxiliando usuários na seleção de roupas adequadas a ocasiões específicas por meio de quiz interativo e análise de arquétipos de moda.

A aplicação compreende um módulo principal:
1. **Módulo de Recomendação de Estilo:** Quiz interativo com 20 perguntas em 5 categorias temáticas (calçado+bolsa, viagem/estética, estampas/acessórios/cores, rotina/funcionalidade, comportamento/consumo/guarda-roupa — ver `api/iniciar_banco.py` para o texto integral) que identifica o arquétipo de moda do usuário (Minimalista, Streetwear, Classico, Boho, Casual Chic) e fornece dicas personalizadas. Sessão via UUID (`POST /api/quiz/sessao`, persistida na tabela `quiz_sessoes`), respostas salvas uma a uma (`POST /api/quiz/resposta` com upsert `DELETE+INSERT` por `sessao_id+pergunta_id` e `404` para sessão inexistente) e resultado calculado no backend (`GET /api/quiz/resultado?sessao_id=...`).

> **Nota:** o módulo de Leads foi removido do repositório (códigos e endpoints `/api/leads` excluídos). O site atual contém apenas o quiz.

---

## Destaques das Funcionalidades

- **Interface Estética Rose Pink:** Estética moderna com paleta de cores rosa (gradiente `from-rosaCha (#FFB6C1) to-rosaBebe (#FFC0CB)` no `<body>` e no `App.jsx`), oferecendo uma experiência visual contemporânea e acolhedora.
- **Quiz Interativo de Estilo:** 20 perguntas de múltipla escolha (5 opções cada, 100 opções no total), contador `Pergunta X de 20`, barra de progresso animada (`duration-500 ease-out`) e navegação fluida entre questões. Cada opção exibe número, cursor customizado em formato de coração rosa e hover `hover:border-rosaCha`. Carregamento paralelo de perguntas + sessão via `Promise.all`.
- **Página de Resultados Detalhada:** Badge `Resultado Calculado via FastAPI + SQLite`, título `Seu Estilo é:`, arquétipo vencedor com ícone 5xl, `X pontos de Y possíveis`, descrição completa, bloco `Dicas Práticas`, até 2 estilos secundários em grid (`Estilos Compatíveis`) e `Pontuação Completa` com barras em percentual (`%`) em gradiente rosa (`duration-700`). Botão `Refazer Quiz 🔄`.
- **Estados de Feedback:** Spinners em `rosaCha` com textos `Carregando perguntas...`, `Salvando resposta...` e `Calculando seu estilo...`; telas de erro com botão `Tentar novamente` / `Refazer Quiz`.
- **Validação e Segurança de Dados:** Sanitização contra XSS com `html.escape` em `api/src/utilitarios/validadores.py`; validação de `sessao_id` (mín. 5 chars), `pergunta_id`/`opcao_id` inteiros com retorno `422/404/201`; proteção contra SQL injection via Prepared Statements (`?`).
- **Arquitetura Full-Stack Integrada:** Comunicação assíncrona via `fetch` nativo (sem Axios/Router — navegação por `useState` em `App.jsx`: `landing → quiz → resultado`) entre frontend React 18 e backend Python FastAPI com CORS configurado via `ORIGEM_PERMITIDA` e proxy Vite `/api → localhost:3000` em dev; em produção o FastAPI serve `frontend/dist` (fallback SPA `/{full_path}`) na porta 3000.
- **Identidade Visual Rose Pink:** Gradiente de fundo `from-rosaCha (#FFB6C1) to-rosaBebe (#FFC0CB)`, destaque em `pink-400 (#F472B6)`, cards glassmorphism (`glass-card-light`, `backdrop-blur-2xl`, `rounded-3xl`, `border-white/30`), botões com gradiente rosa, tipografia Plus Jakarta Sans (textos) + Fira Code (código/valores) via Google Fonts no `index.html`, e animações `animate-pulse-glow` (4s) / `animate-float` (6s).
- **Código enxuto:** apenas 3 componentes ativos (`Onboarding`, `Quiz`, `ResultadoQuiz`); arquivos legados não utilizados foram removidos do repositório.

---

## Arquétipos de Estilo

| Estilo | Ícone | Descrição resumida (texto integral em `api/iniciar_banco.py` e `GET /api/quiz/estilos`) |
|---|---|---|
| **Minimalista** | ◻ | Corte limpo, cores neutras e tecidos de alta qualidade — menos é mais |
| **Streetwear** | 🛹 | Cultura urbana, gráficos ousados, tênis como destaque |
| **Classico** | 🎩 | Cortes tradicionais, tecidos nobres, elegância atemporal |
| **Boho** | 🌿 | Estampas étnicas, tecidos naturais, acessórios artesanais |
| **Casual Chic** | ✨ | Conforto com estilo, mix de peças casuais e refinadas |

---

## Tecnologias Utilizadas

### Frontend (React 18 + Vite + Tailwind CSS)
- **React 18** — Biblioteca declarativa e baseada em componentes reativos para criação de interfaces modernas.
- **Vite 5** — Ferramenta de build de última geração com Hot Module Replacement (HMR) instantâneo e proxy de desenvolvimento `/api → :3000`.
- **Tailwind CSS v3** — Framework CSS utilitário para estilização rápida, responsiva e elegante.
- **JSX & React Hooks** — Gerenciamento de estado (`useState`, `useEffect`), navegação por estado (sem React Router) e integração assíncrona com a API via `fetch` nativo com `Promise.all`.

### Backend (Python 3 + FastAPI + SQLite)
- **Python 3.13** — Linguagem principal de desenvolvimento do backend.
- **FastAPI >= 0.115** — Framework web moderno e de altíssima performance para construção de APIs RESTful.
- **Uvicorn >= 0.30** — Servidor ASGI ultrarrápido para execução da aplicação FastAPI.
- **Pydantic >= 2.0** — Validação de schemas e tratamento de erros (modelos de quiz com retorno `422/404/201`).
- **python-dotenv** — Leitura de `.env` (`PORT`, `ORIGEM_PERMITIDA`).
- **SQLite (sqlite3)** — Banco de dados relacional leve e embutido com suporte a *Prepared Statements* e modo WAL (Write-Ahead Logging).
- **CORS Middleware** — Permissão e controle de requisições Cross-Origin entre React e Python, configurado via variável de ambiente `ORIGEM_PERMITIDA`.

---

## Estrutura de Arquivos do Projeto

```text
estilosos/
├ api/                          # Backend API RESTful em Python
│   ├── db/                       # Banco de dados SQLite (criado em runtime, ignorado no git)
│   │   └── landing.db            # Arquivo da base de dados local (tabelas quiz_*)
│   ├── src/
│   │   ├── __init__.py
│   │   ├── app.py                # FastAPI app, CORS, SPA fallback e estáticos
│   │   ├── server.py / server.js # Legados — entrypoints antigos, não usados (uso atual: main.py)
│   │   ├── config/
│   │   │   └── conexao_banco.py  # Conexão SQLite (dict_factory, WAL + foreign_keys ON)
│   │   ├── controladores/
│   │   │   └── quiz_controlador.py  # Lógica do quiz (sessão UUID, respostas, resultado)
│   │   ├── rotas/
│   │   │   └── quiz_rotas.py     # Endpoints HTTP do quiz (/api/quiz/*)
│   │   └── utilitarios/
│   │       └── validadores.py    # sanitizar() com html.escape
│   ├── iniciar_banco.py          # Criação das tabelas quiz_* + seed (5 estilos, 20 perguntas, 100 opções)
│   ├── main.py                   # Ponto de entrada Uvicorn (PORT=3000, inicializa banco)
│   ├── requirements.txt          # fastapi, uvicorn, pydantic, python-dotenv
│   └── package.json              # Atalho legado (scripts start/dev → main.py)
│
├ frontend/                     # Frontend Reativo em React 18 + Vite
│   ├── src/
│   │   ├── components/           # Componentes React (todos ativos)
│   │   │   ├── Onboarding.jsx    # Tela inicial do quiz (badge, título, CTA)
│   │   │   ├── Quiz.jsx          # Quiz com progresso, cursor coração, fetch paralelo
│   │   │   └── ResultadoQuiz.jsx # Resultado (principal, compatíveis, barras %)
│   │   ├── App.jsx               # Navegação por estado: landing → quiz → resultado
│   │   ├── main.jsx              # Entry React (StrictMode)
│   │   └── index.css             # Gradiente global, glass-card/light, animate-float/pulse-glow
│   ├── index.html                # Montagem HTML + Google Fonts (Plus Jakarta Sans + Fira Code)
│   ├── vite.config.js            # Vite + proxy /api -> http://localhost:3000 (porta 5173)
│   ├── tailwind.config.js        # Cores rosaCha #FFB6C1, rosaBebe #FFC0CB
│   ├── postcss.config.js
│   └── package.json              # react, react-dom, vite, tailwindcss
│
├ doc/                          # Documentação técnica do projeto
│   ├── dados_projeto.md
│   ├── escopo_do_projeto.md
│   ├── planoprojeto.md
│   ├── requisitos_de_sistema.md
│   └── requisitos_de_usuario_estilosos.md
│
├ .gitignore                    # .venv, node_modules, dist, api/db, *.db, .env
└ README.md                     # Documentação oficial do projeto
```

---

## Guia Rápido: Como Executar o Servidor

### 1. Instalar as Dependências (Primeira Execução)

**Backend (API Python):**
```bash
cd api
python -m venv .venv
# No Windows:
.venv\Scripts\pip install -r requirements.txt
# No Linux/Mac:
# source .venv/bin/activate && pip install -r requirements.txt
```

**Frontend (React 18 + Vite):**
```bash
cd ../frontend
npm install
```

---

### 2. Executar o Projeto em Modo de Desenvolvimento (Recomendado)

No modo de desenvolvimento, o servidor React roda via Vite na porta **5173** com atualização instantânea no navegador (Hot Reload) e redirecionamento de requisições de API para a porta **3000**.

#### Passo 1: Iniciar o Servidor Backend (Python + FastAPI)
No primeiro terminal:
```bash
cd api
# Windows:
.venv\Scripts\python main.py
# Linux/Mac:
# .venv/bin/python main.py
```
> O servidor iniciara na porta **3000** (`http://localhost:3000`).

#### Passo 2: Iniciar o Servidor Frontend (React)
Abra um **segundo terminal** no VS Code ou terminal de sua preferencia:
```bash
cd frontend
npm run dev
```
> O Vite iniciara o servidor React na porta **5173** (`http://localhost:5173`).

#### Passo 3: Acessar no Navegador
- **Interface React (Modo Dev):** http://localhost:5173
- **API Python (Health Check):** http://localhost:3000/api/health

---

### 3. Executar o Projeto em Modo de Produção (Build Único)

Caso prefira compilar a aplicação React e servir tudo através do servidor Python/FastAPI na porta **3000**:

1. **Gerar a compilacao de producao do React:**
   ```bash
   cd frontend
   npm run build
   ```
   *Isso criará a pasta otimizada `frontend/dist`.*

2. **Iniciar o servidor backend Python:**
   ```bash
   cd ../api
   .venv\Scripts\python main.py
   ```

3. **Acessar no navegador:**
   - **Aplicação Completa em Produção:** http://localhost:3000

---

## Endpoints da API RESTful

Resposta padrão sucesso: `{sucesso: true, dados, mensagem/total}`. Erros: `{sucesso: false, mensagem, erros?}` com status `404/422/500`.

### Sistema
| Metodo | Rota | Descricao | Status |
|---|---|---|---|
| `GET` | `/api/health` | Health Check (`{sucesso, mensagem}`) | 200 |
| `GET` | `/{full_path}` | SPA fallback — serve `frontend/dist` ou `index.html`; `404` JSON se `full_path` começar com `api` | 200/404 |

### Quiz de Estilo
| Metodo | Rota | Descricao | Status |
|---|---|---|---|
| `POST` | `/api/quiz/sessao` | Criar sessão (UUID persistido em `quiz_sessoes`) | 200 |
| `GET` | `/api/quiz/perguntas` | Listar 20 perguntas + opções (`{sucesso, dados, total}`) | 200 |
| `GET` | `/api/quiz/estilos` | Listar 5 estilos (`nome, descricao, dicas, icone`) | 200 |
| `POST` | `/api/quiz/resposta` | Salvar resposta (`sessao_id min 5 chars, pergunta_id int, opcao_id int`) com upsert; valida FK pergunta/opção | 201 / 404 / 422 |
| `GET` | `/api/quiz/resultado?sessao_id=...` | Calcular resultado (`estilo_principal, pontuacao_principal/total, estilos_secundarios[0..2], todas_pontuacoes`) | 200 / 404 / 422 |

---

## Licença e Créditos

Projeto desenvolvido com fins acadêmicos e educacionais.

**Desenvolvedoras:** Laiara Emanuelly Marinho Barbosa & Yasmim Ribeiro dos Santos

Repositorio oficial no GitHub:
[https://github.com/elaiara-cyber/estilosos.git](https://github.com/elaiara-cyber/estilosos.git)

---