import React, { useState } from 'react'
import Quiz from './components/Quiz'
import ResultadoQuiz from './components/ResultadoQuiz'
import Onboarding from './components/Onboarding'

export default function App() {
  const [telaQuiz, setTelaQuiz] = useState('landing')
  const [sessaoQuiz, setSessaoQuiz] = useState('')

  const iniciarQuiz = () => setTelaQuiz('quiz')

  const finalizarQuiz = (sessaoId) => {
    setSessaoQuiz(sessaoId)
    setTelaQuiz('resultado')
  }

  const refazerQuiz = () => {
    setSessaoQuiz('')
    setTelaQuiz('landing')
  }

  if (telaQuiz === 'quiz') {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gradient-to-b from-rosaCha to-rosaBebe text-gray-800 selection:bg-rosaCha selection:text-white">
        <Quiz aoFinalizar={finalizarQuiz} />
      </div>
    )
  }

  if (telaQuiz === 'resultado') {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gradient-to-b from-rosaCha to-rosaBebe text-gray-800 selection:bg-rosaCha selection:text-white">
        <ResultadoQuiz sessaoId={sessaoQuiz} aoRefazer={refazerQuiz} />
      </div>
    )
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-b from-rosaCha to-rosaBebe text-gray-800 selection:bg-rosaCha selection:text-white">
      <Onboarding aoIniciar={iniciarQuiz} />
    </div>
  )
}
