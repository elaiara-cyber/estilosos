# Plano de Desenvolvimento do Projeto: Estilosos — Recomendador de Estilo Pessoal

**Dupla Criadora:** Laiara Emanuelly Marinho Barbosa e Yasmim Ribeiro dos Santos  
**Ferramenta de IA/Assistente:** OpenCode  
**Base Tecnológica:** Arquitetura, estética e linguagens já existentes descritas no arquivo `README.md` e nos códigos-fonte do repositório.

---

## 0. Stack Tecnológico Oficial

* **Front-end:** React 18 (Vite + Tailwind CSS v3) — componentes reativos com JSX e React Hooks (`useState`, `useEffect`), comunicação assíncrona via `fetch` com a API.
* **Back-end:** Python 3.13 + FastAPI + Uvicorn — API RESTful de alta performance, com Pydantic e validadores (`html.escape`) para sanitização anti-XSS, e Middleware CORS.
* **Banco de Dados:** SQLite (sqlite3) — relacional embutido com *Prepared Statements* e modo WAL.
* **Estrutura:** Backend em `api/` (rotas, controladores, utilitários) e Frontend em `frontend/` (componentes React), servidos em modo dev nas portas **3000** (FastAPI) e **5173** (Vite), com proxy `/api → localhost:3000` configurado no `vite.config.js`.

---

## 0.1 Identidade Visual do Site (Extraída dos Códigos)

A estética oficial do projeto é o tema claro **Rose Pink**, definida no `tailwind.config.js`, no `index.css` e aplicada em todos os componentes ativos.

### Paleta de Cores

| Cor | Código | Uso no Site |
|---|---|---|
| `rosaCha` | `#FFB6C1` | Cor da marca: fundo do gradiente base, bordas de hover das opções, spinners de carregamento, badges e destaques |
| `rosaBebe` | `#FFC0CB` | Complemento do gradiente base (fundo) e das barras de progresso/pontuação |
| `pink-400` | `#F472B6` | Tom central dos gradientes dos botões e destaque sólido de palavras-chave do título |
| Branco translúcido (`bg-white`, `border-white/30`) | — | Cards glassmorphism claros sobre o fundo rosa |
| `gray-800` / tons de `slate` | — | Tipografia principal e textos secundários |

### Fundo e Cartões

* **Fundo global:** gradiente vertical `from-rosaCha to-rosaBebe` aplicado no `<body>` (definido em `index.css` e repetido nas telas do `App.jsx`).
* **Cartões:** estilo *glassmorphism claro* — fundo branco com `backdrop-blur-2xl`, cantos arredondados (`rounded-3xl`), borda `border-white/30` e sombra profunda (`shadow-2xl`).
* **Luzes decorativas (orbs):** círculos desfocados (`blur-[100px]` a `blur-[120px]`) em tons rosa translúcidos posicionados ao fundo das seções.

### Botões Padrão

* **Botão primário (CTA):** gradiente horizontal `from-rosaCha via-pink-400 to-rosaBebe`, texto branco, `font-extrabold`, cantos `rounded-2xl`, sombra `shadow-xl shadow-rosaCha/25` e hover que intensifica o gradiente (`hover:from-rosaCha hover:to-pink-400`). Ex.: "Iniciar Quiz de Estilo" e "Refazer Quiz".
* **Botão secundário:** fundo branco com borda sutil e hover acinzentado. Ex.: "Tentar novamente".

### Tipografia

* **Interface:** `Plus Jakarta Sans` (pesos 400–800), carregada via Google Fonts no `index.html`.
* **Código/valores numéricos:** `Fira Code` (monoespaçada).

### Animações e Microinterações

* `animate-pulse-glow` — pulsação suave dos orbs de luz (4s).
* `.animate-float` — flutuação vertical contínua (6s).
* Barra de progresso do quiz com transição de largura animada (`duration-500 ease-out`); barras de pontuação do resultado com `duration-700`.
* Spinners circulares em `rosaCha` nos estados de carregamento ("Carregando perguntas...", "Calculando seu estilo...").
* Hover com elevação/deslocamento nos botões (seta `➔` desloca para a direita) e mudança de borda nas opções do quiz.

### Telas Ativas (montadas pelo `App.jsx`)

