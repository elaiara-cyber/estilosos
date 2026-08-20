import React from 'react'

export default function Footer({ aoAbrirModalLeads }) {
  return (
    <footer className="bg-slate-50 text-slate-600 py-12 px-4 sm:px-6 lg:px-8 border-t border-white/30">
      <div className="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-6 text-center md:text-left">
        
        {/* Marca & Descrição */}
        <div className="space-y-1">
          <div className="flex items-center justify-center md:justify-start gap-2">
            <span className="text-xl">👗</span>
            <span className="text-lg font-black text-gray-800 tracking-tight">Estilosos Full Stack</span>
          </div>
          <p className="text-xs text-slate-500">
            Projeto Acadêmico para demonstração de arquitetura <strong className="text-rosaCha">Python (FastAPI)</strong> + <strong className="text-rose-400">React 18</strong> + <strong className="text-rosaBebe">SQLite</strong>.
          </p>
        </div>

        {/* Badges & Atalho Modal */}
        <div className="flex flex-wrap items-center justify-center gap-3 text-xs">
          <span className="px-3 py-1.5 rounded-xl bg-white/80 text-slate-500 border border-white/30">
            Backend: Python / FastAPI
          </span>
          <span className="px-3 py-1.5 rounded-xl bg-white/80 text-slate-500 border border-white/30">
            Frontend: React 18 / Vite
          </span>
          <span className="px-3 py-1.5 rounded-xl bg-white/80 text-slate-500 border border-white/30">
            Banco: SQLite
          </span>
          <button
            onClick={aoAbrirModalLeads}
            className="px-3 py-1.5 rounded-xl bg-rosaCha/20 text-rosaCha hover:bg-rosaCha/30 border border-rosaCha/30 transition font-bold"
          >
            🗄️ Ver Leads SQLite
          </button>
        </div>

      </div>

      <div className="max-w-7xl mx-auto border-t border-white/20 mt-8 pt-6 text-center text-xs text-slate-500">
        &copy; 2026 Estilosos. Desenvolvido para fins acadêmicos e educacionais.
      </div>
    </footer>
  )
}
