import math

def motor_izaje(datos):
    # Variables
    peso = datos["peso_carga_kg"]
    largo = datos["largo_carga_m"]
    forma = datos["forma_carga"].lower()
    angulo = math.radians(datos["angulo_slingas_deg"])
    distancia = datos["distancia_horizontal_m"]
    altura = datos["altura_izaje_m"]

    # Cálculos
    tension = peso / (2 * math.sin(angulo))
    pluma_requerida = math.sqrt(distancia**2 + altura**2)

    # Reglas de inferencia
    spreader = "Sí" if largo > 6 or forma in ["cilíndrica", "tanque"] else "No"

    # tipo de grua
    if peso <= 35000 and pluma_requerida <= 30:
        modelo = "GR-350XL Tadano"
    elif peso <= 50000 and pluma_requerida <= 38:
        modelo = "GMK 3050 Grove"
    elif peso <= 100000 and pluma_requerida <= 52:
        modelo = "LTM 1100 Liebherr"
    else:
        modelo = "Consulta especializada requerida"

    return {
        "modelo_grua": modelo,
        "tension_eslinga_kg": round(tension, 2),
        "pluma_requerida_m": round(pluma_requerida, 2),
        "requiere_spreader": spreader
    }
