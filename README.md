# Parte 1 - Questão 1: FastAPI com GPT-2

API HTTP simples que recebe uma frase em JSON e gera uma continuação com o modelo GPT-2 da Hugging Face.

Este projeto faz parte do DR3/TP2 da disciplina **Desenvolvimento de Data-Driven Apps com Python**.

## O que foi usado

- **FastAPI** recebe a requisição HTTP.
- **Pydantic** verifica o JSON.
- **transformers.pipeline** utiliza o modelo GPT-2.

## 1. Preparar o ambiente

É recomendado utilizar **Python 3.11 ou 3.12**. No terminal, entre na pasta do projeto e execute:

**Windows (PowerShell):**

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Se `py -3.11` não estiver disponível, utilize `python -m venv .venv` com uma versão compatível.

**Linux/macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 2. Executar a API

```bash
uvicorn app:app --reload
```

Depois, acesse a documentação automática do FastAPI: **http://127.0.0.1:8000/docs**.

## 2.1. Exemplo de requisição

**POST** `http://127.0.0.1:8000/gerar`

```json
{"frase": "Once upon a time"}
```

O retorno contém `frase_original`, `continuacao`, `texto_completo` e `modelo`. A continuação varia a cada execução. O GPT-2 foi treinado principalmente com textos em inglês; por isso o exemplo está em inglês.


## 3. Testar

```bash
pytest -q
```

Os testes automatizados usam **simulações (mocks)** para não baixar modelos nem gastar créditos. Para testar o modelo real, execute a aplicação e faça uma requisição pela página `/docs`.

## Observações

O código é um exercício didático de geração de texto. O GPT-2 foi treinado principalmente em inglês. Os modelos locais precisam ser baixados antes da primeira tradução ou geração. A API da OpenAI exige uma chave válida e pode gerar cobrança. O tempo de resposta depende da máquina, do tamanho do texto e da conexão.

**Importante:** as saídas reais não foram inventadas nem medidas. Os testes usam simulações e verificam o processamento do JSON e das rotas.