1. **Onboarding** — badge "Recomendador de Estilo Pessoal", título "Descubra seu **Estilo**" (destaque sólido em `pink-400`), parágrafo descritivo, 4 badges (20 Perguntas, 5 Estilos, Resultado Instantâneo, React + FastAPI + SQLite), CTA "Iniciar Quiz de Estilo ➔" e créditos Laiara & Yasmim.
2. **Quiz** — contador "Pergunta X de 20", barra de progresso gradiente (`duration-500`), card branco com pergunta + opções numeradas (cursor coração rosa custom via inline SVG), estados "Carregando perguntas...", "Salvando resposta..." e erro + "Tentar novamente"; `Promise.all` para perguntas+sessão.
3. **ResultadoQuiz** — badge "Resultado Calculado via FastAPI + SQLite", "Seu Estilo é:", ícone 5xl, `X pontos de Y possíveis`, descrição, bloco "Dicas Práticas", "Estilos Compatíveis" (grid até 2) e "Pontuação Completa" em `%` com barras gradiente (`duration-700`); CTA "Refazer Quiz 🔄"; loading "Calculando seu estilo...".

> **Nota:** componentes legados da landing page antiga e o protótipo `quiz-interface.html` foram removidos do repositório — o frontend contém apenas os 3 componentes do quiz. Não há endpoints `/api/leads` no backend.

---

## 1. Diretrizes para o OpenCode (Regras de Ouro)
* **Respeito ao Legado:** O OpenCode deve ler rigorosamente o arquivo `README.md` antes de gerar qualquer código para identificar o stack tecnológico oficial (React 18 + Vite + Tailwind, Python 3 + FastAPI, SQLite).
* **Identidade Visual Obrigatória:** Qualquer novo componente deve seguir o tema **Rose Pink** descrito na seção 0.1 — fundo gradiente `rosaCha → rosaBebe`, cards brancos translúcidos com blur, botões com gradiente rosa e tipografia Plus Jakarta Sans. Não utilizar temas escuros.
* **Separação de Camadas:** Manter a estrita separação entre Front-end (`frontend/`) e Back-end (`api/`) conforme a arquitetura preexistente no repositório.
* **Padrões do Back-end:** Seguir a estrutura existente de `api/src/config/conexao_banco.py` (row_factory dict, modo WAL), `api/src/controladores/`, `api/src/rotas/` e `api/src/utilitarios/validadores.py`, expondo endpoints via `api/src/app.py` e `api/main.py` (Uvicorn na porta 3000).
* **Padrões do Front-end:** Reutilizar os componentes ativos do quiz de `frontend/src/components/` (Onboarding, Quiz, ResultadoQuiz) e os utilitários visuais de `frontend/src/index.css` (`.glass-card-light`, `.animate-pulse-glow`, `.animate-float`).
* **Consistência de Código:** Seguir o estilo de código, linter, formatação e convenções de nomenclatura já definidos no projeto.

---

## 2. Fases do Plano de Execução

### Fase 1: Análise e Configuração do Ambiente ✅ CONCLUÍDA
* **Ação executada:**
  * Leitura e análise do `README.md` para mapear o stack tecnológico oficial (React 18 + Vite + Tailwind CSS, Python 3 + FastAPI + Uvicorn, SQLite) e a estrutura de pastas (`api/`, `frontend/`, `doc/`).
  * Verificação de dependências no `api/requirements.txt` e `frontend/package.json`.
* **Entregável:** Estrutura mapeada e ambiente local configurado.

### Fase 2: Desenvolvimento do Back-end ✅ CONCLUÍDA
* **Arquivos criados:**
  * `api/iniciar_banco.py` — Tabelas `quiz_estilos`, `quiz_perguntas`, `quiz_opcoes`, `quiz_respostas` com seed de dados (5 estilos, 20 perguntas, 100 opções).
  * `api/src/controladores/quiz_controlador.py` — Lógica de pontuação, cálculo de resultado, listagem de perguntas, criação de sessão e validação de respostas.
  * `api/src/rotas/quiz_rotas.py` — Endpoints RESTful: `POST /api/quiz/sessao`, `GET /api/quiz/perguntas`, `GET /api/quiz/estilos`, `POST /api/quiz/resposta`, `GET /api/quiz/resultado`.
  * `api/src/app.py` — Inclusão do router via `app.include_router(quiz_router, prefix="/api")` e endpoint de health check.
* **Entregável:** Endpoints de API funcionais, validados e sanitizados.

### Fase 3: Desenvolvimento do Front-end ✅ CONCLUÍDA
* **Arquivos criados:**
  * `frontend/src/components/Onboarding.jsx` — Tela inicial do quiz com badge, título destacado, badges informativos e CTA gradiente.
  * `frontend/src/components/Quiz.jsx` — Interface do quiz com barra de progresso animada, seleção de opções e envio assíncrono via `fetch`.
  * `frontend/src/components/ResultadoQuiz.jsx` — Página de resultados com arquétipo principal, estilos secundários, barras de pontuação e dicas práticas.
  * `frontend/src/App.jsx` — Integração das 3 telas do quiz (Onboarding → Quiz → ResultadoQuiz) com navegação por estado e fundo Rose Pink.
