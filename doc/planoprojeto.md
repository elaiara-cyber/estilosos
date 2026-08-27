# Plano de Desenvolvimento do Projeto: Estilosos — Recomendador de Estilo Pessoal

**Dupla Criadora:** Laiara Emanuelly Marinho Barbosa e Yasmim Ribeiro dos Santos  
**Ferramenta de IA/Assistente:** OpenCode  
**Base Tecnológica:** Arquitetura, estética e linguagens já existentes descritas no arquivo `README.md` e nos códigos-fonte do repositório.

---

## 0. Stack Tecnológico Oficial (Conforme README.md)

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

1. **Onboarding** — tela inicial com badge "Recomendador de Estilo Pessoal", título "Descubra seu **Estilo**" (destaque sólido em `pink-400`), badges informativos (20 Perguntas, 5 Estilos, Resultado Instantâneo, React + FastAPI + SQLite) e CTA de início.
2. **Quiz** — cartão branco com pergunta atual, contador "Pergunta X de 6", barra de progresso gradiente e opções numeradas com hover rosa; envio assíncrono de cada resposta.
3. **ResultadoQuiz** — arquétipo vencedor com ícone, pontuação, dicas práticas, estilos secundários compatíveis e gráfico de barras com a pontuação completa dos 5 estilos.

> **Nota:** os componentes de landing page legados (`Header.jsx`, `Hero.jsx`, `Beneficios.jsx`, `FormularioLead.jsx`, `ModalLeads.jsx`, `Toast.jsx` e `Footer.jsx`) permanecem no diretório `frontend/src/components/` para uso futuro, mas não são montados pelo `App.jsx` na navegação atual.

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
* **Ação do OpenCode:**
  * Ler e analisar o arquivo `README.md` para mapear o stack tecnológico oficial (React 18 + Vite + Tailwind CSS, Python 3 + FastAPI + Uvicorn, SQLite) e a estrutura de pastas (`api/`, `frontend/`, `doc/`).
  * Verificar dependências no `api/requirements.txt` e `frontend/package.json` e garantir que o ambiente local esteja pronto para desenvolvimento Full-stack (Uvicorn na porta 3000 e Vite na porta 5173).
* **Entregável:** Relatório de compatibilidade e estrutura mapeada pelo OpenCode.

### Fase 2: Desenvolvimento do Back-end ✅ CONCLUÍDA
* **Arquivos criados/atualizados:**
  * `api/iniciar_banco.py` — Tabelas `leads`, `quiz_estilos`, `quiz_perguntas`, `quiz_opcoes`, `quiz_respostas` com seed de dados (5 estilos, 20 perguntas em 4 categorias, 100 opções).
  * `api/src/controladores/lead_controlador.py` — Cadastro e listagem de leads com sanitização anti-XSS.
  * `api/src/controladores/quiz_controlador.py` — Lógica de pontuação, cálculo de resultado, listagem de perguntas e criação de sessão.
  * `api/src/rotas/lead_rotas.py` — Endpoints `POST /api/leads` e `GET /api/leads`.
  * `api/src/rotas/quiz_rotas.py` — Endpoints RESTful: `POST /api/quiz/sessao`, `GET /api/quiz/perguntas`, `GET /api/quiz/estilos`, `POST /api/quiz/resposta`, `GET /api/quiz/resultado`.
  * `api/src/app.py` — Inclusão dos routers via `app.include_router(..., prefix="/api")`.
* **Entregável:** Endpoints de API funcionais, validados e sanitizados no padrão do projeto.

### Fase 3: Desenvolvimento do Front-end ✅ CONCLUÍDA
* **Arquivos criados/atualizados:**
  * `frontend/src/components/Onboarding.jsx` — Tela inicial do quiz com badge, título destacado, badges informativos e CTA gradiente.
  * `frontend/src/components/Quiz.jsx` — Interface do quiz com barra de progresso animada, seleção de opções e envio assíncrono via `fetch`.
  * `frontend/src/components/ResultadoQuiz.jsx` — Página de resultados com arquétipo principal, estilos secundários, barras de pontuação e dicas práticas.
  * `frontend/src/App.jsx` — Integração das 3 telas do quiz (Onboarding → Quiz → ResultadoQuiz) com navegação por estado e fundo Rose Pink.
* **Entregável:** Interface web responsiva e integrada, no padrão visual **Rose Pink** (glassmorphism claro) do projeto.

### Fase 4: Testes, Ajustes e Documentação ✅ CONCLUÍDA
* **Ações executadas:**
  * Testes de integração: criação de sessão, envio de 6 respostas e cálculo de resultado validados via `curl`.
  * Validação do build do React (`npm run build` sem erros).
  * Validação dos endpoints do FastAPI (health check, perguntas, estilos, respostas, resultado).
  * Correção de bug: colunas `texto` e `ordem` da tabela `quiz_perguntas` invertidas no INSERT.
  * Atualização do `README.md` com documentação completa do quiz e novos endpoints.
  * Refinamentos visuais na tela Onboarding (destaque do título "Estilo" alinhado à identidade rosa dos botões).
* **Entregável:** Código testado, limpo e pronto para deploy.

---

## 3. Créditos Oficiais
* **Desenvolvedoras:** Laiara Emanuelly Marinho Barbosa & Yasmim Ribeiro dos Santos
* **Assistência de Programação:** OpenCode
