# Especificação de Requisitos de Sistema

**Projeto:** Estilosos — Recomendador de Estilo Pessoal  
**Versão:** 1.0  
**Data:** Setembro 2026  
**Autoras:** Laiara Emanuelly Marinho Barbosa e Yasmim Ribeiro dos Santos  
**Revisão Técnica:** OpenCode (Assistente de IA)

---

## 1. Visão Geral

Este documento especifica os requisitos técnicos de sistema do projeto **Estilosos**, uma aplicação web full-stack de recomendação de estilo pessoal. O sistema é composto por um frontend SPA em React e uma API REST em Python, comunicando de forma assíncrona via HTTP/JSON, com persistência em banco de dados SQLite.

---

## 2. Arquitetura do Sistema

### 2.1 Diagrama de Componentes

```
┌─────────────────────────────────────────────────────────┐
│                      CLIENTE (Browser)                   │
│                                                         │
│  ┌───────────────┐    ┌──────────────────────────────┐  │
│  │   React 18    │───▶│   Vite Dev Server (5173)     │  │
│  │   SPA + JSX   │    │   Proxy /api → :3000          │  │
│  └───────────────┘    └──────────────────────────────┘  │
└──────────────────────────┬──────────────────────────────┘
                           │ HTTP/JSON (fetch)
                           ▼
┌──────────────────────────────────────────────────────────┐
│                    SERVIDOR (Python)                      │
│                                                          │
│  ┌───────────────┐    ┌───────────────┐    ┌──────────┐ │
│  │  FastAPI +    │───▶│  Controladores │───▶│  SQLite  │ │
│  │  Uvicorn :3000│    │  (Lógica)      │    │  (WAL)   │ │
│  └───────────────┘    └───────────────┘    └──────────┘ │
└──────────────────────────────────────────────────────────┘
```

### 2.2 Stack Tecnológico

| Camada | Tecnologia | Versão | Responsabilidade |
|---|---|---|---|
| Frontend | React | 18.3.x | UI reativa com componentes funcionais |
| Build Tool | Vite | 5.4.x | Bundler, HMR, proxy de dev |
| Estilo | Tailwind CSS | 3.4.x | Utilitários de design responsivo |
| Backend | FastAPI | >= 0.115 | Framework ASGI de alta performance |
| Servidor | Uvicorn | >= 0.30 | Servidor ASGI assíncrono |
| Validação | Pydantic | >= 2.0 | Validação de schemas e serialização |
| Banco | SQLite | stdlib | Banco relacional embutido |
| Linguagem | Python | 3.13 | Backend |
| Linguagem | JavaScript (ESM) | — | Frontend |

### 2.3 Princípios Arquiteturais

1. **Separação de Responsabilidades:** Frontend (`frontend/`) e Backend (`api/`) são camadas independentes com interfaces bem definidas.
2. **API-First:** O contrato da API REST é a fonte única de comunicação entre as camadas.
3. **Stateless:** Cada requisição HTTP é independente; o estado do quiz é persistido no banco via `sessao_id`.
4. **Componentização:** O frontend é decomposto em componentes React de responsabilidade única.

---

## 3. Requisitos de Desempenho

| ID | Requisito | Critério Aceitável | Métrica |
|---|---|---|---|
| PERF-001 | Tempo de resposta da API | < 200ms para operações de leitura | Latência P95 |
| PERF-002 | Tempo de resposta da API | < 500ms para operações de escrita | Latência P95 |
| PERF-003 | Tempo de carregamento inicial do frontend | < 2s em conexão 3G | Lighthouse Performance |
| PERF-004 | Tempo de renderização do quiz | < 100ms por troca de pergunta | Core Web Vitals (INP) |
| PERF-005 | Throughput de sessões concorrentes | >= 100 sessões simultâneas | Requisições/segundo |
| PERF-006 | Tamanho do bundle de produção | < 500KB (gzipped) | `vite build --mode production` |

### 3.1 Otimizações Implementadas

- **SQLite WAL Mode:** Write-Ahead Logging habilitado para concorrência de leitura/escrita sem bloqueio.
- **Vite Code Splitting:** Chunk splitting automático por rotas e componentes lazy-loaded.
- **Tailwind Purge:** Remoção de classes CSS não utilizadas em produção.
- **Prepared Statements:** Queries SQL compiladas uma vez e reutilizadas.

