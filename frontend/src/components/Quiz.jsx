import React, { useState, useEffect } from 'react'

export default function Quiz({ aoFinalizar }) {
  const [perguntas, setPerguntas] = useState([])
  const [indiceAtual, setIndiceAtual] = useState(0)
  const [sessaoId, setSessaoId] = useState('')
  const [carregando, setCarregando] = useState(true)
  const [enviando, setEnviando] = useState(false)
  const [erro, setErro] = useState('')

  useEffect(() => {
    const carregarDados = async () => {
      try {
        const [resPerguntas, resSessao] = await Promise.all([
          fetch('/api/quiz/perguntas'),
          fetch('/api/quiz/sessao', { method: 'POST' })
        ])

        const dadosPerguntas = await resPerguntas.json()
        const dadosSessao = await resSessao.json()

        if (dadosPerguntas.sucesso) {
          setPerguntas(dadosPerguntas.dados)
        }
        if (dadosSessao.sucesso) {
          setSessaoId(dadosSessao.sessao_id)
        }
      } catch (err) {
        setErro('Erro ao carregar o quiz. Verifique se a API está rodando.')
      } finally {
        setCarregando(false)
      }
    }
    carregarDados()
  }, [])

  const selecionarOpcao = async (perguntaId, opcaoId) => {
    if (enviando) return
    setEnviando(true)
    setErro('')

    try {
      const resposta = await fetch('/api/quiz/resposta', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          sessao_id: sessaoId,
          pergunta_id: perguntaId,
          opcao_id: opcaoId
        })
      })

      const resultado = await resposta.json()

      if (!resultado.sucesso) {
        setErro(resultado.mensagem || 'Erro ao salvar resposta.')
        return
      }

      if (indiceAtual < perguntas.length - 1) {
        setIndiceAtual(prev => prev + 1)
      } else {
        aoFinalizar(sessaoId)
      }
    } catch (err) {
      setErro('Erro de conexao com a API.')
    } finally {
      setEnviando(false)
    }
  }

  if (carregando) {
    return (
      <section className="min-h-[80vh] flex items-center justify-center">
        <div className="text-center space-y-4">
          <div className="w-10 h-10 border-4 border-rosaCha border-t-transparent rounded-full animate-spin mx-auto"></div>
          <p className="text-slate-600 text-sm">Carregando perguntas...</p>
        </div>
      </section>
    )
  }

  if (erro && perguntas.length === 0) {
    return (
      <section className="min-h-[80vh] flex items-center justify-center px-4">
        <div className="text-center space-y-4">
          <p className="text-red-400 text-sm">{erro}</p>
          <button onClick={() => window.location.reload()} className="px-4 py-2 rounded-xl bg-white border border-slate-300 text-slate-700 text-sm font-semibold hover:bg-gray-100 transition">
            Tentar novamente
          </button>
        </div>
      </section>
    )
  }

  const pergunta = perguntas[indiceAtual]
  const progresso = ((indiceAtual + 1) / perguntas.length) * 100

  return (
    <section className="min-h-[80vh] flex items-center justify-center px-4 sm:px-6 lg:px-8 relative overflow-hidden">
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[400px] bg-gradient-to-r from-rosaCha/20 via-pink-300/10 to-rosaBebe/20 rounded-full blur-[100px] pointer-events-none"></div>

      <div className="max-w-2xl w-full relative z-10 space-y-8">
        <div className="text-center space-y-2">
          <span className="text-xs font-bold text-rosaCha">Pergunta {indiceAtual + 1} de {perguntas.length}</span>
          <div className="w-full bg-white rounded-full h-2.5 overflow-hidden">
            <div
              className="h-full bg-gradient-to-r from-rosaCha to-rosaBebe rounded-full transition-all duration-500 ease-out"
              style={{ width: `${progresso}%` }}
            ></div>
          </div>
        </div>

        <div className="bg-white backdrop-blur-2xl p-8 sm:p-10 rounded-3xl border border-white/30 shadow-2xl space-y-6">
          <h2 className="text-xl sm:text-2xl font-bold text-gray-800 text-center leading-relaxed">
            {pergunta.texto}
          </h2>

          <div className="grid gap-3">
            {pergunta.opcoes.map(opcao => (
              <button
                key={opcao.id}
                onClick={() => selecionarOpcao(pergunta.id, opcao.id)}
                disabled={enviando}
                className="w-full text-left px-5 py-4 rounded-xl bg-white border text-gray-800 font-medium text-sm hover:border-rosaCha hover:bg-gray-50 transition duration-200 cursor-not-allowed flex items-center gap-3 group"
              >
                <span className="w-8 h-8 rounded-lg bg-white border flex items-center justify-center text-xs font-bold text-rosaCha group-hover:border-rosaCha group-hover:text-rosaCha transition shrink-0">
                  {pergunta.opcoes.indexOf(opcao) + 1}
                </span>
                <span>{opcao.texto}</span>
              </button>
            ))}
          </div>

          {erro && (
            <p className="text-red-400 text-xs text-center">{erro}</p>
          )}

          {enviando && (
            <div className="flex items-center justify-center gap-2 text-xs text-gray-600">
              <div className="w-4 h-4 border-2 border-rosaCha border-t-transparent rounded-full animate-spin"></div>
              Salvando resposta...
            </div>
          )}
        </div>
      </div>
    </section>
  )
}
