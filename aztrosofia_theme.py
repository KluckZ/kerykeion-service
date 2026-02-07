"""
Aztrosofia Theme for Kerykeion 5.7.2
Tema oscuro cosmico - colores custom para carta natal SVG

Usa theme=None + colors_settings/celestial_points_settings/aspects_settings
para override completo sin CSS variables.
"""

# ═══════════════════════════════════════════════════════════
# COLORS SETTINGS - Override de DEFAULT_CHART_COLORS
# Keys: paper_0, paper_1, zodiac_bg_0-11, zodiac_icon_0-11,
#        zodiac_radix_ring_0-2, houses_radix_line, lunar_phase_0-1
# ═══════════════════════════════════════════════════════════

AZTROSOFIA_COLORS = {
    # paper_0 = color de texto/fill principal, paper_1 = fondo del SVG
    "paper_0": "#f1f5f9",               # Blanco suave - Texto principal
    "paper_1": "#0a0e27",               # Azul noche profundo - Fondo SVG

    # Signos zodiacales - fondo (alternando 2 tonos oscuros)
    "zodiac_bg_0": "#141827",           # Aries
    "zodiac_bg_1": "#1a1f3a",           # Tauro
    "zodiac_bg_2": "#141827",           # Geminis
    "zodiac_bg_3": "#1a1f3a",           # Cancer
    "zodiac_bg_4": "#141827",           # Leo
    "zodiac_bg_5": "#1a1f3a",           # Virgo
    "zodiac_bg_6": "#141827",           # Libra
    "zodiac_bg_7": "#1a1f3a",           # Escorpio
    "zodiac_bg_8": "#141827",           # Sagitario
    "zodiac_bg_9": "#1a1f3a",           # Capricornio
    "zodiac_bg_10": "#141827",          # Acuario
    "zodiac_bg_11": "#1a1f3a",          # Piscis

    # Signos zodiacales - iconos
    "zodiac_icon_0": "#ef4444",         # Aries - Rojo fuego
    "zodiac_icon_1": "#10b981",         # Tauro - Verde tierra
    "zodiac_icon_2": "#fbbf24",         # Geminis - Dorado aire
    "zodiac_icon_3": "#60a5fa",         # Cancer - Azul agua
    "zodiac_icon_4": "#ef4444",         # Leo - Rojo fuego
    "zodiac_icon_5": "#10b981",         # Virgo - Verde tierra
    "zodiac_icon_6": "#fbbf24",         # Libra - Dorado aire
    "zodiac_icon_7": "#60a5fa",         # Escorpio - Azul agua
    "zodiac_icon_8": "#ef4444",         # Sagitario - Rojo fuego
    "zodiac_icon_9": "#10b981",         # Capricornio - Verde tierra
    "zodiac_icon_10": "#fbbf24",        # Acuario - Dorado aire
    "zodiac_icon_11": "#60a5fa",        # Piscis - Azul agua

    # Anillos
    "zodiac_radix_ring_0": "#1e293b",   # Anillo exterior
    "zodiac_radix_ring_1": "#334155",   # Anillo medio
    "zodiac_radix_ring_2": "#1e293b",   # Anillo interior

    # Anillos de transito (si aplica)
    "zodiac_transit_ring_0": "#4c1d95",
    "zodiac_transit_ring_1": "#3b0764",
    "zodiac_transit_ring_2": "#4c1d95",

    # Lineas de casas
    "houses_radix_line": "#475569",

    # Fase lunar
    "lunar_phase_0": "#e0e7ff",
    "lunar_phase_1": "#141827",

    # Primer punto de Aries
    "first_point_of_aries": "#8b5cf6",
}


# ═══════════════════════════════════════════════════════════
# CELESTIAL POINTS SETTINGS
# Cada item: {id, name, color, element_points, label}
# ═══════════════════════════════════════════════════════════

