"""
motor.py
--------
Módulo de lógica de negocio para el Simulador Logístico de Grúas.

Este archivo implementa la función principal de recomendación de grúas, 
procesando los datos técnicos del izaje y seleccionando el modelo de grúa más adecuado 
según la información técnica disponible.

Estructura:
- Función motor_izaje: Realiza los cálculos de izaje y determina la grúa recomendada.

Autor: Ing. Elkin Moreno
Fecha: 12 Sept 2025
Versión: 0.1
"""

import math

def motor_izaje(datos, gruas):
    """
    Procesa los datos técnicos del izaje y recomienda el modelo de grúa más adecuado.

    Args:
        datos (dict): Diccionario con los datos técnicos del plan de izaje.
            - peso_carga_kg: Peso de la carga en kilogramos.
            - largo_carga_m: Largo de la carga en metros.
            - forma_carga: Forma de la carga (ej. 'cilindro', 'rectangular').
            - angulo_slingas_deg: Ángulo de las eslingas en grados.
            - distancia_horizontal_m: Distancia horizontal de izaje en metros.
            - altura_izaje_m: Altura de izaje en metros.
        gruas (list[dict]): Lista de diccionarios con la información técnica de cada grúa.

    Returns:
        dict: Resultado de la recomendación, incluyendo modelo de grúa, tensión de eslinga, 
              pluma requerida y si requiere spreader.
    """
    # --- Extracción y preparación de variables ---
    peso = datos["peso_carga_kg"]
    largo = datos["largo_carga_m"]
    forma = datos["forma_carga"].lower()
    angulo = math.radians(datos["angulo_slingas_deg"])  # Convierte el ángulo a radianes para cálculos trigonométricos
    distancia = datos["distancia_horizontal_m"]
    altura = datos["altura_izaje_m"]

    # --- Cálculo de la tensión en las eslingas ---
    # Fórmula: tensión = peso / (2 * sin(ángulo))
    # Se asume izaje con dos eslingas y ángulo simétrico
    try:
        tension = peso / (2 * math.sin(angulo)) if angulo != 0 else float('inf')
    except Exception as e:
        tension = float('inf')
        print(f"Error en el cálculo de la tensión: {e}")

    # --- Cálculo de la pluma requerida ---
    # Se usa el teorema de Pitágoras para estimar la longitud mínima de pluma
    pluma_requerida = math.sqrt(distancia**2 + altura**2)

    # --- Reglas de inferencia para spreader ---
    # Se recomienda spreader si la carga es larga o de forma especial
    spreader = "Sí" if largo > 6 or forma in ["cilíndrica", "tanque"] else "No"

    # --- Selección de la grúa recomendada ---
    # Se busca la primera grúa que cumpla con la capacidad y pluma requerida
    modelo = "Consulta especializada requerida"
    for grua in gruas:
        if peso <= grua["capacidad_kg"] and pluma_requerida <= grua["pluma_max_m"]:
            modelo = grua["modelo"]
            break

    # --- Retorno del resultado ---
    return {
        "modelo_grua": modelo,
        "tension_eslinga_kg": round(tension, 2),
        "pluma_requerida_m": round(pluma_requerida, 2),
        "requiere_spreader": spreader
    }