import html


def sanitizar(texto: str) -> str:
    if not texto:
        return ""
    texto_limpo = str(texto).strip()
    return html.escape(texto_limpo)
