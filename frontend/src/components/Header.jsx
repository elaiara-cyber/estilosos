import React from 'react'

export default function Header({ aoAbrirModalLeads, aoVoltarLanding }) {
  return (
    <>
      <header className="fixed top-0 left-0 w-full z-50 bg-slate-950/80 backdrop-blur-xl border-b border-slate-800/80 shadow-2xl">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
          
          {/* Logo & Stack Badge */}
          <div className="flex items-center gap-3">
            <div className="relative group">
              <div className="absolute -inset-0.5 bg-gradient-to-r from-rosaCha via-pink-300 to-rosaBebe rounded-2xl blur opacity-60 group-hover:opacity-100 transition duration-300"></div>
              <div className="relative w-11 h-11 rounded-2xl bg-slate-900 flex items-center justify-center text-2xl shadow-inner border border-slate-700">
                👗
              </div>
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="text-xl font-black tracking-tight text-white">
                  Estilo<span className="bg-gradient-to-r from-rosaCha via-pink-300 to-rosaBebe bg-clip-text text-transparent">sos</span>
                </span>
                <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-bold bg-rosaCha/20 text-rosaCha border border-rosaCha/30">
                  v2.0 Full Stack
                </span>
              </div>
              <p className="text-xs text-slate-400 hidden sm:block">
                Backend em <strong className="text-rosaCha font-semibold">Python (FastAPI)</strong> + Frontend em <strong className="text-rose-400 font-semibold">React 18</strong>
              </p>
            </div>
          </div>

          {/* Nav Links & Actions */}
          <div className="flex items-center gap-4">
            {aoVoltarLanding && (
              <button
                onClick={aoVoltarLanding}
                className="hidden md:inline-block text-xs font-semibold text-slate-300 hover:text-purple-400 transition py-2 px-3 rounded-lg hover:bg-slate-900"
              >
                ← Voltar
              </button>
            )}

            <a
              href="#tecnologias"
              className="hidden md:inline-block text-xs font-semibold text-slate-300 hover:text-rosaCha transition py-2 px-3 rounded-lg hover:bg-slate-900"
            >
              Arquitetura
            </a>

            <button
              onClick={aoAbrirModalLeads}
              className="hidden sm:flex items-center gap-2 text-xs font-bold text-slate-200 bg-slate-900/90 border border-slate-700/80 hover:border-rosaCha/50 hover:bg-slate-800 px-4 py-2 rounded-xl transition shadow-sm"
            >
              <span>🗄️ Ver Leads Gravados</span>
            </button>

            <a
              href="#formulario"
              className="relative inline-flex items-center justify-center p-0.5 overflow-hidden text-xs font-bold rounded-xl group bg-gradient-to-br from-rosaCha via-pink-400 to-transparent group-hover:from-rosaCha group-hover:to-pink-400 text-white shadow-lg shadow-rosaCha/20 hover:shadow-rosaCha/40 transition duration-300"
            >
              <span className="relative px-4 py-2.5 transition-all ease-in duration-75 bg-slate-950 rounded-[10px] group-hover:bg-opacity-0 flex items-center gap-1.5">
                                <span>🐍 Testar API Python</span>
              </span>
            </a>
          </div>

        </div>
      </header>

      {/* Spacer */}
      <div className="h-20"></div>
    </>
  )
}