AZTROSOFIA_CELESTIAL_POINTS = [
    # Planetas principales
    {"id": "Sun", "name": "Sun", "color": "#fbbf24", "element_points": 40, "label": "Su"},
    {"id": "Moon", "name": "Moon", "color": "#e0e7ff", "element_points": 40, "label": "Mo"},
    {"id": "Mercury", "name": "Mercury", "color": "#22d3ee", "element_points": 15, "label": "Me"},
    {"id": "Venus", "name": "Venus", "color": "#fb7185", "element_points": 15, "label": "Ve"},
    {"id": "Mars", "name": "Mars", "color": "#ef4444", "element_points": 15, "label": "Ma"},
    {"id": "Jupiter", "name": "Jupiter", "color": "#f97316", "element_points": 10, "label": "Ju"},
    {"id": "Saturn", "name": "Saturn", "color": "#a8855c", "element_points": 10, "label": "Sa"},
    {"id": "Uranus", "name": "Uranus", "color": "#06b6d4", "element_points": 5, "label": "Ur"},
    {"id": "Neptune", "name": "Neptune", "color": "#6366f1", "element_points": 5, "label": "Ne"},
    {"id": "Pluto", "name": "Pluto", "color": "#7c3aed", "element_points": 5, "label": "Pl"},

    # Nodos lunares
    {"id": "Mean_North_Lunar_Node", "name": "Mean North Lunar Node", "color": "#a78bfa", "element_points": 0, "label": "NN"},
    {"id": "True_North_Lunar_Node", "name": "True North Lunar Node", "color": "#a78bfa", "element_points": 0, "label": "TN"},
    {"id": "Mean_South_Lunar_Node", "name": "Mean South Lunar Node", "color": "#a78bfa", "element_points": 0, "label": "SN"},
    {"id": "True_South_Lunar_Node", "name": "True South Lunar Node", "color": "#a78bfa", "element_points": 0, "label": "TS"},

    # Puntos especiales
    {"id": "Chiron", "name": "Chiron", "color": "#f97316", "element_points": 0, "label": "Ch"},
    {"id": "Mean_Lilith", "name": "Mean Lilith", "color": "#be123c", "element_points": 0, "label": "Li"},
    {"id": "Pars_Fortunae", "name": "Pars Fortunae", "color": "#fbbf24", "element_points": 0, "label": "PF"},
    {"id": "Vertex", "name": "Vertex", "color": "#8b5cf6", "element_points": 0, "label": "Vx"},
    {"id": "Anti_Vertex", "name": "Anti Vertex", "color": "#8b5cf6", "element_points": 0, "label": "AV"},

    # Angulos
    {"id": "Ascendant", "name": "Ascendant", "color": "#f1f5f9", "element_points": 0, "label": "As"},
    {"id": "Descendant", "name": "Descendant", "color": "#cbd5e1", "element_points": 0, "label": "Ds"},
    {"id": "Medium_Coeli", "name": "Medium Coeli", "color": "#f1f5f9", "element_points": 0, "label": "MC"},
    {"id": "Imum_Coeli", "name": "Imum Coeli", "color": "#cbd5e1", "element_points": 0, "label": "IC"},

    # Planetas hipoteticos / extras (Kerykeion incluye ~42 por defecto)
    {"id": "True_Lilith", "name": "True Lilith", "color": "#be123c", "element_points": 0, "label": "TL"},
    {"id": "Interpolated_Lilith", "name": "Interpolated Lilith", "color": "#be123c", "element_points": 0, "label": "IL"},
    {"id": "Ceres", "name": "Ceres", "color": "#10b981", "element_points": 0, "label": "Ce"},
    {"id": "Pallas", "name": "Pallas", "color": "#22d3ee", "element_points": 0, "label": "Pa"},
    {"id": "Juno", "name": "Juno", "color": "#fb7185", "element_points": 0, "label": "Jn"},
    {"id": "Vesta", "name": "Vesta", "color": "#ef4444", "element_points": 0, "label": "Vs"},
    {"id": "Eris", "name": "Eris", "color": "#7c3aed", "element_points": 0, "label": "Er"},
    {"id": "Sedna", "name": "Sedna", "color": "#f97316", "element_points": 0, "label": "Se"},
    {"id": "Makemake", "name": "Makemake", "color": "#10b981", "element_points": 0, "label": "Mk"},
    {"id": "Haumea", "name": "Haumea", "color": "#60a5fa", "element_points": 0, "label": "Ha"},
    {"id": "Quaoar", "name": "Quaoar", "color": "#a78bfa", "element_points": 0, "label": "Qu"},
    {"id": "Gonggong", "name": "Gonggong", "color": "#ef4444", "element_points": 0, "label": "Go"},
    {"id": "Orcus", "name": "Orcus", "color": "#6366f1", "element_points": 0, "label": "Or"},
    {"id": "Varuna", "name": "Varuna", "color": "#06b6d4", "element_points": 0, "label": "Va"},
    {"id": "Ixion", "name": "Ixion", "color": "#ef4444", "element_points": 0, "label": "Ix"},
    {"id": "Nessus", "name": "Nessus", "color": "#be123c", "element_points": 0, "label": "Ne"},
    {"id": "Pholus", "name": "Pholus", "color": "#f97316", "element_points": 0, "label": "Ph"},
    {"id": "Hygeia", "name": "Hygeia", "color": "#10b981", "element_points": 0, "label": "Hy"},
    {"id": "Astraea", "name": "Astraea", "color": "#fbbf24", "element_points": 0, "label": "At"},
]


# ═══════════════════════════════════════════════════════════
# ASPECTS SETTINGS
# Cada item: {degree, name, classification, color}
# ═══════════════════════════════════════════════════════════

AZTROSOFIA_ASPECTS = [
    # Aspectos mayores
    {"degree": 0, "name": "Conjunction", "classification": "major", "color": "#60a5fa"},
    {"degree": 60, "name": "Sextile", "classification": "major", "color": "#10b981"},
    {"degree": 90, "name": "Square", "classification": "major", "color": "#ef4444"},
    {"degree": 120, "name": "Trine", "classification": "major", "color": "#10b981"},
    {"degree": 180, "name": "Opposition", "classification": "major", "color": "#f97316"},

    # Aspectos menores
    {"degree": 30, "name": "Semi-Sextile", "classification": "minor", "color": "#a78bfa"},
    {"degree": 45, "name": "Semi-Square", "classification": "minor", "color": "#fbbf24"},
    {"degree": 72, "name": "Quintile", "classification": "minor", "color": "#34d399"},
    {"degree": 135, "name": "Sesquiquadrate", "classification": "minor", "color": "#fb923c"},
    {"degree": 144, "name": "Bi-Quintile", "classification": "minor", "color": "#34d399"},
    {"degree": 150, "name": "Quincunx", "classification": "minor", "color": "#c084fc"},
]
