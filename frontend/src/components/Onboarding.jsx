import React from 'react'

export default function Onboarding({ aoIniciar }) {
  return (
    <section className="min-h-[80vh] flex items-center justify-center px-4 sm:px-6 lg:px-8 bg-slate-950 relative overflow-hidden">
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[700px] h-[500px] bg-gradient-to-tr from-purple-600/15 via-pink-600/10 to-cyan-600/15 rounded-full blur-[120px] pointer-events-none animate-pulse-glow"></div>
      <div className="absolute top-10 right-10 w-72 h-72 bg-cyan-500/10 rounded-full blur-[80px] pointer-events-none"></div>

      <div className="max-w-2xl w-full text-center relative z-10 space-y-8">
        <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-slate-900 border border-slate-800 text-xs font-bold text-purple-400">
          <span>Recomeendador de Estilo Pessoal</span>
        </div>

        <div className="space-y-4">
          <h1 className="text-4xl sm:text-5xl lg:text-6xl font-black text-white tracking-tight leading-tight">
            Descubra seu{' '}
            <span className="bg-gradient-to-r from-purple-400 via-pink-400 to-cyan-400 bg-clip-text text-transparent">
              Estilo
            </span>
          </h1>
          <p className="text-lg text-slate-300 max-w-xl mx-auto leading-relaxed">
            Responda um quiz rapido de 6 perguntas e descubra qual arquetipo de estilo combina mais com voce. Minimalista, Streetwear, Classico, Boho ou Casual Chic.
          </p>
        </div>

        <div className="flex flex-wrap items-center justify-center gap-3 text-xs font-semibold text-slate-400">
          <span className="px-3 py-1.5 rounded-xl bg-slate-900/80 border border-slate-800 text-purple-300">
            6 Perguntas
          </span>
          <span className="px-3 py-1.5 rounded-xl bg-slate-900/80 border border-slate-800 text-pink-300">
            5 Estilos
          </span>
          <span className="px-3 py-1.5 rounded-xl bg-slate-900/80 border border-slate-800 text-cyan-300">
            Resultado Instantaneo
          </span>
          <span className="px-3 py-1.5 rounded-xl bg-slate-900/80 border border-slate-800 text-emerald-300">
            React + FastAPI + SQLite
          </span>
        </div>

        <button
          onClick={aoIniciar}
          className="px-10 py-5 rounded-2xl bg-gradient-to-r from-purple-500 via-pink-500 to-cyan-500 hover:from-purple-400 hover:to-cyan-400 text-white font-extrabold text-lg transition duration-300 shadow-xl shadow-purple-500/25 hover:shadow-purple-500/40 flex items-center gap-3 mx-auto group"
        >
          <span>Iniciar Quiz de Estilo</span>
          <span className="group-hover:translate-x-1 transition-transform text-xl">➔</span>
        </button>

        <p className="text-xs text-slate-500">
          Desenvolvido por <strong className="text-slate-400">Laiara Emanuelly</strong> & <strong className="text-slate-400">Yasmim Ribeiro</strong>
        </p>
      </div>
    </section>
  )
}
