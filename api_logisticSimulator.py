"""
api_logisticSimulator.py
------------------------
API REST principal del Simulador Logístico de Grúas.

Este archivo expone la lógica de recomendación de grúas como un servicio web RESTful usando FastAPI.
Permite recibir solicitudes POST con los datos técnicos del izaje y retorna la recomendación de grúa en formato JSON.
La API puede ser consumida por aplicaciones externas, móviles o sistemas de terceros.

Estructura:
- Inicialización de la aplicación FastAPI.
- Instanciación del controlador principal.
- Definición del endpoint /recomendar_grua/ para recibir y procesar solicitudes.

Autor: Ing. Elkin Moreno
Fecha: 12 Sept 2025
Versión: 0.1
"""

from fastapi import FastAPI
from controller import GruaController

# Inicializa la aplicación FastAPI
app = FastAPI()

# Instancia del controlador principal para la recomendación de grúas
controller = GruaController()

@app.post("/recomendar_grua/")
def recomendar_grua(datos: dict):
    """
    Endpoint POST para recomendar una grúa.

    Recibe un JSON con los datos técnicos del izaje y retorna la recomendación de grúa.
    El controlador orquesta la consulta a la base de datos y la lógica de negocio.

    Args:
        datos (dict): Datos técnicos del plan de izaje enviados en el cuerpo de la solicitud.

    Returns:
        dict: Resultado de la recomendación de grúa.
    """
    # Llama al controlador para procesar la recomendación y retorna el resultado
    return controller.recomendar_grua(datos)