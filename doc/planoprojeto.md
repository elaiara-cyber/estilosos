# Plano de Desenvolvimento do Projeto: Recomendador de Estilo Pessoal

**Dupla Criadora:** Laiara Emanuelly Marinho Barbosa e Yasmim Ribeiro dos Santos  
**Ferramenta de IA/Assistente:** OpenCode  
**Base Tecnológica:** Arquitetura e linguagens já existentes descritas no arquivo `README.md` do repositório.

---

## 0. Stack Tecnológico Oficial (Conforme README.md)

* **Front-end:** React 18 (Vite + Tailwind CSS v3) — componentes reativos com JSX e React Hooks (`useState`, `useEffect`), máscaras dinâmicas e integração assíncrona via `fetch`. Estética **Dark Glassmorphism** com Google Fonts (*Plus Jakarta Sans* e *Fira Code*).
* **Back-end:** Python 3.13 + FastAPI + Uvicorn — API RESTful de alta performance, com Pydantic e validadores (`html.escape`) para sanitização anti-XSS, e Middleware CORS.
* **Banco de Dados:** SQLite (sqlite3) — relacional embutido com *Prepared Statements* e modo WAL.
* **Estrutura:** Backend em `api/` (rotas, controladores, utilitários) e Frontend em `frontend/` (componentes React), servidos em modo dev nas portas 3000 (FastAPI) e 5173 (Vite).

---

## 1. Diretrizes para o OpenCode (Regras de Ouro)
* **Respeito ao Legado:** O OpenCode deve ler rigorosamente o arquivo `README.md` antes de gerar qualquer código para identificar o stack tecnológico oficial (React 18 + Vite + Tailwind, Python 3 + FastAPI, SQLite).
* **Separação de Camadas:** Manter a estrita separação entre Front-end (`frontend/`) e Back-end (`api/`) conforme a arquitetura preexistente no repositório.
* **Padrões do Back-end:** Seguir a estrutura existente de `api/src/config/conexao_banco.py` (row_factory dict, modo WAL), `api/src/controladores/`, `api/src/rotas/` e `api/src/utilitarios/validadores.py`, expondo endpoints via `api/src/app.py` e `api/main.py` (Uvicorn na porta 3000).
* **Padrões do Front-end:** Reutilizar os componentes React de `frontend/src/components/` (Header, Hero, Beneficios, FormularioLead, ModalLeads, Toast, Footer) e a estética Dark Glassmorphism de `frontend/src/index.css`.
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
  * `api/iniciar_banco.py` — Tabelas `quiz_estilos`, `quiz_perguntas`, `quiz_opcoes`, `quiz_respostas` com seed de dados (5 estilos, 6 perguntas, 24 opções).
  * `api/src/controladores/quiz_controlador.py` — Lógica de pontuação, cálculo de resultado, listagem de perguntas e criação de sessão.
  * `api/src/rotas/quiz_rotas.py` — Endpoints RESTful: `POST /api/quiz/sessao`, `GET /api/quiz/perguntas`, `GET /api/quiz/estilos`, `POST /api/quiz/resposta`, `GET /api/quiz/resultado`.
  * `api/src/app.py` — Inclusão do router do quiz via `app.include_router(quiz_router, prefix="/api")`.
* **Entregável:** Endpoints de API funcionais, validados e sanitizados no padrão do projeto.

### Fase 3: Desenvolvimento do Front-end ✅ CONCLUÍDA
* **Arquivos criados/atualizados:**
  * `frontend/src/components/Onboarding.jsx` — Tela inicial do quiz com título, descrição dos 5 estilos e botão de início.
  * `frontend/src/components/Quiz.jsx` — Interface do quiz com barra de progresso, seleção de opções e envio assíncrono via `fetch`.
  * `frontend/src/components/ResultadoQuiz.jsx` — Página de resultados com arquétipo principal, estilos secundários, barras de pontuação e dicas práticas.
  * `frontend/src/App.jsx` — Integração das 3 telas do quiz (Onboarding → Quiz → ResultadoQuiz) com navegação de estado.
  * `frontend/src/components/Header.jsx` — Botão "← Voltar" para navegação do quiz.
* **Entregável:** Interface web responsiva e integrada, no padrão Dark Glassmorphism do projeto.

### Fase 4: Testes, Ajustes e Documentação ✅ CONCLUÍDA
* **Ações executadas:**
  * Testes de integração: criação de sessão, envio de 6 respostas e cálculo de resultado validados via `curl`.
  * Validação do build do React (`npm run build` sem erros).
  * Validação dos endpoints do FastAPI (health check, perguntas, estilos, respostas, resultado).
  * Correção de bug: colunas `texto` e `ordem` da tabela `quiz_perguntas` invertidas no INSERT.
  * Atualização do `README.md` com documentação completa do quiz e novos endpoints.
* **Entregável:** Código testado, limpo e pronto para deploy.

---

## 3. Créditos Oficiais
* **Desenvolvedoras:** Laiara Emanuelly Marinho Barbosa & Yasmim Ribeiro dos Santos
* **Assistência de Programação:** OpenCode
