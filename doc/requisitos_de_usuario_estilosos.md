# Especificação de Requisitos de Usuário (UML 2.5.1)

**Projeto:** Estilosos — Sistema de Recomendação de Estilo Vestuário  
**Instituição:** Instituto Federal de Mato Grosso — Campus Barra do Garças  
**Curso:** Técnico em Informática (3º Ano B) — 2026  
**Autoras:** Laiara Emanuelly Marinho Barbosa e Yasmim Ribeiro dos Santos  
**Orientador:** Prof. Carlos David Rocha de Souza  
**Disciplina:** Desenvolvimento para Web  

---

## 1. Visão Geral do Sistema
O **Estilosos** é um sistema full-stack acadêmico projetado como um recomendador de estilo pessoal. O sistema guia o usuário através de um quiz interativo de 20 perguntas para identificar seu arquétipo de moda predominante (*Minimalista, Streetwear, Clássico, Boho ou Casual Chic*) e fornece recomendações personalizadas com dicas práticas de vestuário.

---

## 2. Atores do Sistema (UML 2.5.1 - *Actors*)

Segundo a especificação UML 2.5.1 (seção 18.1), um *Actor* especifica um papel desempenhado por um usuário externo ou sistema que interage com o assunto (*Subject*).

| Ator | Tipo UML | Descrição / Responsabilidades |
|---|---|---|
| **Usuário Final (Visitante)** | Ator Humano (Principal) | Interage com o Quiz de 20 perguntas, visualiza os resultados de estilo personalizado e pode refazer o questionário. |
| **Sistema de API REST (FastAPI)** | Ator de Sistema (Autônomo) | Valida/sanitiza os dados, processa os algoritmos de pontuação do quiz e efetua as operações CRUD de persistência no SQLite. |

---

## 3. Diagrama e Casos de Uso (*Use Cases*)

```text
 +---------------------------------------------------------------------------------+
 |                              SISTEMA ESTILOSOS                                  |
 |                                                                                 |
 |    (UC01: Iniciar Sessão do Quiz) <------ (<<include>>) <---+                  |
 |                   ^                                         |                   |
 |                   |                                         |                   |
 |    (UC02: Responder Quiz de 20 Perguntas)                   |                   |
 |                   ^                                         |                   |
 |                   |                                         |                   |
 |    (UC03: Visualizar Resultado e Arquétipo)                 |                   |
 |                                                             |                   |
 |    (UC04: Refazer Quiz) -----------------------------------+                   |
 |                                                                                 |
 |    (UC05: Health Check da API) <================================= [Sistema]    |
 +---------------------------------------------------------------------------------+
        ^
        |
 [Usuário Final]
```

### Detalhamento dos Casos de Uso

* **UC01 — Iniciar Sessão do Quiz:** O Usuário Final solicita o início de um novo teste; o sistema gera um identificador único de sessão (UUID).
* **UC02 — Responder Quiz de Estilo:** O Usuário responde às 20 perguntas de múltipla escolha. Cada resposta é enviada individualmente via API.
* **UC03 — Visualizar Resultado:** O sistema exibe o arquétipo vencedor com ícone, descrição e dicas práticas, além de até 2 estilos secundários compatíveis e um gráfico de barras com a pontuação completa.
* **UC04 — Refazer Quiz:** O Usuário pode reiniciar o questionário, voltando à tela de Onboarding.
* **UC05 — Monitorar Saúde da API:** Verificação do status do servidor através do endpoint `GET /api/health`.

---

## 4. Requisitos Funcionais (RF)

