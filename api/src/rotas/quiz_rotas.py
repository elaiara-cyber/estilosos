from fastapi import APIRouter, Request, Query
from ..controladores.quiz_controlador import (
    listar_perguntas_controlador,
    listar_estilos_controlador,
    calcular_resultado_controlador,
    salvar_resposta_controlador,
    criar_sessao_controlador
)

router = APIRouter()


@router.get("/quiz/perguntas")
def listar_perguntas_rota():
    return listar_perguntas_controlador()


@router.get("/quiz/estilos")
def listar_estilos_rota():
    return listar_estilos_controlador()


@router.post("/quiz/sessao")
def criar_sessao_rota():
    return criar_sessao_controlador()


@router.post("/quiz/resposta")
async def salvar_resposta_rota(request: Request):
    try:
        payload = await request.json()
    except Exception:
        payload = {}
    return salvar_resposta_controlador(payload)


@router.get("/quiz/resultado")
def calcular_resultado_rota(sessao_id: str = Query(..., min_length=5)):
    return calcular_resultado_controlador(sessao_id)
