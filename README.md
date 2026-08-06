# Sistema Academico de Captura de Leads e Recomendador de Estilo — React 18 + Python (FastAPI) + SQLite

> **Projeto Academico Full Stack:** Aplicacao moderna baseada em componentes reativos em **React 18 (Vite + Tailwind CSS)** com estetica **Dark Glassmorphic** e API RESTful robusta de alta performance em **Python 3 (FastAPI + Uvicorn)** com banco de dados **SQLite**.

---

## Sobre o Projeto

Este projeto consiste em um **Sistema Academico de Captura e Gestao de Leads** e um **Recomendador de Estilo Pessoal** desenvolvidos para demonstrar a integracao de ponta a ponta entre uma interface web reativa em **React 18** e um servidor de API em **Python (FastAPI)** com persistencia relacional no **SQLite**.

A aplicacao conta com:
- Interface futurista baseada em **Dark Glassmorphism**, tipografia com **Google Fonts**, validacao e sanitizacao estrita de dados no servidor contra ataques XSS.
- **Modal interativo em tempo real** para consultar os leads gravados diretamente no SQLite via API.
- **Quiz interativo de estilo** com 6 perguntas, 5 arquétipos de moda (Minimalista, Streetwear, Classico, Boho, Casual Chic), barra de progresso e pagina de resultados com dicas praticas.

---

## Destaques da Interface & Experiencia do Usuario

- **Estetica Dark Glassmorphism:** Cores futuristas (tons de slate, ciano React, roxo e azul Python), transparencias com `backdrop-blur` e efeitos neon (*glow*).
- **Tipografia Importada (Google Fonts):** Utilizacao das fontes *Plus Jakarta Sans* para a interface e *Fira Code* para amostras de codigo.
- **Visualizador Interativo de Codigo:** Abas interativas no banner principal alternando entre trechos de codigo do backend em **Python (FastAPI)** e do frontend em **React (Hooks)**.
- **Inspector de Banco de Dados ao Vivo (`ModalLeads.jsx`):** Modal flutuante que permite aos usuarios e avaliadores consultar e atualizar em tempo real a lista de leads cadastrados no SQLite via rota `GET /api/leads`.
- **Quiz de Estilo Interativo (`Quiz.jsx`):** Navegacao fluida entre 6 perguntas com barra de progresso animada, selecao visual de opcoes e integracao assincrona com a API Python.
- **Pagina de Resultados (`ResultadoQuiz.jsx`):** Exibicao do arquétipo de estilo vencedor, estilos secundarios compativeis, barra de pontuacao completa e dicas praticas de moda.

---

## Tecnologias Utilizadas

### **Frontend (React 18 + Vite + Tailwind CSS)**
- **React 18** — Biblioteca declarativa e baseada em componentes reativos para criacao de interfaces modernas.
- **Vite** — Ferramenta de build de ultima geracao com Hot Module Replacement (HMR) instantaneo.
- **Tailwind CSS v3** — Framework CSS utilitario para estilizacao rapida, responsiva e elegante.
- **JSX & React Hooks** — Gerenciamento de estado de formulario (`useState`, `useEffect`), mascaras dinamicas e integracao assincrona com a API via `fetch`.

### **Backend (Python 3 + FastAPI + SQLite)**
- **Python 3.13** — Linguagem principal de desenvolvimento do backend.
- **FastAPI** — Framework web moderno e de altissima performance para construcao de APIs RESTful.
- **Uvicorn** — Servidor ASGI ultrarrapido para execucao da aplicacao FastAPI.
- **Pydantic & Validadores** — Sanitizacao de dados contra ataques XSS (`html.escape`), tratamento de erros e validacao de emails/telefones.
- **SQLite (sqlite3)** — Banco de dados relacional leve e embutido com suporte a *Prepared Statements* e modo WAL (Write-Ahead Logging).
- **CORS Middleware** — Permissao e controle de requisicoes Cross-Origin entre React e Python.

---

