# 🔮 Kerykeion Service

**Microservicio aislado para cálculos astrológicos**

[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL%203.0-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green.svg)](https://fastapi.tiangolo.com/)

## 📋 Descripción

Este microservicio proporciona cálculos astrológicos utilizando [Kerykeion](https://github.com/g-battaglia/kerykeion), una biblioteca Python de código abierto para astrología.

Este servicio está licenciado bajo AGPL-3.0 debido al uso de Kerykeion.

## 🏗️ Arquitectura

Microservicio independiente que proporciona cálculos astrológicos vía API REST.

**Características:**
- ✅ API REST con FastAPI
- ✅ Cálculos astrológicos precisos con Kerykeion
- ✅ Generación de imágenes SVG de cartas natales
- ✅ Documentación interactiva automática
- ✅ Fácil de integrar vía HTTP/JSON

## 🚀 Endpoints

### `GET /`
Información del servicio y link al código fuente (cumplimiento AGPL)

### `GET /health`
Health check del servicio

### `POST /calculate`
Calcula una carta natal completa

**Request:**
```json
{
  "name": "John Doe",
  "year": 1990,
  "month": 5,
  "day": 15,
  "hour": 14,
  "minute": 30,
  "latitude": 40.7128,
  "longitude": -74.0060,
  "city": "New York",
  "timezone": "America/New_York"
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "planets": [...],
    "houses": [...],
    "aspects": [...]
  },
  "metadata": {...}
}
```

### `POST /generate-svg`
Genera imagen SVG de la carta natal

**Request:** (igual que `/calculate`)

**Response:**
```json
{
  "success": true,
  "svg": "<svg>...</svg>",
  "metadata": {...}
}
```

## 🛠️ Instalación Local

### Requisitos
- Python 3.12+
- Docker (opcional)

### Con Docker (Recomendado)

```bash
# Construir imagen
docker build -t kerykeion-service .

# Ejecutar contenedor
docker run -p 8000:8000 kerykeion-service
```

### Sin Docker

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar servidor
uvicorn app:app --host 0.0.0.0 --port 8000
```

El servicio estará disponible en: `http://localhost:8000`

## 📚 Documentación API

Una vez ejecutando, visita:
- **Documentación interactiva:** `http://localhost:8000/docs`
- **OpenAPI Schema:** `http://localhost:8000/openapi.json`

## 🧪 Testing

```bash
# Ejemplo con curl
curl -X POST http://localhost:8000/calculate \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test",
    "year": 1990,
    "month": 1,
    "day": 1,
    "hour": 12,
    "minute": 0,
    "latitude": 0,
    "longitude": 0,
    "city": "Test City",
    "timezone": "UTC"
  }'
```

## 📄 Licencia

Este proyecto está licenciado bajo **AGPL-3.0** - ver el archivo [LICENSE](LICENSE) para detalles.

Este servicio utiliza Kerykeion, que está bajo licencia AGPL-3.0, por lo tanto este microservicio también debe ser AGPL-3.0 y estar disponible públicamente.

## 🙏 Atribución

Este servicio utiliza [Kerykeion](https://github.com/g-battaglia/kerykeion), creado por Giacomo Battaglia.

Kerykeion está licenciado bajo AGPL-3.0, por lo que este servicio derivado también debe estar bajo AGPL-3.0 y disponible públicamente.

**Gracias a Giacomo Battaglia y todos los contribuidores de Kerykeion por su excelente trabajo.**

## 🔗 Enlaces

- **Repositorio:** https://github.com/KluckZ/kerykeion-service
- **Kerykeion Original:** https://github.com/g-battaglia/kerykeion
- **Licencia AGPL-3.0:** https://www.gnu.org/licenses/agpl-3.0.txt

## 📞 Soporte

Para issues o preguntas, abre un issue en este repositorio.

---

**Powered by Kerykeion**
