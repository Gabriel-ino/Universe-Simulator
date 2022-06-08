def verify_calculation_by_sun(celestial_body1, celestial_body2, distance):
    try:
        verifier = celestial_body2.is_the_sun
    except AttributeError:
        return False

    if verifier:
        celestial_body1.distance_from_sun = distance
