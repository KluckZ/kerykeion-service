"""
Kerykeion Service - Utils
License: AGPL-3.0
"""

def extract_planets(subject):
    """Extrae posiciones planetarias del objeto AstrologicalSubject"""
    planets = []

    # Lista de planetas a extraer
    planet_names = [
        'sun', 'moon', 'mercury', 'venus', 'mars',
        'jupiter', 'saturn', 'uranus', 'neptune', 'pluto',
        'mean_node', 'true_node', 'chiron', 'pars_fortuna', 'asc', 'mc'
    ]

    for planet_name in planet_names:
        if hasattr(subject, planet_name):
            planet_obj = getattr(subject, planet_name)
            planets.append({
                'name': planet_name,
                'sign': planet_obj.get('sign', ''),
                'position': planet_obj.get('position', 0.0),
                'abs_pos': planet_obj.get('abs_pos', 0.0),
                'house': planet_obj.get('house', ''),
                'retrograde': planet_obj.get('retrograde', False)
            })

    return planets


def extract_houses(subject):
    """Extrae cúspides de casas del objeto AstrologicalSubject"""
    houses = []

    for i in range(1, 13):
        house_attr = f'first_house' if i == 1 else f'house{i}'
        if hasattr(subject, house_attr):
            house_obj = getattr(subject, house_attr)
            houses.append({
                'house_number': i,
                'sign': house_obj.get('sign', ''),
                'position': house_obj.get('position', 0.0),
                'abs_pos': house_obj.get('abs_pos', 0.0)
            })

    return houses


def extract_aspects(subject):
    """Extrae aspectos del objeto AstrologicalSubject"""
    aspects = []

    if hasattr(subject, 'aspects_list'):
        for aspect in subject.aspects_list:
            aspects.append({
                'planet1': aspect.get('p1_name', ''),
                'planet2': aspect.get('p2_name', ''),
                'aspect': aspect.get('aspect', ''),
                'orb': aspect.get('orb', 0.0),
                'diff': aspect.get('orbit', 0.0),
                'aid': aspect.get('aid', 0)
            })

    return aspects
