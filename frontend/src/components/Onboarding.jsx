import React from 'react'

export default function Onboarding({ aoIniciar }) {
  return (
    <section className="min-h-[80vh] flex items-center justify-center px-4 sm:px-6 lg:px-8 relative overflow-hidden">
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[700px] h-[500px] bg-gradient-to-tr from-rosaCha/20 via-pink-300/10 to-rosaBebe/20 rounded-full blur-[120px] pointer-events-none animate-pulse-glow"></div>
      <div className="absolute top-10 right-10 w-72 h-72 bg-rosaCha/10 rounded-full blur-[80px] pointer-events-none"></div>

      <div className="max-w-2xl w-full text-center relative z-10 space-y-8">
        <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white border border-white/30 text-xs font-bold text-rosaCha">
            <span>Recomendador de Estilo Pessoal</span>
        </div>

        <div className="space-y-4">
          <h1 className="text-4xl sm:text-5xl lg:text-6xl font-black text-gray-800 tracking-tight leading-tight">
            Descubra seu{' '}
            <span className="text-rosaCha">
              Estilo
            </span>
          </h1>
          <p className="text-lg text-gray-700 max-w-xl mx-auto leading-relaxed">
            Responda um quiz rápido de 6 perguntas e descubra qual arquetipo de estilo combina mais com você. Minimalista, Streetwear, Classico, Boho ou Casual Chic.
          </p>
        </div>

        <div className="flex flex-wrap items-center justify-center gap-3 text-xs font-semibold text-gray-600">
          <span className="px-3 py-1.5 rounded-xl bg-white border border-white/30 text-rosaCha">
            6 Perguntas
          </span>
          <span className="px-3 py-1.5 rounded-xl bg-white border border-white/30 text-pink-500">
            5 Estilos
          </span>
          <span className="px-3 py-1.5 rounded-xl bg-white border border-white/30 text-rosaBebe">
            Resultado Instantâneo
          </span>
          <span className="px-3 py-1.5 rounded-xl bg-white border border-white/30 text-rosaCha">
            React + FastAPI + SQLite
          </span>
        </div>

        <button
          onClick={aoIniciar}
          className="px-10 py-5 rounded-2xl bg-gradient-to-r from-rosaCha via-pink-400 to-rosaBebe hover:from-rosaCha hover:to-pink-400 text-white font-extrabold text-lg transition duration-300 shadow-xl shadow-rosaCha/25 hover:shadow-rosaCha/40 flex items-center gap-3 mx-auto group"
        >
          <span>Iniciar Quiz de Estilo</span>
          <span className="group-hover:translate-x-1 transition-transform text-xl">➔</span>
        </button>

        <p className="text-xs text-gray-500">
          Desenvolvido por <strong className="text-gray-600">Laiara Emanuelly</strong> & <strong className="text-gray-600">Yasmim Ribeiro</strong>
        </p>
      </div>
    </section>
  )
}
