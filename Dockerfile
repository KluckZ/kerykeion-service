# Kerykeion Service - AGPL-3.0
# Microservicio aislado para cálculos astrológicos
FROM python:3.12-slim

WORKDIR /app

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY . .

# Exponer puerto (Railway asigna dinámicamente)
EXPOSE 8000

# Variable de entorno para puerto (Railway la sobrescribe)
ENV PORT=8000

# Comando de inicio (usa variable PORT)
CMD uvicorn app:app --host 0.0.0.0 --port $PORT
