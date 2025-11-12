FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/root/.local/bin:${PATH}"

WORKDIR /app

# Instalar uv
RUN apt-get update && apt-get install -y curl ca-certificates && rm -rf /var/lib/apt/lists/* \
 && curl -LsSf https://astral.sh/uv/install.sh | sh

# Copiar proyecto
COPY . .

# Instalar deps declaradas en pyproject (crea .venv en /app/.venv)
RUN uv sync

EXPOSE 5173

# Abre el inspector para probar el server 
CMD ["uv", "run", "mcp", "dev", "mcp_server.py"]