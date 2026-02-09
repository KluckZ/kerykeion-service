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

    # Signos zodiacales - fondo por elemento (colores fuertes)
    "zodiac_bg_0": "#dc2626",           # Aries - Fuego
    "zodiac_bg_1": "#059669",           # Tauro - Tierra
    "zodiac_bg_2": "#d97706",           # Geminis - Aire
    "zodiac_bg_3": "#2563eb",           # Cancer - Agua
    "zodiac_bg_4": "#dc2626",           # Leo - Fuego
    "zodiac_bg_5": "#059669",           # Virgo - Tierra
    "zodiac_bg_6": "#d97706",           # Libra - Aire
    "zodiac_bg_7": "#2563eb",           # Escorpio - Agua
    "zodiac_bg_8": "#dc2626",           # Sagitario - Fuego
    "zodiac_bg_9": "#059669",           # Capricornio - Tierra
    "zodiac_bg_10": "#d97706",          # Acuario - Aire
    "zodiac_bg_11": "#2563eb",          # Piscis - Agua

    # Signos zodiacales - glifos negros
    "zodiac_icon_0": "#000000",         # Aries
    "zodiac_icon_1": "#000000",         # Tauro
    "zodiac_icon_2": "#000000",         # Geminis
    "zodiac_icon_3": "#000000",         # Cancer
    "zodiac_icon_4": "#000000",         # Leo
    "zodiac_icon_5": "#000000",         # Virgo
    "zodiac_icon_6": "#000000",         # Libra
    "zodiac_icon_7": "#000000",         # Escorpio
    "zodiac_icon_8": "#000000",         # Sagitario
    "zodiac_icon_9": "#000000",         # Capricornio
    "zodiac_icon_10": "#000000",        # Acuario
    "zodiac_icon_11": "#000000",        # Piscis

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
    {"id": 1, "name": "Moon", "color": "#94a3b8", "element_points": 40, "label": "Moon"},
    {"id": 2, "name": "Mercury", "color": "#ca8a04", "element_points": 15, "label": "Mercury"},
    {"id": 3, "name": "Venus", "color": "#22c55e", "element_points": 15, "label": "Venus"},
    {"id": 4, "name": "Mars", "color": "#ef4444", "element_points": 15, "label": "Mars"},
    {"id": 5, "name": "Jupiter", "color": "#06b6d4", "element_points": 10, "label": "Jupiter"},
    {"id": 6, "name": "Saturn", "color": "#dc2626", "element_points": 10, "label": "Saturn"},
    {"id": 7, "name": "Uranus", "color": "#4f46e5", "element_points": 10, "label": "Uranus"},
    {"id": 8, "name": "Neptune", "color": "#7c3aed", "element_points": 10, "label": "Neptune"},
    {"id": 9, "name": "Pluto", "color": "#78350f", "element_points": 10, "label": "Pluto"},

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


# ═══════════════════════════════════════════════════════════
# CSS THEME STRING
# Necesario para que inline_css_variables_in_svg() pueda
# reemplazar las var(--kerykeion-chart-color-xxx) en los glifos SVG.
# Sin esto, los glifos de planetas quedan invisibles.
# ═══════════════════════════════════════════════════════════

