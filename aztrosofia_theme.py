"""
Aztrosofia Theme for Kerykeion 5.7.2
Tema claro con fondos blancos - colores custom para carta natal SVG

IMPORTANTE:
- celestial_points_settings: "id" debe ser integer (0-41), orden idéntico al default
- aspects_settings: "name" en lowercase, usar "is_major" (no "classification")
- Usar theme=None + colors_settings/celestial_points_settings/aspects_settings
"""

# ═══════════════════════════════════════════════════════════
# COLORS SETTINGS - Override de DEFAULT_CHART_COLORS
# Keys: paper_0, paper_1, zodiac_bg_0-11, zodiac_icon_0-11,
#        zodiac_radix_ring_0-2, houses_radix_line, lunar_phase_0-1
# ═══════════════════════════════════════════════════════════

AZTROSOFIA_COLORS = {
    # paper_0 = color de texto/fill principal, paper_1 = fondo del SVG
    "paper_0": "#1e293b",               # Texto oscuro (slate 800)
    "paper_1": "#ffffff",               # Fondo blanco

    # Signos zodiacales - fondo blanco
    "zodiac_bg_0": "#ffffff",           # Aries
    "zodiac_bg_1": "#f8fafc",           # Tauro
    "zodiac_bg_2": "#ffffff",           # Geminis
    "zodiac_bg_3": "#f8fafc",           # Cancer
    "zodiac_bg_4": "#ffffff",           # Leo
    "zodiac_bg_5": "#f8fafc",           # Virgo
    "zodiac_bg_6": "#ffffff",           # Libra
    "zodiac_bg_7": "#f8fafc",           # Escorpio
    "zodiac_bg_8": "#ffffff",           # Sagitario
    "zodiac_bg_9": "#f8fafc",           # Capricornio
    "zodiac_bg_10": "#ffffff",          # Acuario
    "zodiac_bg_11": "#f8fafc",          # Piscis

    # Signos zodiacales - iconos por elemento
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
    "zodiac_radix_ring_0": "#cbd5e1",   # Anillo exterior (slate 300)
    "zodiac_radix_ring_1": "#e2e8f0",   # Anillo medio (slate 200)
    "zodiac_radix_ring_2": "#cbd5e1",   # Anillo interior (slate 300)

    # Anillos de transito (si aplica)
    "zodiac_transit_ring_0": "#c4b5fd",
    "zodiac_transit_ring_1": "#ddd6fe",
    "zodiac_transit_ring_2": "#c4b5fd",

    # Lineas de casas
    "houses_radix_line": "#94a3b8",     # Slate 400

    # Fase lunar
    "lunar_phase_0": "#1e293b",         # Oscuro
    "lunar_phase_1": "#ffffff",         # Blanco

    # Primer punto de Aries
    "first_point_of_aries": "#8b5cf6",
}


# ═══════════════════════════════════════════════════════════
# CELESTIAL POINTS SETTINGS
# IMPORTANTE: "id" debe ser integer, orden IDENTICO al default de Kerykeion
# Cada item: {id, name, color, element_points, label}
# ═══════════════════════════════════════════════════════════