## Estrutura de Arquivos do Projeto

```text
outfitsite/
├── api/                          # Backend API RESTful em Python
│   ├── db/                       # Banco de dados SQLite (criado em runtime)
│   │   └── landing.db            # Arquivo da base de dados local
│   ├── src/
│   │   ├── config/
│   │   │   └── conexao_banco.py  # Conexao SQLite (row_factory dict, WAL mode)
│   │   ├── controladores/
│   │   │   ├── lead_controlador.py  # Logica de negocio (cadastrar e listar leads)
│   │   │   └── quiz_controlador.py  # Logica do quiz (perguntas, respostas, resultado)
│   │   ├── rotas/
│   │   │   ├── lead_rotas.py     # Endpoints HTTP de leads (/api/leads)
│   │   │   └── quiz_rotas.py     # Endpoints HTTP do quiz (/api/quiz/*)
│   │   ├── utilitarios/
│   │   │   └── validadores.py    # Funcoes de sanitizacao e validacao
│   │   └── app.py                # FastAPI app, CORS, estaticos e fallback SPA
│   ├── .env                      # Variaveis de ambiente (PORT=3000, ORIGEM_PERMITIDA=*)
│   ├── iniciar_banco.py          # Criacao das tabelas leads + quiz e seed de dados
│   ├── main.py                   # Ponto de entrada do servidor Uvicorn (Porta 3000)
│   ├── package.json              # Atalho para scripts de desenvolvimento
│   └── requirements.txt          # Dependencias do Python (FastAPI, Uvicorn, etc.)
│
├── frontend/                     # Frontend Reativo em React 18 + Vite
│   ├── src/
│   │   ├── components/           # Componentes React Modulares
│   │   │   ├── Header.jsx        # Navbar fixa com marca AcademiStack e status
│   │   │   ├── Hero.jsx          # Banner principal com visualizador de codigo
│   │   │   ├── Onboarding.jsx    # Tela inicial do quiz de estilo
│   │   │   ├── Quiz.jsx          # Quiz interativo com barra de progresso
│   │   │   ├── ResultadoQuiz.jsx # Pagina de resultados do quiz
│   │   │   ├── Beneficios.jsx    # Cards da arquitetura (Python, React, SQLite, Seguranca)
│   │   │   ├── FormularioLead.jsx# Formulario reativo com mascara e validacao
│   │   │   ├── ModalLeads.jsx    # Modal de consulta em tempo real aos leads do SQLite
│   │   │   ├── Toast.jsx         # Componente de notificacao flutuante
│   │   │   └── Footer.jsx        # Rodape academico com atalhos de sistema
│   │   ├── App.jsx               # Componente raiz da aplicacao (rotas de telas)
│   │   ├── main.jsx              # Ponto de entrada do React (ReactDOM)
│   │   └── index.css             # Estilos globais, fontes e animacoes glassmorphic
│   ├── index.html                # Ponto de montagem HTML com Google Fonts
│   ├── vite.config.js            # Configuracao do Vite e proxy da API (/api -> 3000)
│   ├── tailwind.config.js        # Configuracao do Tailwind CSS
│   ├── postcss.config.js         # Configuracao PostCSS
│   └── package.json              # Dependencias do React e scripts Vite
│
├── doc/                          # Documentacao tecnica do projeto
│   ├── planoprojeto.md           # Plano de desenvolvimento do Recomendador de Estilo
│   ├── escopo_do_projeto.md      # Escopo detalhado do quiz e funcionalidades
│   ├── plano_landingpage_python.md   # Especificacao tecnica oficial da arquitetura Python
│   └── plano_landingpage_nodejs.md   # Documentacao de referencia da versao legada em Node.js
│
├── .gitignore                    # Arquivos ignorados pelo Git (.venv, node_modules, dist, db)
└── README.md                     # Documentacao oficial do projeto
```

---

## Guia Rapido: Como Executar o Servidor React e o Backend Python

