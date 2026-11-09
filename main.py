
import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

def responder(mensagem):
    chave = os.getenv("ANTHROPIC_API_KEY")

    if not chave:
        return "Configure a chave da API do Claude."

    cliente = Anthropic(api_key=chave)

    resposta = cliente.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=300,
        system=(
            "Você é um apresentador virtual de lives "
            "do TikTok. Fale em português brasileiro, "
            "seja divertido, educado e espontâneo. "
            "Nunca invente preços ou características "
            "de produtos. Deixe claro que é uma IA."
        ),
        messages=[
            {"role": "user", "content": mensagem}
        ]
    )

    return resposta.content[0].text


if __name__ == "__main__":
    print(responder("Olá! Apresente nossa live."))
