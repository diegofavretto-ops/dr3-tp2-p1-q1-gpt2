from fastapi.testclient import TestClient

import app as modulo

cliente = TestClient(modulo.app)


class GeradorFalso:
    tokenizer = type("Tokenizer", (), {"eos_token_id": 50256})()

    def __call__(self, texto, **kwargs):
        return [{"generated_text": "and the story continued."}]


def test_gera_continuacao(monkeypatch):
    monkeypatch.setattr(modulo, "obter_gerador", lambda: GeradorFalso())
    resposta = cliente.post("/gerar", json={"frase": "Once upon a time"})
    assert resposta.status_code == 200
    assert resposta.json()["continuacao"] == "and the story continued."
    assert resposta.json()["modelo"] == "gpt2"


def test_frase_vazia_e_rejeitada():
    resposta = cliente.post("/gerar", json={"frase": "  "})
    assert resposta.status_code == 422
