import math

def seleccionar_grua(peso, pluma_requerida):
    if peso <= 20000:
        return "Grúa articulada 30T"
    elif peso <= 50000:
        return "Grúa telescópica 100T"
    elif peso <= 100000:
        return "Grúa hidráulica 200T"
    else:
        return "Grúa sobre orugas o sistema de gatos hidráulicos"
        
    #if peso <= 35000 and pluma_requerida <= 30:
    #    modelo = "GR-350XL Tadano"
    #elif peso <= 50000 and pluma_requerida <= 38:
    #    modelo = "GMK 3050 Grove"
    #elif peso <= 100000 and pluma_requerida <= 52:
    #    modelo = "LTM 1100 Liebherr"
    #else:
    #    modelo = "Consulta especializada requerida"

def calcular_tension(peso, angulo):
    rad = math.radians(angulo)
    tension = peso / (2 * math.sin(rad))
    return round(tension, 2)

def calcular_plumaRequerida(peso, angulo):
    rad = math.radians(angulo)
    tension = peso / (2 * math.sin(rad))
    return round(tension, 2)

def recomendar_spreader(largo, forma):
    if largo > 6 or forma.lower() in ["cilíndrica", "tanque"]:
        return "Spreader beam recomendado"
    return "No se requiere spreader"


def motor_izaje(datos):
    # Variables
    peso = datos["peso_carga_kg"]
    largo = datos["largo_carga_m"]
    forma = datos["forma_carga"].lower()
    angulo = math.radians(datos["angulo_slingas_deg"])
    distancia = datos["distancia_horizontal_m"]
    altura = datos["altura_izaje_m"]

    # Cálcular tension
    tension = calcular_tension(peso, angulo)
    #tension = peso / (2 * math.sin(angulo))

    # Calcular pluma requerida
    pluma_requerida = calcular_plumaRequerida(distancia, altura)
    #pluma_requerida = math.sqrt(distancia**2 + altura**2)

    # Reglas de inferencia spreader
    spreader = recomendar_spreader(largo, forma)
    #spreader = "Sí" if largo > 6 or forma in ["cilíndrica", "tanque"] else "No"

    #Seleccion tipo de grua
    modelo = seleccionar_grua(peso, pluma_requerida)

    #evaluar tipo de grua
    return {
        "modelo_grua": modelo,
        "tension_eslinga_kg": round(tension, 2),
        "pluma_requerida_m": round(pluma_requerida, 2),
        "requiere_spreader": spreader
    }
