OBTENER_GRUAS = """
    SELECT modelo, capacidad_kg, pluma_max_m
    FROM gruas
    ORDER BY capacidad_kg ASC, pluma_max_m ASC
"""