import os
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv

caminho_env = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=caminho_env)

from .rotas.quiz_rotas import router as quiz_router
from .middlewares.seguranca import RateLimitMiddleware, SecurityHeadersMiddleware

app = FastAPI(title="API Estilosos - Quiz de Estilo")

origem_permitida = os.getenv("ORIGEM_PERMITIDA", "*")
origens = [o.strip() for o in origem_permitida.split(",") if o.strip()] or ["*"]

try:
    limite_requisicoes = max(1, int(os.getenv("RATE_LIMIT_PER_MINUTE", "60")))
except ValueError:
    limite_requisicoes = 60

app.add_middleware(SecurityHeadersMiddleware)
app.add_middleware(RateLimitMiddleware, limite_por_minuto=limite_requisicoes)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origens,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(quiz_router, prefix="/api")

@app.get("/api/health")
def health_check():
    return {"sucesso": True, "mensagem": "API funcionando!"}

caminho_dist = Path(__file__).resolve().parent.parent.parent / 'frontend' / 'dist'
caminho_frontend = Path(__file__).resolve().parent.parent.parent / 'frontend'
pasta_estatica = caminho_dist if caminho_dist.exists() else caminho_frontend

if pasta_estatica.exists():
    app.mount("/static", StaticFiles(directory=str(pasta_estatica)), name="static")

@app.get("/{full_path:path}")
async def servir_frontend_ou_fallback(request: Request, full_path: str):
    if full_path.startswith("api"):
        return JSONResponse(
            status_code=404,
            content={'sucesso': False, 'mensagem': 'Rota de API não encontrada.'}
        )

    caminho_arquivo = pasta_estatica / full_path
    if full_path and caminho_arquivo.is_file():
        return FileResponse(caminho_arquivo)

    index_path = pasta_estatica / "index.html"
    if index_path.is_file():
        return FileResponse(index_path)

    return {"erro": "Página não encontrada"}