* **Entregável:** Interface web responsiva e integrada, no padrão visual **Rose Pink** (glassmorphism claro).

### Fase 4: Testes, Ajustes e Documentação ✅ CONCLUÍDA
* **Ações executadas:**
  * Testes de integração: criação de sessão, envio de 20 respostas e cálculo de resultado validados via `curl`.
  * Validação do build do React (`npm run build` sem erros).
  * Validação dos endpoints do FastAPI (health check, perguntas, estilos, respostas, resultado).
  * Correção de bug: colunas `texto` e `ordem` da tabela `quiz_perguntas` invertidas no INSERT.
  * Atualização do `README.md` com documentação completa do quiz e endpoints.
  * Refinamentos visuais na tela Onboarding (destaque do título "Estilo" alinhado à identidade rosa dos botões).
* **Entregável:** Código testado, limpo e pronto para deploy.

---

## 3. Estrutura de Arquivos do Projeto

```
estilosos/
├── api/
│   ├── main.py                          # Entrypoint Uvicorn (PORT=3000, inicializa banco)
│   ├── iniciar_banco.py                 # Schema quiz_* + seed (5 estilos, 20 perguntas, 100 opções)
│   ├── requirements.txt                 # fastapi, uvicorn, pydantic, python-dotenv
│   ├── package.json                     # Atalho legado
│   ├── db/landing.db                    # SQLite WAL (ignorado no git)
│   └── src/
│       ├── __init__.py
│       ├── app.py                       # FastAPI app, CORS, router, estáticos + SPA fallback
│       ├── server.js / server.py        # LEGADOS (não usados)
│       ├── config/
│       │   └── conexao_banco.py         # dict_factory + WAL + foreign_keys ON
│       ├── controladores/
│       │   └── quiz_controlador.py      # Sessão UUID, upsert DELETE+INSERT, cálculo resultado
│       ├── rotas/
│       │   └── quiz_rotas.py            # /quiz/perguntas, /quiz/estilos, /quiz/sessao, /quiz/resposta, /quiz/resultado
│       └── utilitarios/
│           └── validadores.py           # sanitizar() com html.escape
├── frontend/
│   ├── index.html                       # pt-BR, title Estilosos, Plus Jakarta Sans + Fira Code
│   ├── vite.config.js                   # 5173 + proxy /api → localhost:3000
│   ├── tailwind.config.js               # rosaCha #FFB6C1, rosaBebe #FFC0CB
│   ├── postcss.config.js
│   ├── package.json                     # react 18, vite 5, tailwind 3
│   └── src/
│       ├── main.jsx                     # StrictMode
│       ├── App.jsx                      # landing → quiz → resultado (useState)
│       ├── index.css                    # gradiente global, glass-card/light, float/pulse-glow
│       └── components/
│           ├── Onboarding.jsx           # Tela inicial do quiz
│           ├── Quiz.jsx                 # Interface do quiz
│           └── ResultadoQuiz.jsx        # Tela de resultados
└── doc/
    ├── dados_projeto.md
    ├── escopo_do_projeto.md
    ├── planoprojeto.md
    ├── requisitos_de_sistema.md
    └── requisitos_de_usuario_estilosos.md
```

---

## 4. Mapa de Endpoints da API

| Método | Endpoint | Descrição | Status |
|---|---|---|---|
| `GET` | `/api/health` | Health check — `{sucesso, mensagem}` | 200 |
| `GET` | `/api/quiz/perguntas` | 20 perguntas + opções (`{sucesso, dados, total}`) | 200 |
| `GET` | `/api/quiz/estilos` | 5 arquétipos | 200 |
| `POST` | `/api/quiz/sessao` | Nova sessão UUID (sem persistência) | 200 |
| `POST` | `/api/quiz/resposta` | Upsert `DELETE+INSERT` por sessão; valida FKs | 201 / 404 / 422 |
| `GET` | `/api/quiz/resultado?sessao_id=...` | `{estilo_principal, pontuacao_principal/total, estilos_secundarios, todas_pontuacoes}` | 200 / 404 / 422 |
| `GET` | `/{full_path}` | SPA fallback — estáticos ou index.html; 404 JSON se `api*` | 200 / 404 |

---

## 5. Créditos Oficiais
* **Desenvolvedoras:** Laiara Emanuelly Marinho Barbosa & Yasmim Ribeiro dos Santos
* **Assistência de Programação:** OpenCode
