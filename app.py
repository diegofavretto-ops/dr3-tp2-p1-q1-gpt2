"""Geração de texto com FastAPI + GPT-2 (Hugging Face)."""
from functools import lru_cache

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, field_validator

app = FastAPI(title="GPT-2 - Gerador de texto", version="1.0")


class Entrada(BaseModel):
    frase: str = Field(min_length=1, max_length=500)

    @field_validator("frase")
    @classmethod
    def verificar_frase(cls, valor: str) -> str:
        if not valor.strip():
            raise ValueError("A frase não pode estar em branco.")
        return valor.strip()


@lru_cache(maxsize=1)
def obter_gerador():
    """Carrega o modelo uma única vez para reutilizá-lo nas requisições."""
    from transformers import pipeline

    return pipeline("text-generation", model="gpt2")


@app.get("/")
def inicio():
    return {"mensagem": "Use POST /gerar para continuar uma frase."}


@app.post("/gerar")
def gerar_texto(entrada: Entrada):
    try:
        gerador = obter_gerador()
        resultado = gerador(
            entrada.frase,
            max_new_tokens=50,
            do_sample=True,
            temperature=0.8,
            return_full_text=False,
            pad_token_id=gerador.tokenizer.eos_token_id,
        )
        continuacao = resultado[0]["generated_text"].strip()
    except Exception as erro:
        # Mostra um erro HTTP legível sem revelar detalhes internos do servidor.
        raise HTTPException(status_code=503, detail="Falha ao executar o GPT-2.") from erro

    return {
        "frase_original": entrada.frase,
        "continuacao": continuacao,
        "texto_completo": entrada.frase + " " + continuacao,
        "modelo": "gpt2",
    }
