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
        'mean_node', 'true_node', 'chiron', 'pars_fortuna'
    ]

    # Planetas regulares
    for planet_name in planet_names:
        if hasattr(subject, planet_name):
            planet_obj = getattr(subject, planet_name)
            if planet_obj:
                try:
                    planets.append({
                        'name': planet_name,
                        'sign': getattr(planet_obj, 'sign', ''),
                        'sign_num': getattr(planet_obj, 'sign_num', 0),
                        'position': getattr(planet_obj, 'position', 0.0),
                        'abs_pos': getattr(planet_obj, 'abs_pos', 0.0),
                        'emoji': getattr(planet_obj, 'emoji', ''),
                        'house': getattr(planet_obj, 'house', ''),
                        'retrograde': getattr(planet_obj, 'retrograde', False)
                    })
                except Exception:
                    pass

    return planets


def extract_houses(subject):
    """Extrae cúspides de casas del objeto AstrologicalSubject"""
    houses = []

    # Lista de casas (Kerykeion usa first_house para casa 1, second_house para casa 2, etc)
    house_names = [
        'first_house', 'second_house', 'third_house', 'fourth_house',
        'fifth_house', 'sixth_house', 'seventh_house', 'eighth_house',
        'ninth_house', 'tenth_house', 'eleventh_house', 'twelfth_house'
    ]

    for i, house_name in enumerate(house_names, 1):
        if hasattr(subject, house_name):
            house_obj = getattr(subject, house_name)
            if house_obj:
                try:
                    houses.append({
                        'house_number': i,
                        'sign': getattr(house_obj, 'sign', ''),
                        'sign_num': getattr(house_obj, 'sign_num', 0),
                        'position': getattr(house_obj, 'position', 0.0),
                        'abs_pos': getattr(house_obj, 'abs_pos', 0.0),
                        'emoji': getattr(house_obj, 'emoji', '')
                    })
                except Exception:
                    pass

    return houses


def extract_aspects(subject):
    """Extrae aspectos del objeto AstrologicalSubject"""
    aspects = []

    if hasattr(subject, 'aspects_list') and subject.aspects_list:
        for aspect in subject.aspects_list:
            if aspect:
                try:
                    # Los aspectos son diccionarios en Kerykeion
                    if isinstance(aspect, dict):
                        aspects.append({
                            'planet1': aspect.get('p1_name', ''),
                            'planet2': aspect.get('p2_name', ''),
                            'aspect': aspect.get('aspect', ''),
                            'orbit': aspect.get('orbit', 0.0),
                            'aspect_degrees': aspect.get('aspect_degrees', 0),
                            'aid': aspect.get('aid', 0),
                            'diff': aspect.get('orbit', 0.0),
                            'p1_abs_pos': aspect.get('p1_abs_pos', 0.0),
                            'p2_abs_pos': aspect.get('p2_abs_pos', 0.0)
                        })
                except Exception:
                    pass

    return aspects