---

## 4. Requisitos de Segurança

| ID | Requisito | Implementação | Critério |
|---|---|---|---|
| SEC-001 | Proteção contra XSS | `html.escape()` em todos os inputs sanitizados via Pydantic | Zero vulnerabilidade XSS |
| SEC-002 | Validação de entradas | Pydantic models com tipos estritos e `model_validator` | Rejeição de inputs inválidos |
| SEC-003 | Integridade referencial | FOREIGN KEYs habilitadas no SQLite | Zero dados órfãos |
| SEC-004 | Prevenção de SQL Injection | Prepared statements (parâmetros `?`) em todas as queries | Zero SQL injection |
| SEC-005 | CORS configurável | Middleware CORS com origem permitida via variável de ambiente | Apenas origens autorizadas |
| SEC-006 | Não exposição de secrets | Arquivo `.env` no `.gitignore`; chaves nunca hardcoded | Zero secrets no repositório |

### 4.1 Diretrizes de Segurança

- Nunca concatenar strings diretamente em queries SQL.
- Validar e sanitizar **todos** os dados vindos do cliente antes de processar.
- Utilizar apenas variáveis de ambiente para configurações sensíveis.
- Auditar dependências periodicamente (`pip audit`, `npm audit`).

---

## 5. Requisitos de Banco de Dados

### 5.1 Modelo de Dados

| Tabela | Registros | Descrição |
|---|---|---|
| `quiz_estilos` | 5 | Arquétipos de estilo (nome, descrição, dicas, ícone) |
| `quiz_perguntas` | 20 | Perguntas do quiz com ordenação |
| `quiz_opcoes` | 100 | Opções de resposta (5 por pergunta) com pontuação JSON |
| `quiz_respostas` | Variável | Respostas dos usuários por sessão |

### 5.2 Especificações Técnicas

| ID | Requisito | Especificação |
|---|---|---|
| DB-001 | Engine | SQLite 3.x embutido (sem servidor externo) |
| DB-002 | Modo de escrita | WAL (Write-Ahead Logging) habilitado |
| DB-003 | Chaves estrangeiras | `PRAGMA foreign_keys = ON` |
| DB-004 | Índices | Índices em `quiz_opcoes(pergunta_id)` e `quiz_respostas(sessao_id)` |
| DB-005 | Inicialização | Script `iniciar_banco.py` cria schema e popula dados seed |
| DB-006 | Localização | `api/db/landing.db` (arquivo único, sem servidor) |
| DB-007 | Row Factory | `sqlite3.Row` com `row_factory = dict` para acesso por nome de coluna |

### 5.3 Diagrama ER

```
┌──────────────────┐       ┌──────────────────┐
│   quiz_estilos   │       │  quiz_perguntas   │
├──────────────────┤       ├──────────────────┤
│ id (PK)          │       │ id (PK)          │
│ nome (UNIQUE)    │       │ texto            │
│ descricao        │       │ ordem            │
│ dicas            │       └────────┬─────────┘
│ icone            │                │
└──────────────────┘                │ 1:N
                                    ▼
                          ┌──────────────────┐
                          │  quiz_opcoes     │
                          ├──────────────────┤
                          │ id (PK)          │
                          │ pergunta_id (FK) │──▶ quiz_perguntas.id
                          │ texto            │
                          │ estilos_pontos   │  ← JSON: {"Minimalista": 3}
                          └──────────────────┘

                          ┌──────────────────┐
                          │ quiz_respostas   │
                          ├──────────────────┤
                          │ id (PK)          │
                          │ sessao_id        │  ← UUID (texto)
                          │ pergunta_id (FK) │──▶ quiz_perguntas.id
                          │ opcao_id (FK)    │──▶ quiz_opcoes.id
                          │ data_resposta    │  ← datetime('now','localtime')
                          └──────────────────┘
```

---

## 6. Requisitos de API

### 6.1 Contrato Geral

- **Protocolo:** HTTP/1.1
- **Formato:** application/json
- **Codificação:** UTF-8
- **Base URL (dev):** `http://localhost:3000`
- **Prefixo:** `/api`

### 6.2 Padronização de Respostas

