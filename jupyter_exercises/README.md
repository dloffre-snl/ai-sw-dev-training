# Jupyter Exercises

## Prerequisites

- Apple Silicon Mac (uses `mlx-lm`)
- [LM Studio](https://lmstudio.ai/) with the server enabled on port 1234
- Models loaded in LM Studio (see `config.toml`):
  - `openai/gpt-oss-20b`
  - `openai/gpt-oss-120b`
  - `meta/llama-3.3-70b`
  - `text-embedding-embeddinggemma-300m-qat`

## Setup

```bash
cd jupyter_exercises
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt jupyterlab
```

## Run

```bash
jupyter lab
```

Open notebooks in order. Restart the kernel between notebooks.

Notebook 03 also requires two background processes in separate terminals:

```bash
python mcp_server.py   # port 8000
python mcp_proxy.py    # port 8080
```
