import React, { useState, useEffect } from 'react'

export default function ResultadoQuiz({ sessaoId, aoRefazer }) {
  const [resultado, setResultado] = useState(null)
  const [carregando, setCarregando] = useState(true)
  const [erro, setErro] = useState('')

  useEffect(() => {
    const carregarResultado = async () => {
      try {
        const resposta = await fetch(`/api/quiz/resultado?sessao_id=${sessaoId}`)
        const dados = await resposta.json()

        if (dados.sucesso) {
          setResultado(dados.dados)
        } else {
          setErro(dados.mensagem || 'Erro ao calcular resultado.')
        }
      } catch (err) {
        setErro('Erro de conexao com a API.')
      } finally {
        setCarregando(false)
      }
    }
    carregarResultado()
  }, [sessaoId])

  if (carregando) {
    return (
      <section className="min-h-[80vh] flex items-center justify-center">
        <div className="text-center space-y-4">
          <div className="w-10 h-10 border-4 border-rosaCha border-t-transparent rounded-full animate-spin mx-auto"></div>
          <p className="text-slate-600 text-sm">Calculando seu estilo...</p>
        </div>
      </section>
    )
  }

  if (erro) {
    return (
      <section className="min-h-[80vh] flex items-center justify-center px-4">
        <div className="text-center space-y-4">
          <p className="text-red-400 text-sm">{erro}</p>
          <button onClick={aoRefazer} className="px-4 py-2 rounded-xl bg-white border border-white/30 text-slate-700 text-sm font-semibold hover:bg-gray-100 transition">
            Refazer Quiz
          </button>
        </div>
      </section>
    )
  }

  const estilo = resultado.estilo_principal
  const secundarios = resultado.estilos_secundarios || []
  const pontuacoes = resultado.todas_pontuacoes || {}

  return (
    <section className="min-h-[80vh] py-20 px-4 sm:px-6 lg:px-8 relative overflow-hidden">
      <div className="absolute top-1/4 left-1/2 -translate-x-1/2 w-[700px] h-[500px] bg-gradient-to-tr from-rosaCha/20 via-pink-300/10 to-rosaBebe/20 rounded-full blur-[120px] pointer-events-none animate-pulse-glow"></div>

      <div className="max-w-3xl mx-auto relative z-10 space-y-10">
        <div className="text-center space-y-3">
          <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white border border-white/30 text-xs font-bold text-rosaCha">
            <span className="w-2 h-2 rounded-full bg-rosaCha animate-pulse"></span>
            <span>Resultado Calculado via FastAPI + SQLite</span>
          </div>
          <h1 className="text-3xl sm:text-4xl font-black text-gray-800 tracking-tight">
            Seu Estilo é:
          </h1>
        </div>

        <div className="bg-white backdrop-blur-2xl p-8 sm:p-10 rounded-3xl border border-white/30 shadow-2xl space-y-6">
          <div className="text-center space-y-2">
            <span className="text-5xl">{estilo.icone}</span>
            <h2 className="text-3xl sm:text-4xl font-black text-rosaCha">
              {estilo.nome}
            </h2>
            <p className="text-sm text-slate-500">
              {resultado.pontuacao_principal} pontos de {resultado.pontuacao_total} possíveis
            </p>
          </div>

          <p className="text-gray-700 text-center leading-relaxed">
            {estilo.descricao}
          </p>

          <div className="border-t border-white/20 pt-6">
            <h3 className="text-sm font-bold text-rosaCha uppercase tracking-wider mb-3">Dicas Práticas</h3>
            <div className="bg-white rounded-xl p-5 border border-white/30">
              <pre className="text-sm text-slate-700 whitespace-pre-wrap font-sans leading-relaxed">
                {estilo.dicas}
              </pre>
            </div>
          </div>
        </div>

        {secundarios.length > 0 && (
          <div className="space-y-4">
            <h3 className="text-sm font-bold text-slate-500 uppercase tracking-wider text-center">Estilos Compatíveis</h3>
            <div className="grid sm:grid-cols-2 gap-4">
              {secundarios.map(s => (
                <div key={s.id} className="bg-white backdrop-blur-xl p-6 rounded-2xl border border-white/30 text-center space-y-2">
                  <span className="text-2xl">{s.icone}</span>
                  <h4 className="text-lg font-bold text-gray-800">{s.nome}</h4>
                  <p className="text-xs text-slate-500">{s.pontuacao} pontos</p>
                </div>
              ))}
            </div>
          </div>
        )}

        <div className="bg-white backdrop-blur-xl p-6 rounded-2xl border border-white/30">
          <h3 className="text-sm font-bold text-slate-500 uppercase tracking-wider mb-4 text-center">Pontuação Completa</h3>
          <div className="space-y-3">
            {Object.entries(pontuacoes).map(([nome, pts]) => {
              const pct = Math.round((pts / resultado.pontuacao_total) * 100)
              return (
                <div key={nome} className="flex items-center gap-3">
                  <span className="text-xs font-bold text-slate-600 w-32 text-right truncate">{nome}</span>
                  <div className="flex-1 bg-white rounded-full h-3 overflow-hidden">
                    <div
                      className="h-full bg-gradient-to-r from-rosaCha to-rosaBebe rounded-full transition-all duration-700"
                      style={{ width: `${pct}%` }}
                    ></div>
                  </div>
                  <span className="text-xs font-mono text-slate-500 w-12 text-right">{pct}%</span>
                </div>
              )
            })}
          </div>
        </div>

        <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
          <button
            onClick={aoRefazer}
            className="px-8 py-4 rounded-2xl bg-gradient-to-r from-rosaCha via-pink-400 to-rosaBebe hover:from-rosaCha hover:to-pink-400 text-white font-extrabold text-base transition duration-300 shadow-xl shadow-rosaCha/25 hover:shadow-rosaCha/40 flex items-center gap-2"
          >
            <span>Refazer Quiz</span>
            <span>🔄</span>
          </button>
        </div>
      </div>
    </section>
  )
}