| Código | Requisito Funcional | Descrição | Prioridade |
|---|---|---|---|
| **RF-001** | Criar Sessão do Quiz | O sistema deve gerar uma sessão com ID único (UUID) para cada execução do quiz via `POST /api/quiz/sessao`. | **Alta** |
| **RF-002** | Exibir Quiz de 20 Questões | O sistema deve renderizar 20 perguntas de múltipla escolha, cada uma com 5 opções. | **Alta** |
| **RF-003** | Barra de Progresso e Navegação | O frontend deve fornecer navegação fluida com indicador animado de progresso entre as questões. | **Média** |
| **RF-004** | Calcular Arquétipo de Estilo | O backend deve processar a pontuação e definir o estilo vencedor entre: *Minimalista, Streetwear, Clássico, Boho e Casual Chic*. | **Alta** |
| **RF-005** | Exibir Resultados e Recomendação | A interface deve apresentar o perfil principal com descrição e dicas, ranking secundário (até 2 estilos) e gráfico de barras com pontuação completa. | **Alta** |
| **RF-006** | Refazer Quiz | O usuário deve poder reiniciar o questionário a qualquer momento pela tela de resultados. | **Média** |
| **RF-007** | Health Check da API | O sistema deve disponibilizar um endpoint de verificação de saúde (`GET /api/health`). | **Baixa** |

---

## 5. Requisitos Não-Funcionais (RNF)

| Código | Categoria | Descrição / Restrição Técnica | Métrica / Critério |
|---|---|---|---|
| **RNF-001** | Segurança | Sanitização de dados contra ataques XSS no backend FastAPI via `html.escape` em validadores Pydantic. | Zero vulnerabilidade XSS |
| **RNF-002** | Desempenho & Banco | Utilização do banco de dados relacional SQLite configurado com modo WAL (Write-Ahead Logging). | Resposta `< 200ms` |
| **RNF-003** | Arquitetura | Comunicação assíncrona entre React 18 e FastAPI via requisições `fetch` com CORS ativo. | Interatividade SPA sem reload |
| **RNF-004** | Usabilidade & UI | Design reativo na paleta de cores Rose Pink, responsivo em dispositivos móveis com Tailwind CSS v3. | 100% Responsivo |
| **RNF-005** | Manutenibilidade | Separação clara de responsabilidades: frontend em componentes React e backend com controladores/rotas. | Baixo Acoplamento |

---

## 6. Domínio dos Arquétipos de Estilo

1. **◻ Minimalista:** Peças de corte limpo, cores neutras e tecidos nobres.
2. **🛹 Streetwear:** Cultura urbana, gráficos ousados, modelagem oversized e tênis.
3. **🎩 Clássico:** Alfaiataria tradicional, elegância atemporal e sobriedade.
4. **🌿 Boho:** Estampas étnicas, tecidos naturais e fluídos, e acessórios artesanais.
5. **✨ Casual Chic:** Equilíbrio moderno entre conforto e sofisticação refinada.

---

## 7. Matriz de Rastreabilidade

| Requisito | Componente React (Frontend) | Componente Python (Backend) | Rota / Endpoint |
|---|---|---|---|
| **RF-001** | `Onboarding.jsx`, `Quiz.jsx` | `quiz_controlador.py`, `quiz_rotas.py` | `POST /api/quiz/sessao` |
| **RF-002 / RF-003** | `Quiz.jsx` | `quiz_controlador.py`, `quiz_rotas.py` | `GET /api/quiz/perguntas` |
| **RF-004** | `Quiz.jsx` | `quiz_controlador.py`, `quiz_rotas.py` | `POST /api/quiz/resposta` |
| **RF-005** | `ResultadoQuiz.jsx` | `quiz_controlador.py`, `quiz_rotas.py` | `GET /api/quiz/resultado` |
| **RF-006** | `ResultadoQuiz.jsx`, `App.jsx` | — | Navegação por estado |
| **RF-007** | — | `app.py` | `GET /api/health` |
| **RNF-001** | — | `validadores.py` | — |
| **RNF-002** | — | `conexao_banco.py` | — |
| **RNF-003** | `App.jsx`, `Quiz.jsx` | `app.py` (CORS) | Todos os endpoints |
| **RNF-004** | `index.css`, `tailwind.config.js` | — | — |
| **RNF-005** | `components/` | `controladores/`, `rotas/` | — |
