import math

def motor_izaje(datos, gruas):
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

    # Selección de grúa
    modelo = "Consulta especializada requerida"
    for grua in gruas:
        if peso <= grua["capacidad_kg"] and pluma_requerida <= grua["pluma_max_m"]:
            modelo = grua["modelo"]
            break

    return {
        "modelo_grua": modelo,
        "tension_eslinga_kg": round(tension, 2),
        "pluma_requerida_m": round(pluma_requerida, 2),
        "requiere_spreader": spreader
    }
