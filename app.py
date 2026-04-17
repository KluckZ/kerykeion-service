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
from aztrosofia_theme import (
    AZTROSOFIA_COLORS, AZTROSOFIA_CELESTIAL_POINTS, AZTROSOFIA_ASPECTS, AZTROSOFIA_CSS,
    build_theme_from_config,
)

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
    colors: Optional[dict] = None


class TransitPositionsRequest(BaseModel):
    """Request model para posiciones de tránsitos en una fecha dada"""
    year: int = Field(..., ge=1900, le=2100)
    month: int = Field(..., ge=1, le=12)
    day: int = Field(..., ge=1, le=31)
    hour: int = Field(12, ge=0, le=23)
    minute: int = Field(0, ge=0, le=59)
    timezone: str = Field("UTC")
    latitude: Optional[float] = Field(None, ge=-90, le=90)
    longitude: Optional[float] = Field(None, ge=-180, le=180)
    city: Optional[str] = Field(None)


class LunarEventsRequest(BaseModel):
    """Request model para detección de lunas nuevas y llenas en un rango"""
    start_date: str  # "YYYY-MM-DD"
    end_date: str    # "YYYY-MM-DD" — máx 6 meses


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
            "/health": "GET - Health check",
            "/calculate": "POST - Calcular carta natal completa",
            "/generate-svg": "POST - Generar imagen SVG de carta",
            "/transit-positions": "POST - Posiciones planetarias para cualquier fecha",
            "/lunar-events": "POST - Lunas nuevas y llenas en rango (máx 6 meses)"
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

        # Fix Fortune: kerykeion 5.7.2 has inverted day/night formula.
        # Correct rule: Sun in houses 7-12 = above horizon = day birth.
        # Day  → Fortune = ASC + Moon - Sun
        # Night → Fortune = ASC + Sun  - Moon
        _HOUSE_NUMBERS = {
            "First_House": 1, "Second_House": 2, "Third_House": 3, "Fourth_House": 4,
            "Fifth_House": 5, "Sixth_House": 6, "Seventh_House": 7, "Eighth_House": 8,
            "Ninth_House": 9, "Tenth_House": 10, "Eleventh_House": 11, "Twelfth_House": 12
        }
        _ZODIAC_SIGNS = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
                         "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
        if subject.pars_fortunae:
            sun_house_num = _HOUSE_NUMBERS.get(getattr(subject.sun, "house", ""), 0)
            is_day = 7 <= sun_house_num <= 12
            asc_deg = subject.first_house.abs_pos
            sun_deg = subject.sun.abs_pos
            moon_deg = subject.moon.abs_pos
            if is_day:
                fortune_deg = (asc_deg + moon_deg - sun_deg) % 360
            else:
                fortune_deg = (asc_deg + sun_deg - moon_deg) % 360
            pf = subject.pars_fortunae
            pf.abs_pos = fortune_deg
            pf.sign_num = int(fortune_deg / 30)
            pf.sign = _ZODIAC_SIGNS[pf.sign_num]
            pf.position = fortune_deg % 30
            logger.info(
                f"Fortune corrected: {'day' if is_day else 'night'} birth "
                f"(Sun house {sun_house_num}) → {pf.sign} {pf.position:.2f}°"
            )

        # Crear datos del chart
        chart_data = ChartDataFactory.create_natal_chart_data(subject)

        # Build theme: use admin colors if provided, otherwise hardcoded defaults
        if request.colors:
            logger.info("Using custom colors from request")
            colors_s, celestial_s, aspects_s, css_s = build_theme_from_config(request.colors)
        else:
            colors_s = AZTROSOFIA_COLORS
            celestial_s = AZTROSOFIA_CELESTIAL_POINTS
            aspects_s = AZTROSOFIA_ASPECTS
            css_s = AZTROSOFIA_CSS

        # Dibujar con tema Aztrosofia custom
        drawer = ChartDrawer(
            chart_data=chart_data,
            theme=None,
            colors_settings=colors_s,
            celestial_points_settings=celestial_s,
            aspects_settings=aspects_s,
            chart_language="ES",
        )
        # Inyectar CSS custom para que los glifos SVG tengan color
        # (theme=None deja el <style> vacio, los var() quedan sin definir)
        drawer.color_style_tag = css_s

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


def _refine_lunar_event(day1, day2, target_angle, angle_fn):
    """Bisección para precisión de ~1.5 minutos en la hora del evento."""
    from datetime import timedelta
    low, high = day1, day2
    for _ in range(10):
        mid = low + (high - low) / 2
        angle = angle_fn(mid)
        diff = (angle - target_angle + 180.0) % 360.0 - 180.0
        if diff < 0:
            low = mid
        else:
            high = mid
    return low + (high - low) / 2