AZTROSOFIA_CSS = """:root {
    /* Main Colors */
    --kerykeion-chart-color-paper-0: #1e293b;
    --kerykeion-chart-color-paper-1: #ffffff;
    --kerykeion-chart-color-zodiac-bg-0: #dc2626;
    --kerykeion-chart-color-zodiac-bg-1: #059669;
    --kerykeion-chart-color-zodiac-bg-2: #d97706;
    --kerykeion-chart-color-zodiac-bg-3: #2563eb;
    --kerykeion-chart-color-zodiac-bg-4: #dc2626;
    --kerykeion-chart-color-zodiac-bg-5: #059669;
    --kerykeion-chart-color-zodiac-bg-6: #d97706;
    --kerykeion-chart-color-zodiac-bg-7: #2563eb;
    --kerykeion-chart-color-zodiac-bg-8: #dc2626;
    --kerykeion-chart-color-zodiac-bg-9: #059669;
    --kerykeion-chart-color-zodiac-bg-10: #d97706;
    --kerykeion-chart-color-zodiac-bg-11: #2563eb;
    --kerykeion-chart-color-zodiac-icon-0: #000000;
    --kerykeion-chart-color-zodiac-icon-1: #000000;
    --kerykeion-chart-color-zodiac-icon-2: #000000;
    --kerykeion-chart-color-zodiac-icon-3: #000000;
    --kerykeion-chart-color-zodiac-icon-4: #000000;
    --kerykeion-chart-color-zodiac-icon-5: #000000;
    --kerykeion-chart-color-zodiac-icon-6: #000000;
    --kerykeion-chart-color-zodiac-icon-7: #000000;
    --kerykeion-chart-color-zodiac-icon-8: #000000;
    --kerykeion-chart-color-zodiac-icon-9: #000000;
    --kerykeion-chart-color-zodiac-icon-10: #000000;
    --kerykeion-chart-color-zodiac-icon-11: #000000;
    --kerykeion-chart-color-zodiac-radix-ring-0: #cbd5e1;
    --kerykeion-chart-color-zodiac-radix-ring-1: #e2e8f0;
    --kerykeion-chart-color-zodiac-radix-ring-2: #cbd5e1;
    --kerykeion-chart-color-zodiac-transit-ring-0: #c4b5fd;
    --kerykeion-chart-color-zodiac-transit-ring-1: #ddd6fe;
    --kerykeion-chart-color-zodiac-transit-ring-2: #c4b5fd;
    --kerykeion-chart-color-zodiac-transit-ring-3: #c4b5fd;
    --kerykeion-chart-color-houses-radix-line: #94a3b8;
    --kerykeion-chart-color-houses-transit-line: #94a3b8;
    --kerykeion-chart-color-lunar-phase-0: #1e293b;
    --kerykeion-chart-color-lunar-phase-1: #ffffff;

    /* Aspects */
    --kerykeion-chart-color-conjunction: #60a5fa;
    --kerykeion-chart-color-semi-sextile: #a78bfa;
    --kerykeion-chart-color-semi-square: #fbbf24;
    --kerykeion-chart-color-sextile: #10b981;
    --kerykeion-chart-color-quintile: #34d399;
    --kerykeion-chart-color-square: #ef4444;
    --kerykeion-chart-color-trine: #10b981;
    --kerykeion-chart-color-sesquiquadrate: #fb923c;
    --kerykeion-chart-color-biquintile: #34d399;
    --kerykeion-chart-color-quincunx: #c084fc;
    --kerykeion-chart-color-opposition: #ef4444;

    /* Planets */
    --kerykeion-chart-color-sun: #fbbf24;
    --kerykeion-chart-color-moon: #94a3b8;
    --kerykeion-chart-color-mercury: #ca8a04;
    --kerykeion-chart-color-venus: #22c55e;
    --kerykeion-chart-color-mars: #ef4444;
    --kerykeion-chart-color-jupiter: #06b6d4;
    --kerykeion-chart-color-saturn: #dc2626;
    --kerykeion-chart-color-uranus: #4f46e5;
    --kerykeion-chart-color-neptune: #7c3aed;
    --kerykeion-chart-color-pluto: #78350f;
    --kerykeion-chart-color-mean-node: #9ca3af;
    --kerykeion-chart-color-true-node: #9ca3af;
    --kerykeion-chart-color-chiron: #93c5fd;
    --kerykeion-chart-color-first-house: #1e293b;
    --kerykeion-chart-color-tenth-house: #64748b;
    --kerykeion-chart-color-seventh-house: #64748b;
    --kerykeion-chart-color-fourth-house: #64748b;
    --kerykeion-chart-color-mean-lilith: #c084fc;
    --kerykeion-chart-color-true-lilith: #c084fc;
    --kerykeion-chart-color-ceres: #10b981;
    --kerykeion-chart-color-pallas: #22d3ee;
    --kerykeion-chart-color-juno: #fb7185;
    --kerykeion-chart-color-vesta: #ef4444;
    --kerykeion-chart-color-pars-fortunae: #fbbf24;
    --kerykeion-chart-color-vertex: #8b5cf6;
    --kerykeion-chart-color-east-point: #8b5cf6;
    --kerykeion-chart-color-eris: #7c3aed;
    --kerykeion-chart-color-earth: #10b981;
    --kerykeion-chart-color-pholus: #f97316;
    --kerykeion-chart-color-sedna: #f97316;
    --kerykeion-chart-color-haumea: #60a5fa;
    --kerykeion-chart-color-makemake: #10b981;
    --kerykeion-chart-color-ixion: #ef4444;
    --kerykeion-chart-color-orcus: #6366f1;
    --kerykeion-chart-color-quaoar: #a78bfa;
    --kerykeion-chart-color-regulus: #fbbf24;
    --kerykeion-chart-color-spica: #10b981;
    --kerykeion-chart-color-anti-vertex: #8b5cf6;

    /* Arab Parts */
    --kerykeion-chart-color-pars-spiritus: #8b5cf6;
    --kerykeion-chart-color-pars-amoris: #fb7185;
    --kerykeion-chart-color-pars-fidei: #06b6d4;

    /* Elements Percentage */
    --kerykeion-chart-color-fire-percentage: #ef4444;
    --kerykeion-chart-color-earth-percentage: #10b981;
    --kerykeion-chart-color-air-percentage: #fbbf24;
    --kerykeion-chart-color-water-percentage: #60a5fa;

    /* Modalities Percentage */
    --kerykeion-chart-color-cardinal-percentage: #ef4444;
    --kerykeion-chart-color-fixed-percentage: #10b981;
    --kerykeion-chart-color-mutable-percentage: #60a5fa;

    /* Other */
    --kerykeion-chart-color-house-number: #94a3b8;
}
"""
