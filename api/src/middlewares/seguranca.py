import time
from collections import defaultdict

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    """Item 18 — headers de segurança sem dependências extras.

    Não inclui Content-Security-Policy restritivo de propósito: o frontend
    usa `style={{...}}` inline e Google Fonts, que um CSP rígido quebraria.
    """

    async def dispatch(self, request, call_next):
        resposta = await call_next(request)
        resposta.headers["X-Content-Type-Options"] = "nosniff"
        resposta.headers["X-Frame-Options"] = "DENY"
        resposta.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        resposta.headers["Permissions-Policy"] = (
            "camera=(), microphone=(), geolocation=()"
        )
        return resposta


class RateLimitMiddleware(BaseHTTPMiddleware):
    """Item 11 — rate limit simples em memória (anti-spam/bots no quiz).

    Janela deslizante de 60s por IP, só em rotas /api. Sem dependências
    externas. Retorna 429 com o padrão {sucesso, mensagem} da API.
    Limite via env RATE_LIMIT_PER_MINUTE (padrão 60 — folga p/ o fluxo
    normal: 1 sessão + 1 perguntas + 20 respostas + 1 resultado ≈ 23 req).
    """

    def __init__(self, app, limite_por_minuto=60):
        super().__init__(app)
        self.limite = limite_por_minuto
        self.requisicoes = defaultdict(list)

    async def dispatch(self, request, call_next):
        if request.url.path.startswith("/api"):
            ip = request.client.host if request.client else "desconhecido"
            agora = time.monotonic()
            janela = [t for t in self.requisicoes[ip] if agora - t < 60]
            if len(janela) >= self.limite:
                return JSONResponse(
                    status_code=429,
                    content={
                        "sucesso": False,
                        "mensagem": "Muitas requisições. Tente novamente em instantes.",
                    },
                )
            janela.append(agora)
            self.requisicoes[ip] = janela
            # Poda simples para o dicionário não crescer sem limite
            if len(self.requisicoes) > 1000:
                self.requisicoes = defaultdict(
                    list,
                    {k: v for k, v in self.requisicoes.items() if v and agora - v[-1] < 60},
                )
        return await call_next(request)
