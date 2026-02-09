"""
Kerykeion Microservice - License: AGPL-3.0
Servicio aislado para cálculos astrológicos usando Kerykeion
Source: https://github.com/KluckZ/kerykeion-service

Version: 5.7.2 (ChartDataFactory + ChartDrawer pipeline, custom theme)
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional
import logging

# Imports de Kerykeion 5.7.2 (AGPL-3.0)
from kerykeion import AstrologicalSubjectFactory, ChartDataFactory, ChartDrawer

from utils import extract_planets, extract_houses, extract_aspects
from aztrosofia_theme import AZTROSOFIA_COLORS, AZTROSOFIA_CELESTIAL_POINTS, AZTROSOFIA_ASPECTS, AZTROSOFIA_CSS

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
    import kerykeion
    return {
        "status": "healthy",
        "service": "kerykeion-calculation-service",
        "version": "1.0.0",
        "kerykeion_version": kerykeion.__version__ if hasattr(kerykeion, '__version__') else "unknown"
    }


@app.get("/debug/attributes")
async def debug_attributes():
    """
    DEBUG: Endpoint temporal para verificar atributos de Kerykeion 5.7.2
    """
    import inspect
    import sys
    import kerykeion as ker
    try:
        kerykeion_info = {
            "module_file": ker.__file__ if hasattr(ker, '__file__') else "unknown",
            "version": ker.__version__ if hasattr(ker, '__version__') else "unknown",
            "python_version": sys.version
        }

        # Crear sujeto de prueba con la nueva API
        subject = AstrologicalSubjectFactory.from_birth_data(
            name="Debug",
            year=1990,
            month=11,
            day=3,
            hour=15,
            minute=30,
            city="Bogota",
            lat=4.6097,
            lng=-74.0817,
            tz_str="America/Bogota",
            online=False
        )

        sig = inspect.signature(AstrologicalSubjectFactory.from_birth_data)
        params = list(sig.parameters.keys())

        fortune_attrs = [attr for attr in dir(subject) if 'fortun' in attr.lower()]
        vertex_attrs = [attr for attr in dir(subject) if 'vertex' in attr.lower()]

        return {
            "kerykeion_info": kerykeion_info,
            "factory_parameters": params,
            "has_active_points_param": "active_points" in params,
            "fortune_related_attrs": fortune_attrs,
            "vertex_related_attrs": vertex_attrs,
            "all_attrs_count": len([a for a in dir(subject) if not a.startswith('_')])
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/calculate")
async def calculate_chart(birth_data: BirthDataRequest):
    """
    Calcula una carta natal completa

    Returns:
        JSON con planetas, casas y aspectos calculados
    """
    try:
        logger.info(f"Calculando carta natal para: {birth_data.name}")

        # Crear objeto astrológico con puntos adicionales activados
        # IMPORTANTE: Usar AstrologicalSubjectFactory.from_birth_data() para active_points
        # (AstrologicalSubject es un wrapper de compatibilidad que NO soporta active_points)
        subject = AstrologicalSubjectFactory.from_birth_data(
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
            online=False,
            active_points=[
                # Planetas principales
                "Sun", "Moon", "Mercury", "Venus", "Mars",
                "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto",
                # Nodos lunares
                "Mean_North_Lunar_Node", "True_North_Lunar_Node",
                # Puntos especiales
                "Chiron", "Mean_Lilith",
                # Arabic Parts
                "Pars_Fortunae",
                # Puntos especiales (Vertex y Anti_Vertex)
                "Vertex", "Anti_Vertex"
            ]
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
    Genera imagen SVG de carta natal con tema Aztrosofia oscuro

    Returns:
        SVG string de la carta natal
    """
    try:
        logger.info(f"Generando SVG para: {request.name}")

        # Crear sujeto astrologico con puntos adicionales (Vertex, Pars Fortunae)
        subject = AstrologicalSubjectFactory.from_birth_data(
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
            online=False,
            active_points=[
                "Sun", "Moon", "Mercury", "Venus", "Mars",
                "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto",
                "True_North_Lunar_Node", "True_South_Lunar_Node",
                "Chiron", "Mean_Lilith",
                "Ascendant", "Medium_Coeli", "Descendant", "Imum_Coeli",
                "Pars_Fortunae", "Vertex",
            ]
        )

        # Crear datos del chart
        chart_data = ChartDataFactory.create_natal_chart_data(subject)

        # Dibujar con tema Aztrosofia custom
        drawer = ChartDrawer(
            chart_data=chart_data,
            theme=None,
            colors_settings=AZTROSOFIA_COLORS,
            celestial_points_settings=AZTROSOFIA_CELESTIAL_POINTS,
            aspects_settings=AZTROSOFIA_ASPECTS,
            chart_language="ES",
        )
        # Inyectar CSS custom para que los glifos SVG tengan color
        # (theme=None deja el <style> vacio, los var() quedan sin definir)
        drawer.color_style_tag = AZTROSOFIA_CSS

        # Filtrar aspectos a angulos (no dibujar lineas a ASC/MC/DSC/IC)
        ANGLES = {"Ascendant", "Medium_Coeli", "Descendant", "Imum_Coeli"}
        drawer.aspects_list = [
            a for a in drawer.aspects_list
            if a["p1_name"] not in ANGLES and a["p2_name"] not in ANGLES
        ]

        # Generar SVG string directamente (sin archivos temporales)
        # remove_css_variables=True inlinea los colores en el SVG
        svg_content = drawer.generate_svg_string(
            minify=True,
            remove_css_variables=True
        )

        # Post-process SVG to make zodiac strip opaque and inner area white.
        # scourString converts inline styles to presentation attributes, so we
        # need to handle both formats:
        #   inline style: fill-opacity:.2;   (before scour)
        #   presentation:  fill-opacity='.2' (after scour + quote replace)
        for val in ['.5', '0.5']:  # zodiac slices (library hardcodes 0.5)
            svg_content = svg_content.replace(f'fill-opacity:{val};', 'fill-opacity:1;')
            svg_content = svg_content.replace(f"fill-opacity='{val}'", "fill-opacity='1'")
        for val in ['.2', '0.2']:  # second circle - planet area
            svg_content = svg_content.replace(f'fill-opacity:{val};', 'fill-opacity:1;')
            svg_content = svg_content.replace(f"fill-opacity='{val}'", "fill-opacity='1'")
        for val in ['.8', '0.8']:  # third circle - aspect area
            svg_content = svg_content.replace(f'fill-opacity:{val};', 'fill-opacity:1;')
            svg_content = svg_content.replace(f"fill-opacity='{val}'", "fill-opacity='1'")

        logger.info(f"SVG generado exitosamente para: {request.name} ({len(svg_content)} bytes)")

        return {
            "success": True,
            "svg": svg_content,
            "metadata": {
                "name": request.name,
                "chart_type": request.chart_type,
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
