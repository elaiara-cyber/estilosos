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

A aplicação compreende dois módulos principais:
1. **Módulo de Recomendação de Estilo:** Quiz interativo com 6 perguntas que identifica o arquétipo de moda do usuário (Minimalista, Streetwear, Classico, Boho, Casual Chic) e fornece dicas personalizadas, com armazenamento de resultados no banco de dados SQLite.
2. **Módulo de Gestão de Leads:** Sistema para registro e consulta de leads (potenciais interessados) por meio de interface de formulário, com persistência no banco de dados SQLite e visualização em tempo real via modal.

---

## Destaques das Funcionalidades

- **Interface Estética Rose Pink:** Estética moderna com paleta de cores rosa, oferecendo uma experiência visual contemporânea e acolhedora.
- **Quiz Interativo de Estilo:** 6 perguntas com 5 arquétipos de moda (Minimalista, Streetwear, Classico, Boho, Casual Chic), barra de progresso animada e navegação fluida entre questões.
- **Página de Resultados Detalhada:** Exibição do arquétipo vencedor, estilos secundários compatíveis, barra de pontuação completa e dicas práticas de moda.
- **Modal de Consultas em Tempo Real (`ModalLeads.jsx`):** Permite aos usuários e avaliadores consultar e atualizar a lista de leads cadastrados no SQLite via API rota `GET /api/leads` sem recarregar a página.
- **Validação e Segurança de Dados:** Sanitização rigorosa contra ataques XSS usando `html.escape` no backend Python (FastAPI) com validadores de e-mail e telefone.
- **Arquitetura Full-Stack Integrada:** Comunicação assíncrona via fetch entre frontend React 18 e backend Python FastAPI com roteamento CORS configurado.

---

## Arquétipos de Estilo

| Estilo | Ícone | Descrição |
|---|---|---|
| **Minimalista** | ◻ | Peças com corte limpo, cores neutras e tecidos de alta qualidade |
| **Streetwear** | 🛹 | Cultura urbana, gráficos ousados, tênis como destaque |
| **Clássico** | 🎩 | Cortes tradicionais, tecidos nobres, elegância atemporal |
| **Boho** | 🌿 | Estampas étnicas, tecidos naturais, acessórios artesanais |
| **Casual Chic** | ✨ | Conforto com estilo, mix de peças casuais e refinadas |

---

## Tecnologias Utilizadas

### Frontend (React 18 + Vite + Tailwind CSS)
- **React 18** — Biblioteca declarativa e baseada em componentes reativos para criação de interfaces modernas.
- **Vite** — Ferramenta de build de última geração com Hot Module Replacement (HMR) instantâneo.
- **Tailwind CSS v3** — Framework CSS utilitário para estilização rápida, responsiva e elegante.
- **JSX & React Hooks** — Gerenciamento de estado de formulários (`useState`, `useEffect`), máscaras dinâmicas e integração assíncrona com a API via `fetch`.

### Backend (Python 3 + FastAPI + SQLite)
- **Python 3.13** — Linguagem principal de desenvolvimento do backend.
- **FastAPI** — Framework web moderno e de altíssima performance para construção de APIs RESTful.
- **Uvicorn** — Servidor ASGI ultrarrápido para execução da aplicação FastAPI.
- **Pydantic & Validadores** — Sanitização de dados contra ataques XSS (`html.escape`), tratamento de erros e validação de e-mails/telefones.
- **SQLite (sqlite3)** — Banco de dados relacional leve e embutido com suporte a *Prepared Statements* e modo WAL (Write-Ahead Logging).
- **CORS Middleware** — Permissão e controle de requisições Cross-Origin entre React e Python.

---

## Estrutura de Arquivos do Projeto

```text
outfitsite/
├ api/                          # Backend API RESTful em Python
│   ├── db/                       # Banco de dados SQLite (criado em runtime)
│   │   └── landing.db            # Arquivo da base de dados local
│   ├── src/
│   │   ├── config/
│   │   │   └── conexao_banco.py  # Conexão SQLite (row_factory dict, WAL mode)
│   │   ├── controladores/
│   │   │   ├── lead_controlador.py  # Logica de negocio (cadastrar e listar leads)
│   │   │   └── quiz_controlador.py  # Logica do quiz (perguntas, respostas, resultado)
│   │   ├── rotas/
│   │   │   ├── lead_rotas.py     # Endpoints HTTP de leads (/api/leads)
│   │   │   └── quiz_rotas.py     # Endpoints HTTP do quiz (/api/quiz/*)
│   │   ├── utilitarios/
│   │   │   └── validadores.py    # Funções de sanitização e validação
│   │   └── app.py                # FastAPI app, CORS, estaticos e fallback SPA
│   ├── .env                      # Variaveis de ambiente (PORT=3000, ORIGEM_PERMITIDA=*)
│   ├── iniciar_banco.py          # Criação das tabelas leads + quiz e seed de dados
│   ├── main.py                   # Ponto de entrada do servidor Uvicorn (Porta 3000)
│   ├── package.json              # Atalho para scripts de desenvolvimento
│   └── requirements.txt          # Dependências do Python (FastAPI, Uvicorn, etc.)
│
├ frontend/                     # Frontend Reativo em React 18 + Vite
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
├ doc/                          # Documentacao tecnica do projeto
│   ├── planoprojeto.md           # Plano de desenvolvimento do Recomendador de Estilo
│   ├── escopo_do_projeto.md      # Escopo detalhado do quiz e funcionalidades
│   ├── plano_landingpage_python.md   # Especificacao tecnica oficial da arquitetura Python
│   └── plano_landingpage_nodejs.md   # Documentacao de referencia da versao legada em Node.js
│
├ .gitignore                    # Arquivos ignorados pelo Git (.venv, node_modules, dist, db)
└ README.md                     # Documentacao oficial do projeto
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

### Leads
| Metodo | Rota | Descricao |
|---|---|---|
| `GET` | `/` | Servidor estático da aplicação React (`frontend/dist`) |
| `GET` | `/api/health` | Health Check do servidor Python |
| `POST` | `/api/leads` | Cadastrar novo lead no banco SQLite |
| `GET` | `/api/leads` | Listar leads cadastrados no SQLite (`pagina`, `limite`) |

### Quiz de Estilo
| Metodo | Rota | Descricao |
|---|---|---|
| `POST` | `/api/quiz/sessao` | Criar uma nova sessao do quiz (retorna `sessao_id` UUID) |
| `GET` | `/api/quiz/perguntas` | Listar todas as perguntas do quiz com suas opcoes |
| `GET` | `/api/quiz/estilos` | Listar todos os estilos disponiveis (nome, descricao, dicas, icone) |
| `POST` | `/api/quiz/resposta` | Salvar uma resposta do usuario (`sessao_id`, `pergunta_id`, `opcao_id`) |
| `GET` | `/api/quiz/resultado` | Calcular e retornar o resultado do quiz (`?sessao_id=...`) |

---

## Licença e Créditos

Projeto desenvolvido com fins acadêmicos e educacionais.

**Desenvolvedoras:** Laiara Emanuelly Marinho Barbosa & Yasmim Ribeiro dos Santos

Repositorio oficial no GitHub:
[https://github.com/ImagineLikeMe/siteoutfit.git](https://github.com/ImagineLikeMe/siteoutfit.git)

---