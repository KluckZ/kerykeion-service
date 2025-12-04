# Kerykeion Service - AGPL-3.0
# Microservicio aislado para cálculos astrológicos
FROM python:3.12-slim

WORKDIR /app

# Instalar dependencias del sistema necesarias para compilar pyswisseph
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependencias de Python
COPY requirements.txt .
# Forzar instalación de Kerykeion 5.3.2 primero
RUN pip install --no-cache-dir --upgrade kerykeion==5.3.2
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY . .

# Exponer puerto (Railway asigna dinámicamente)
EXPOSE 8000

# Variable de entorno para puerto (Railway la sobrescribe)
ENV PORT=8000

# Comando de inicio (usa shell para expandir variable PORT)
CMD ["/bin/sh", "-c", "uvicorn app:app --host 0.0.0.0 --port $PORT"]