### **1. Instalar as Dependencias (Primeira Execucao)**

Abra o terminal na raiz do projeto e execute:

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

### **2. Executar o Projeto em Modo de Desenvolvimento (Recomendado)**

No modo de desenvolvimento, o servidor React roda via Vite na porta **5173** com atualizacao instantanea no navegador (Hot Reload) e redirecionamento de requisicoes de API para a porta **3000**.

#### **Passo 1: Iniciar o Servidor Backend (Python + FastAPI)**
No primeiro terminal:
```bash
cd api
# Windows:
.venv\Scripts\python main.py
# Linux/Mac:
# .venv/bin/python main.py
```
> O servidor iniciara na porta **3000** (`http://localhost:3000`).

#### **Passo 2: Iniciar o Servidor Frontend (React)**
Abra um **segundo terminal** no VS Code ou terminal de sua preferencia:
```bash
cd frontend
npm run dev
```
> O Vite iniciara o servidor React na porta **5173** (`http://localhost:5173`).

#### **Passo 3: Acessar no Navegador**
- **Interface React (Modo Dev):** http://localhost:5173
- **API Python (Health Check):** http://localhost:3000/api/health

---

### **3. Executar o Projeto em Modo de Producao (Build Unico)**

Caso prefira compilar a aplicacao React e servir tudo atraves do servidor Python/FastAPI na porta **3000**:

1. **Gerar a compilacao de producao do React:**
   ```bash
   cd frontend
   npm run build
   ```
   *Isso criara a pasta otimizada `frontend/dist`.*

2. **Iniciar o servidor backend Python:**
   ```bash
   cd ../api
   .venv\Scripts\python main.py
   ```

3. **Acessar no navegador:**
   - **Aplicacao Completa em Producao:** http://localhost:3000

---

## Endpoints da API RESTful

### **Leads**
| Metodo | Rota | Descricao |
|---|---|---|
| `GET` | `/` | Servidor estatico da aplicacao React (`frontend/dist`) |
| `GET` | `/api/health` | Health Check do servidor Python |
| `POST` | `/api/leads` | Cadastrar novo lead no banco SQLite |
| `GET` | `/api/leads` | Listar leads cadastrados no SQLite (`pagina`, `limite`) |

### **Quiz de Estilo**
| Metodo | Rota | Descricao |
|---|---|---|
| `POST` | `/api/quiz/sessao` | Criar uma nova sessao do quiz (retorna `sessao_id` UUID) |
| `GET` | `/api/quiz/perguntas` | Listar todas as perguntas do quiz com suas opcoes |
| `GET` | `/api/quiz/estilos` | Listar todos os estilos disponiveis (nome, descricao, dicas, icone) |
| `POST` | `/api/quiz/resposta` | Salvar uma resposta do usuario (`sessao_id`, `pergunta_id`, `opcao_id`) |
| `GET` | `/api/quiz/resultado` | Calcular e retornar o resultado do quiz (`?sessao_id=...`) |

---

## Arquétipos de Estilo

| Estilo | Icone | Descricao |
|---|---|---|
| **Minimalista** | ◻ | Pecas com corte limpo, cores neutras e tecidos de alta qualidade |
| **Streetwear** | 🛹 | Cultura urbana, graficos ousados, tenis como destaque |
| **Classico** | 🎩 | Cortes tradicionais, tecidos nobres, elegancia atemporal |
| **Boho** | 🌿 | Estampas etnicas, tecidos naturais, acessorios artesanais |
| **Casual Chic** | ✨ | Conforto com estilo, mix de pecas casuais e refinadas |

---

## Licenca e Creditos

Projeto desenvolvido com fins academicos e educacionais.

**Desenvolvedoras:** Laiara Emanuelly Marinho Barbosa & Yasmim Ribeiro dos Santos

Repositorio oficial no GitHub:
[https://github.com/ImagineLikeMe/siteoutfit.git](https://github.com/ImagineLikeMe/siteoutfit.git)
