
import os
import secrets

from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

from main import responder

app = FastAPI(
    title="Claude Live AI",
    version="1.0.0"
)

class Mensagem(BaseModel):
    texto: str

@app.get("/health")
def health():
    return {
        "status": "online",
        "projeto": "Claude Live AI"
    }

@app.post("/chat")
def chat(
    mensagem: Mensagem,
    x_api_token: str = Header(default="")
):
    token = os.getenv("APP_ACCESS_TOKEN", "")

    if not token or not secrets.compare_digest(
        x_api_token, token
    ):
        raise HTTPException(
            status_code=401,
            detail="Acesso não autorizado"
        )

    if not mensagem.texto.strip():
        raise HTTPException(
            status_code=400,
            detail="Mensagem vazia"
        )

    resposta = responder(mensagem.texto)

    return {
        "resposta": resposta
    }
