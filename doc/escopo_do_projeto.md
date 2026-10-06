# Escopo do Projeto: Recomendador de Estilo Pessoal

---

## 1. Visão Geral do Projeto
Desenvolver uma aplicação web interativa onde os usuários respondem a um questionário de estilo de 20 perguntas e recebem recomendações personalizadas de moda com base em 5 arquétipos de estilo.

## 2. Objetivos Principais
* **Engajamento do Usuário:** Criar um quiz dinâmico, visual e intuitivo com 3 telas: Onboarding, Quiz e Resultado.
* **Personalização:** Mapear as respostas do usuário para arquétipos de estilo específicos (Minimalista, Streetwear, Clássico, Boho, Casual Chic).
* **Resultado Instantâneo:** Entregar o perfil de estilo principal, estilos secundários compatíveis e dicas práticas de vestuário.

---

## 3. Requisitos Funcionais

### A. Tela de Onboarding (Intro)
* Tela inicial com badge "Recomendador de Estilo Pessoal".
* Título destacado "Descubra seu Estilo".
* Badges informativos: 20 Perguntas, 5 Estilos, Resultado Instantâneo, React + FastAPI + SQLite.
* Botão CTA "Iniciar Quiz de Estilo" com gradiente rosa.

### B. Quiz Interativo (20 Perguntas)
* Série de 20 perguntas de múltipla escolha, cada uma com 5 opções (100 opções no total, seed em `api/iniciar_banco.py`).
* Contador `Pergunta X de 20` + barra de progresso animada em gradiente rosa.
* Opções numeradas com cursor customizado de coração rosa e hover `hover:border-rosaCha`.
* Carregamento paralelo via `Promise.all`: `GET /api/quiz/perguntas` + `POST /api/quiz/sessao`.
* Envio assíncrono de cada resposta via `POST /api/quiz/resposta` (upsert por sessão).
* Estados: `Carregando perguntas...`, `Salvando resposta...`, erro + `Tentar novamente`.
* Gerenciamento de sessão com UUID único (sem tabela de sessão — apenas `quiz_respostas.sessao_id`).

### C. Página de Resultados
* Badge `Resultado Calculado via FastAPI + SQLite` + título `Seu Estilo é:`.
* **Arquétipo Principal:** estilo vencedor com ícone (5xl), nome, `X pontos de Y possíveis`, descrição integral e bloco `Dicas Práticas`.
* **Estilos Secundários:** até 2 estilos compatíveis em grid (`Estilos Compatíveis`).
* **Pontuação Completa:** barras em percentual (`%`) com gradiente rosa.
* **Refazer Quiz:** botão `Refazer Quiz 🔄` volta ao Onboarding; estado `Calculando seu estilo...` + erro com `Refazer Quiz`.
* Navegação por `useState` em `App.jsx` (sem React Router): `landing → quiz → resultado`.

---

## 4. Requisitos Não Funcionais
* **Responsividade:** Design totalmente adaptado para dispositivos móveis (smartphones e tablets) e desktops.
* **Desempenho:** Comunicação assíncrona via `fetch` com a API FastAPI.
* **Usabilidade:** Interface limpa, moderna e alinhada ao universo da moda com tema visual Rose Pink (glassmorphism claro).
* **Segurança:** Sanitização de dados contra ataques XSS via `html.escape` no backend.

---

## 5. Stack Tecnológico
* **Front-end:** React 18 (Vite + Tailwind CSS v3)
* **Back-end:** Python 3.13 + FastAPI + Uvicorn (porta 3000)
* **Banco de Dados:** SQLite (modo WAL)
* **Estrutura:** Backend em `api/` (rotas, controladores, utilitários) e Frontend em `frontend/` (componentes React)

---

## 6. Fluxo de Navegação

```
Onboarding → [Iniciar Quiz] → Quiz → [Responder 20 perguntas] → ResultadoQuiz → [Refazer Quiz] → Onboarding
```

---

## 7. Cronograma Sugerido (Fases de Desenvolvimento)

| Fase | Descrição | Principais Entregas |
| :--- | :--- | :--- |
| **Fase 1: Concepção** | Planejamento e Arquitetura | Definição dos 5 arquétipos de estilo e estrutura do quiz. |
| **Fase 2: Banco de Dados** | Estruturação de Conteúdo | Tabelas SQLite: estilos, perguntas, opções e respostas com seed de 20 perguntas. |
| **Fase 3: Desenvolvimento** | Codificação Front-end e Back-end | Quiz interativo com 3 telas e API RESTful com endpoints de sessão, respostas e resultado. |
| **Fase 4: Testes** | Validação e Ajustes | Testes de integração, validação de endpoints e otimização mobile. |
| **Fase 5: Lançamento** | Deploy | Publicação do site em ambiente de produção. |