```json
// Sucesso
{
  "sucesso": true,
  "dados": { ... },
  "mensagem": "Operação realizada com sucesso"
}

// Erro
{
  "sucesso": false,
  "mensagem": "Descrição do erro"
}
```

### 6.3 Endpoints

| Método | Endpoint | Body Request | Body Response | Status |
|---|---|---|---|---|
| `GET` | `/api/health` | — | `{sucesso, mensagem}` | 200 |
| `GET` | `/api/quiz/perguntas` | — | `{sucesso, dados: [...], total}` | 200 |
| `GET` | `/api/quiz/estilos` | — | `{sucesso, dados: [...]}` | 200 |
| `POST` | `/api/quiz/sessao` | — | `{sucesso, sessao_id, mensagem}` | 201 |
| `POST` | `/api/quiz/resposta` | `{sessao_id, pergunta_id, opcao_id}` | `{sucesso, mensagem}` | 201 |
| `GET` | `/api/quiz/resultado?sessao_id=X` | — | `{sucesso, dados: {principal, secundarios, pontuacoes}}` | 200 |

### 6.4 Tratamento de Erros

| Código HTTP | Significado | Causa |
|---|---|---|
| 200 | OK | Operação bem-sucedida |
| 201 | Created | Recurso criado com sucesso |
| 400 | Bad Request | Dados mal formatados ou campos obrigatórios ausentes |
| 404 | Not Found | Recurso não encontrado ou rota inexistente |
| 422 | Unprocessable Entity | Validação de negócio falhou (ex: sessão sem respostas) |
| 500 | Internal Server Error | Erro interno do servidor |

### 6.5 Middlewares

| Middleware | Configuração | Finalidade |
|---|---|---|
| CORS | `allow_origins`, `allow_methods=["*"]`, `allow_headers=["*"]` | Cross-origin requests |
| SPA Fallback | Catch-all `/{path}` serve `index.html` | Navegação client-side |

---

## 7. Requisitos de Frontend

### 7.1 Especificações Técnicas

| ID | Requisito | Especificação |
|---|---|---|
| FE-001 | Framework | React 18 com componentes funcionais e hooks |
| FE-002 | Build Tool | Vite 5.x com HMR (Hot Module Replacement) |
| FE-003 | CSS | Tailwind CSS 3.x com classes utilitárias |
| FE-004 | Módulos | ES Modules (`"type": "module"` no package.json) |
| FE-005 | Fonte | Plus Jakarta Sans (Google Fonts) |
| FE-006 | Comunicação | `fetch` API nativa (sem Axios) |
| FE-007 | Estado | `useState` e `useEffect` (sem Redux/Zustand) |
| FE-008 | Roteamento | Navegação por estado (`useState`), sem React Router |

### 7.2 Componentes Ativos

| Componente | Responsabilidade | Estado |
|---|---|---|
| `Onboarding.jsx` | Tela inicial com CTA e informações do quiz | Ativo |
| `Quiz.jsx` | Renderização de perguntas, seleção de opções, envio de respostas | Ativo |
| `ResultadoQuiz.jsx` | Exibição de resultados, gráfico de barras, dicas | Ativo |
| `App.jsx` | Gerenciamento de navegação (landing → quiz → resultado) | Ativo |

### 7.3 Fluxo de Navegação

```
┌─────────────┐    iniciarQuiz()    ┌─────────────┐    aoFinalizar()    ┌─────────────────┐
│  Onboarding │───────────────────▶│     Quiz     │──────────────────▶│  ResultadoQuiz  │
│  (landing)  │                    │  (20 itens)  │                    │  (resultado)    │
└─────────────┘                    └──────────────┘                    └────────┬────────┘
       ▲                                                                        │
       │                          refazerQuiz()                                 │
       └────────────────────────────────────────────────────────────────────────┘
```

### 7.4 Identidade Visual (Tema Rose Pink)

| Elemento | Especificação |
|---|---|
| Gradiente de fundo | `from-rosaCha (#FFB6C1) to-rosaBebe (#FFC0CB)` |
| Cor de destaque | `pink-400 (#F472B6)` |
| Cards | Glassmorphism claro: `bg-white/80 backdrop-blur-2xl rounded-3xl border-white/30` |
| Botão primário | Gradiente `from-rosaCha via-pink-400 to-rosaBebe`, texto branco, `rounded-2xl` |
| Tipografia | Plus Jakarta Sans (400–800) |
| Animações | `animate-pulse-glow` (orbs), `animate-float` (flutuação), transições em barra de progresso |