def _get_moon_sign_at(dt):
    """Signo zodiacal de la Luna en un momento dado."""
    import swisseph as swe
    SIGNS = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
             "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
    jd = swe.julday(dt.year, dt.month, dt.day, dt.hour + dt.minute / 60.0)
    moon_pos = swe.calc_ut(jd, swe.MOON)[0][0]
    return SIGNS[int(moon_pos / 30)]


@app.post("/transit-positions")
async def transit_positions(request: TransitPositionsRequest):
    """
    Posiciones de 12 cuerpos celestes para cualquier fecha.
    Las posiciones planetarias son globales (lat/lng solo afectan la Luna con alta precisión).
    """
    try:
        lat = request.latitude or 0.0
        lng = request.longitude or 0.0
        city = request.city or "Greenwich"

        subject = AstrologicalSubjectFactory.from_birth_data(
            name="Transit",
            year=request.year,
            month=request.month,
            day=request.day,
            hour=request.hour,
            minute=request.minute,
            city=city,
            lat=lat,
            lng=lng,
            tz_str=request.timezone,
            online=False,
            active_points=[
                "Sun", "Moon", "Mercury", "Venus", "Mars",
                "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto",
                "True_North_Lunar_Node", "Chiron", "Mean_Lilith"
            ]
        )

        planets = extract_planets(subject)
        planets = [p for p in planets if p["name"] not in ("asc", "mc")]

        return {
            "success": True,
            "data": {
                "planets": planets,
                "date": f"{request.year}-{request.month:02d}-{request.day:02d}",
                "time": f"{request.hour:02d}:{request.minute:02d}",
                "timezone": request.timezone
            }
        }

    except Exception as e:
        logger.error(f"Error calculando posiciones de tránsito: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail={
                "error": "Error calculando posiciones de tránsito",
                "message": str(e)
            }
        )


@app.post("/lunar-events")
async def lunar_events(request: LunarEventsRequest):
    """
    Detecta lunas nuevas y llenas en un rango de fechas.
    Algoritmo optimizado: salto 13 días tras cada evento (ciclo sinódico ~29.53 días).
    Máximo 6 meses por petición.
    """
    try:
      return await _lunar_events_impl(request)
    except Exception as e:
      import traceback
      logger.error(f"[lunar-events] Unhandled error: {traceback.format_exc()}")
      raise HTTPException(status_code=500, detail={"error": str(e), "type": type(e).__name__})


async def _lunar_events_impl(request: LunarEventsRequest):
    import swisseph as swe
    from datetime import datetime, timedelta

    start = datetime.strptime(request.start_date, "%Y-%m-%d")
    end = datetime.strptime(request.end_date, "%Y-%m-%d")

    if (end - start).days > 185:
        raise HTTPException(status_code=400, detail="Range cannot exceed 6 months")

    def sun_moon_angle(dt: datetime) -> float:
        """Ángulo Luna−Sol en [0°, 360°). 0°=Nueva, 180°=Llena."""
        jd = swe.julday(dt.year, dt.month, dt.day, dt.hour + dt.minute / 60.0)
        sun_pos = swe.calc_ut(jd, swe.SUN)[0][0]
        moon_pos = swe.calc_ut(jd, swe.MOON)[0][0]
        return (moon_pos - sun_pos) % 360.0

    events = []
    JUMP = timedelta(days=13)  # tras cada evento, el siguiente está en ~14.77 días

    current = start
    prev_angle = sun_moon_angle(current)

    while current <= end:
        next_day = current + timedelta(days=1)
        if next_day > end:
            break

        curr_angle = sun_moon_angle(next_day)
        event_found = None

        # Luna Nueva: ángulo cruza 0° (wrap de ~360° a ~0°-30°)
        # Robusto: detecta aunque el muestreo diario no caiga exactamente en el cruce
        if prev_angle > curr_angle + 300:
            event_found = ("luna_nueva", 0.0)

        # Luna Llena: ángulo cruza 180° en sentido ascendente
        elif prev_angle < 180.0 <= curr_angle:
            event_found = ("luna_llena", 180.0)

        if event_found:
            event_type, target = event_found
            event_dt = _refine_lunar_event(current, next_day, target, sun_moon_angle)
            sign_info = _get_moon_sign_at(event_dt)
            label = "Luna Nueva" if event_type == "luna_nueva" else "Luna Llena"
            events.append({
                "type": event_type,
                "date": event_dt.strftime("%Y-%m-%d"),
                "time": event_dt.strftime("%H:%M"),
                "datetime_utc": event_dt.isoformat(),
                "moon_sign": sign_info,
                "name": f"{label} en {sign_info}"
            })
            # Saltar al vecindario del próximo evento
            current = event_dt + JUMP
            prev_angle = sun_moon_angle(current)
        else:
            prev_angle = curr_angle
            current = next_day

    events.sort(key=lambda e: e["datetime_utc"])

    return {
        "success": True,
        "data": {
            "events": events,
            "total": len(events),
            "range": {"start": request.start_date, "end": request.end_date}
        }
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
