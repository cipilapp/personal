"""
controller.py
-------------
Controlador principal del Simulador Logístico de Grúas.

Este archivo implementa la capa de control (Controller) bajo el patrón MVC, 
orquestando la interacción entre la vista (Streamlit o API) y la lógica de negocio (motor.py).
Se encarga de recibir los datos del usuario, consultar la base de datos a través del DAO y 
llamar al backend para procesar la recomendación de grúa.

Estructura:
- Clase GruaController: Controlador principal para la recomendación de grúas.

Autor: Ing. Elkin Moreno
Fecha: 12 Sept 2025
Versión: 0.1
"""

from dao.grua_dao import GruaDAO
from motor import motor_izaje
from config.config_db import DB_PARAMS

class GruaController:
    """
    Controlador para la recomendación de grúas.

    Esta clase orquesta la obtención de datos desde la base de datos y la lógica de negocio.
    Se recomienda instanciarla una sola vez y reutilizarla en la vista o en la API.

    Métodos:
        recomendar_grua(datos_usuario): Procesa los datos del usuario y retorna la recomendación.
    """
    def __init__(self):
        """
        Inicializa el controlador creando una instancia única del DAO con los parámetros de conexión.
        """
        self.dao = GruaDAO(DB_PARAMS)

    def recomendar_grua(self, datos_usuario):
        """
        Procesa la solicitud de recomendación de grúa.

        1. Obtiene la lista de grúas desde la base de datos usando el DAO.
        2. Llama a la función de lógica de negocio (motor_izaje) con los datos del usuario y la lista de grúas.
        3. Retorna el resultado de la recomendación.

        Args:
            datos_usuario (dict): Diccionario con los datos técnicos del plan de izaje.

        Returns:
            dict: Resultado de la recomendación de grúa.
        """
        # Trae los datos de la base de datos (lista de grúas)
        gruas = self.dao.obtener_gruas()
        # Llama a la lógica de negocio para obtener la recomendación
        resultado = motor_izaje(datos_usuario, gruas)
        return resultado