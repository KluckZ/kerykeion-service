"""
Kerykeion Microservice - License: AGPL-3.0
Servicio aislado para cálculos astrológicos usando Kerykeion
Source: https://github.com/KluckZ/kerykeion-service
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional
import logging

# Imports de Kerykeion (AGPL-3.0)
from kerykeion import AstrologicalSubject, KerykeionChartSVG

from utils import extract_planets, extract_houses, extract_aspects

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Kerykeion Calculation Service",
    description="Microservicio aislado para cálculos astrológicos - AGPL-3.0",
    version="1.0.0"
)

# CORS (permitir requests desde cualquier origen)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class BirthDataRequest(BaseModel):
    """Request model para cálculo de carta natal"""
    name: str = Field(..., description="Nombre de la persona")
    year: int = Field(..., ge=1900, le=2100, description="Año de nacimiento")
    month: int = Field(..., ge=1, le=12, description="Mes de nacimiento")
    day: int = Field(..., ge=1, le=31, description="Día de nacimiento")
    hour: int = Field(..., ge=0, le=23, description="Hora de nacimiento")
    minute: int = Field(..., ge=0, le=59, description="Minuto de nacimiento")
    latitude: float = Field(..., ge=-90, le=90, description="Latitud")
    longitude: float = Field(..., ge=-180, le=180, description="Longitud")
    city: str = Field(..., description="Ciudad de nacimiento")
    timezone: str = Field(..., description="Timezone (ej: America/Bogota)")


class SVGGenerationRequest(BaseModel):
    """Request model para generación de imagen SVG"""
    name: str
    year: int
    month: int
    day: int
    hour: int
    minute: int
    latitude: float
    longitude: float
    city: str
    timezone: str
    chart_type: Optional[str] = "Natal"


@app.get("/")
async def root():
    """
    Endpoint raíz con información del servicio
    IMPORTANTE: Incluye link al código fuente (cumplimiento AGPL-3.0)
    """
    return {
        "service": "Kerykeion Calculation Service",
        "version": "1.0.0",
        "license": "AGPL-3.0",
        "description": "Microservicio aislado para cálculos astrológicos",
        "source_code": "https://github.com/KluckZ/kerykeion-service",
        "attribution": "Powered by Kerykeion - https://github.com/g-battaglia/kerykeion",
        "endpoints": {
            "/health": "Health check",
            "/calculate": "POST - Calcular carta natal",
            "/generate-svg": "POST - Generar imagen SVG de carta"
        }
    }


@app.get("/health")
async def health():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "kerykeion-calculation-service",
        "version": "1.0.0"
    }


@app.post("/calculate")
async def calculate_chart(birth_data: BirthDataRequest):
    """
    Calcula una carta natal completa

    Returns:
        JSON con planetas, casas y aspectos calculados
    """
    try:
        logger.info(f"Calculando carta natal para: {birth_data.name}")

        # Crear objeto astrológico (ÚNICA llamada a librería AGPL)
        subject = AstrologicalSubject(
            name=birth_data.name,
            year=birth_data.year,
            month=birth_data.month,
            day=birth_data.day,
            hour=birth_data.hour,
            minute=birth_data.minute,
            city=birth_data.city,
            lng=birth_data.longitude,
            lat=birth_data.latitude,
            tz_str=birth_data.timezone,
            online=False
        )

        # Extraer datos calculados a formato JSON limpio
        planets = extract_planets(subject)
        houses = extract_houses(subject)
        aspects = extract_aspects(subject)

        logger.info(f"Carta calculada exitosamente: {len(planets)} planetas, {len(houses)} casas, {len(aspects)} aspectos")

        return {
            "success": True,
            "data": {
                "planets": planets,
                "houses": houses,
                "aspects": aspects
            },
            "metadata": {
                "name": birth_data.name,
                "birth_date": f"{birth_data.year}-{birth_data.month:02d}-{birth_data.day:02d}",
                "birth_time": f"{birth_data.hour:02d}:{birth_data.minute:02d}",
                "location": birth_data.city,
                "timezone": birth_data.timezone
            }
        }

    except Exception as e:
        logger.error(f"Error calculando carta: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail={
                "error": "Error calculando carta natal",
                "message": str(e)
            }
        )


@app.post("/generate-svg")
async def generate_svg(request: SVGGenerationRequest):
    """
    Genera imagen SVG de carta natal

    Returns:
        SVG string de la carta natal
    """
    import tempfile
    from pathlib import Path

    try:
        logger.info(f"Generando SVG para: {request.name}")

        # Crear directorio temporal
        with tempfile.TemporaryDirectory() as temp_dir:
            output_dir = Path(temp_dir)

            # Crear objeto astrológico
            subject = AstrologicalSubject(
                name=request.name,
                year=request.year,
                month=request.month,
                day=request.day,
                hour=request.hour,
                minute=request.minute,
                city=request.city,
                lng=request.longitude,
                lat=request.latitude,
                tz_str=request.timezone,
                online=False
            )

            # Generar SVG (guarda en archivo)
            chart = KerykeionChartSVG(subject, chart_type=request.chart_type, new_output_directory=str(output_dir))
            chart.makeSVG()

            # Buscar archivo SVG generado
            svg_files = list(output_dir.glob("*.svg"))

            if not svg_files:
                raise Exception("No se generó ningún archivo SVG")

            # Leer contenido del SVG
            svg_file_path = svg_files[0]
            with open(svg_file_path, 'r', encoding='utf-8') as f:
                svg_content = f.read()

            logger.info(f"SVG generado exitosamente para: {request.name} ({len(svg_content)} bytes)")

            return {
                "success": True,
                "svg": svg_content,
                "metadata": {
                    "name": request.name,
                    "chart_type": request.chart_type,
                    "filename": svg_file_path.name
                }
            }

    except Exception as e:
        logger.error(f"Error generando SVG: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail={
                "error": "Error generando imagen SVG",
                "message": str(e)
            }
        )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