---

## 8. Requisitos de Integração

### 8.1 Comunicação Frontend-Backend

| ID | Requisito | Implementação |
|---|---|---|
| INT-001 | Proxy de desenvolvimento | Vite proxy: `/api` → `http://localhost:3000` |
| INT-002 | Modo produção | FastAPI serve arquivos estáticos de `frontend/dist/` |
| INT-003 | Formato de dados | JSON com `Content-Type: application/json` |
| INT-004 | CORS | Middleware configurado via env `ORIGEM_PERMITIDA` |

### 8.2 Fluxo de Dados do Quiz

```
1. Frontend → POST /api/quiz/sessao          → Backend gera UUID
2. Frontend → GET  /api/quiz/perguntas       → Backend retorna 20 perguntas + opções
3. Frontend → POST /api/quiz/resposta (×20)  → Backend salva cada resposta
4. Frontend → GET  /api/quiz/resultado       → Backend calcula e retorna resultado
```

---

## 9. Requisitos de Deploy

### 9.1 Ambiente de Desenvolvimento

| Serviço | Porta | Comando |
|---|---|---|
| FastAPI (Uvicorn) | 3000 | `python main.py` |
| Vite Dev Server | 5173 | `npm run dev` |

### 9.2 Ambiente de Produção

| ID | Requisito | Especificação |
|---|---|---|
| DEP-001 | Build do frontend | `npm run build` → gera `frontend/dist/` |
| DEP-002 | Serviço único | FastAPI serve API + arquivos estáticos na porta 3000 |
| DEP-003 | Variáveis de ambiente | `PORT`, `ORIGEM_PERMITIDA` via `.env` ou env do sistema |
| DEP-004 | Banco de dados | Arquivo SQLite persistido em `api/db/landing.db` |

### 9.3 Checklist de Deploy

- [ ] `npm run build` executado sem erros
- [ ] `requirements.txt` atualizado
- [ ] Variáveis de ambiente configuradas
- [ ] Banco de dados inicializado (`iniciar_banco.py`)
- [ ] Testes de integração validados (sessão + 20 respostas + resultado)
- [ ] Health check respondendo (`GET /api/health`)

---

## 10. Requisitos de Manutenibilidade

| ID | Requisito | Critério |
|---|---|---|
| MAN-001 | Separação de camadas | Frontend e Backend independentes, sem dependências cruzadas |
| MAN-002 | Nomenclatura | Snake_case para Python, camelCase para JavaScript/JSX |
| MAN-003 | Estrutura de pastas | Padrão MVC: `rotas/`, `controladores/`, `config/`, `utilitarios/` |
| MAN-004 | Documentação | README.md atualizado com instruções de setup e endpoints |
| MAN-005 | Versionamento | Git com commits semânticos e branches para features |

---

## 11. Restrições e Dependências

### 11.1 Restrições Técnicas

- Python >= 3.11 (compatibilidade com FastAPI e type hints)
- Node.js >= 18 (compatibilidade com Vite 5.x)
- SQLite >= 3.35 (suporte a `RETURNING` e funções de janela)

### 11.2 Dependências Externas

| Dependência | Finalidade | Licença |
|---|---|---|
| FastAPI | Framework web async | MIT |
| Uvicorn | Servidor ASGI | BSD-3 |
| Pydantic | Validação de dados | MIT |
| React | Biblioteca UI | MIT |
| Vite | Build tool | MIT |
| Tailwind CSS | CSS utility-first | MIT |

---

## 12. Critérios de Aceite

| ID | Critério | Validação |
|---|---|---|
| AC-001 | Quiz funcional com 20 perguntas | Teste manual completo do fluxo |
| AC-002 | Resultado correto para todas as combinações | Testes automatizados de pontuação |
| AC-003 | API respondendo em < 200ms | Benchmark com ferramenta de load test |
| AC-004 | Frontend responsivo | Teste em dispositivos móveis e desktop |
| AC-005 | Zero erros no build de produção | `npm run build` sem warnings |
| AC-006 | Health check operacional | `curl localhost:3000/api/health` retorna 200 |