AZTROSOFIA_CELESTIAL_POINTS = [
    # Planetas principales (indices 0-9)
    {"id": 0, "name": "Sun", "color": "#fbbf24", "element_points": 40, "label": "Sun"},
    {"id": 1, "name": "Moon", "color": "#e0e7ff", "element_points": 40, "label": "Moon"},
    {"id": 2, "name": "Mercury", "color": "#eab308", "element_points": 15, "label": "Mercury"},
    {"id": 3, "name": "Venus", "color": "#22c55e", "element_points": 15, "label": "Venus"},
    {"id": 4, "name": "Mars", "color": "#ef4444", "element_points": 15, "label": "Mars"},
    {"id": 5, "name": "Jupiter", "color": "#06b6d4", "element_points": 10, "label": "Jupiter"},
    {"id": 6, "name": "Saturn", "color": "#dc2626", "element_points": 10, "label": "Saturn"},
    {"id": 7, "name": "Uranus", "color": "#3b82f6", "element_points": 10, "label": "Uranus"},
    {"id": 8, "name": "Neptune", "color": "#8b5cf6", "element_points": 10, "label": "Neptune"},
    {"id": 9, "name": "Pluto", "color": "#92400e", "element_points": 10, "label": "Pluto"},

    # Nodos lunares (indices 10-11)
    {"id": 10, "name": "Mean_North_Lunar_Node", "color": "#9ca3af", "element_points": 0, "label": "Mean_North_Lunar_Node"},
    {"id": 11, "name": "True_North_Lunar_Node", "color": "#9ca3af", "element_points": 0, "label": "True_North_Lunar_Node"},

    # Chiron (index 12)
    {"id": 12, "name": "Chiron", "color": "#93c5fd", "element_points": 0, "label": "Chiron"},

    # Angulos (indices 13-16) - CRITICO: el codigo accede por indice
    {"id": 13, "name": "Ascendant", "color": "#f1f5f9", "element_points": 40, "label": "Asc"},
    {"id": 14, "name": "Medium_Coeli", "color": "#cbd5e1", "element_points": 20, "label": "Mc"},
    {"id": 15, "name": "Descendant", "color": "#cbd5e1", "element_points": 0, "label": "Dsc"},
    {"id": 16, "name": "Imum_Coeli", "color": "#cbd5e1", "element_points": 0, "label": "Ic"},

    # Lilith (index 17)
    {"id": 17, "name": "Mean_Lilith", "color": "#c084fc", "element_points": 0, "label": "Mean_Lilith"},

    # Nodos Sur (indices 18-19)
    {"id": 18, "name": "Mean_South_Lunar_Node", "color": "#9ca3af", "element_points": 0, "label": "Mean_South_Lunar_Node"},
    {"id": 19, "name": "True_South_Lunar_Node", "color": "#9ca3af", "element_points": 0, "label": "True_South_Lunar_Node"},

    # Lilith verdadera (index 20)
    {"id": 20, "name": "True_Lilith", "color": "#c084fc", "element_points": 0, "label": "True_Lilith"},

    # Earth (index 21)
    {"id": 21, "name": "Earth", "color": "#10b981", "element_points": 0, "label": "Earth"},

    # Asteroides (indices 22-28)
    {"id": 22, "name": "Pholus", "color": "#f97316", "element_points": 0, "label": "Pholus"},
    {"id": 23, "name": "Ceres", "color": "#10b981", "element_points": 0, "label": "Ceres"},
    {"id": 24, "name": "Pallas", "color": "#22d3ee", "element_points": 0, "label": "Pallas"},
    {"id": 25, "name": "Juno", "color": "#fb7185", "element_points": 0, "label": "Juno"},
    {"id": 26, "name": "Vesta", "color": "#ef4444", "element_points": 0, "label": "Vesta"},
    {"id": 27, "name": "Eris", "color": "#7c3aed", "element_points": 0, "label": "Eris"},
    {"id": 28, "name": "Sedna", "color": "#f97316", "element_points": 0, "label": "Sedna"},

    # TNOs (indices 29-33)
    {"id": 29, "name": "Haumea", "color": "#60a5fa", "element_points": 0, "label": "Haumea"},
    {"id": 30, "name": "Makemake", "color": "#10b981", "element_points": 0, "label": "Makemake"},
    {"id": 31, "name": "Ixion", "color": "#ef4444", "element_points": 0, "label": "Ixion"},
    {"id": 32, "name": "Orcus", "color": "#6366f1", "element_points": 0, "label": "Orcus"},
    {"id": 33, "name": "Quaoar", "color": "#a78bfa", "element_points": 0, "label": "Quaoar"},

    # Estrellas fijas (indices 34-35)
    {"id": 34, "name": "Regulus", "color": "#fbbf24", "element_points": 0, "label": "Regulus"},
    {"id": 35, "name": "Spica", "color": "#10b981", "element_points": 0, "label": "Spica"},

    # Arabic Parts (indices 36-39)
    {"id": 36, "name": "Pars_Fortunae", "color": "#fbbf24", "element_points": 5, "label": "Fortune"},
    {"id": 37, "name": "Pars_Spiritus", "color": "#8b5cf6", "element_points": 0, "label": "Spirit"},
    {"id": 38, "name": "Pars_Amoris", "color": "#fb7185", "element_points": 0, "label": "Love"},
    {"id": 39, "name": "Pars_Fidei", "color": "#06b6d4", "element_points": 0, "label": "Faith"},

    # Vertex (indices 40-41)
    {"id": 40, "name": "Vertex", "color": "#8b5cf6", "element_points": 0, "label": "Vertex"},
    {"id": 41, "name": "Anti_Vertex", "color": "#8b5cf6", "element_points": 0, "label": "Anti_Vertex"},
]


# ═══════════════════════════════════════════════════════════
# ASPECTS SETTINGS
# IMPORTANTE: "name" en lowercase, usar "is_major" (no "classification")
# Cada item: {degree, name, is_major, color}
# ═══════════════════════════════════════════════════════════

AZTROSOFIA_ASPECTS = [
    # Aspectos mayores
    {"degree": 0, "name": "conjunction", "is_major": True, "color": "#60a5fa"},
    {"degree": 60, "name": "sextile", "is_major": True, "color": "#10b981"},
    {"degree": 90, "name": "square", "is_major": True, "color": "#ef4444"},
    {"degree": 120, "name": "trine", "is_major": True, "color": "#10b981"},
    {"degree": 180, "name": "opposition", "is_major": True, "color": "#ef4444"},

    # Aspectos menores
    {"degree": 30, "name": "semi-sextile", "is_major": False, "color": "#a78bfa"},
    {"degree": 45, "name": "semi-square", "is_major": False, "color": "#fbbf24"},
    {"degree": 72, "name": "quintile", "is_major": False, "color": "#34d399"},
    {"degree": 135, "name": "sesquiquadrate", "is_major": False, "color": "#fb923c"},
    {"degree": 144, "name": "biquintile", "is_major": False, "color": "#34d399"},
    {"degree": 150, "name": "quincunx", "is_major": False, "color": "#c084fc"},
]
