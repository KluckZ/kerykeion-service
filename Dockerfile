# Kerykeion Service - AGPL-3.0
# Microservicio aislado para cálculos astrológicos
FROM python:3.12-slim

WORKDIR /app

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY . .

# Exponer puerto
EXPOSE 8000

# Comando de inicio
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
