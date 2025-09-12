"""
grua_dao.py
-----------
Data Access Object (DAO) para la gestión de información técnica de grúas.

Este módulo encapsula el acceso a la base de datos para obtener los registros de grúas, centralizando las consultas SQL y el manejo de la conexión.
Implementa el patrón Singleton para asegurar que solo exista una instancia de acceso a datos durante la ejecución de la aplicación.

Estructura:
- Clase GruaDAO: Singleton para acceso a datos de grúas.
- Método obtener_gruas: Recupera la lista de grúas desde la base de datos o retorna datos de ejemplo si no hay conexión.

Autor: Ing. Elkin Moreno
Fecha: 12 Sept 2025
Versión: 0.1
"""

import psycopg2
from .grua_queries import OBTENER_GRUAS

class GruaDAO:
    """
    Data Access Object (DAO) para la entidad Grúa.
    Implementa el patrón Singleton para evitar múltiples instancias y conexiones innecesarias.

    Métodos:
        obtener_gruas(): Recupera la lista de grúas desde la base de datos.
    """
    _instance = None

    def __new__(cls, db_params=None):
        """
        Controla la creación de instancias para implementar el patrón Singleton.
        Si ya existe una instancia, retorna la existente.
        """
        if cls._instance is None:
            cls._instance = super(GruaDAO, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, db_params=None):
        """
        Inicializa la instancia con los parámetros de conexión a la base de datos.
        Solo se ejecuta una vez por el patrón Singleton.
        """
        if not self._initialized:
            self.db_params = db_params
            self._initialized = True

    def obtener_gruas(self):
        """
        Recupera la lista de grúas desde la base de datos PostgreSQL.
        Si no hay parámetros de conexión, retorna datos de ejemplo para pruebas.

        Returns:
            list[dict]: Lista de diccionarios con la información técnica de cada grúa.
        """
        if not self.db_params:
            # Datos de ejemplo para pruebas sin base de datos
            return [
                {"modelo": "GR-350XL Tadano", "capacidad_kg": 35000, "pluma_max_m": 30},
                {"modelo": "GMK 3050 Grove", "capacidad_kg": 50000, "pluma_max_m": 38},
                {"modelo": "LTM 1100 Liebherr", "capacidad_kg": 100000, "pluma_max_m": 52},
            ]
        try:
            # Abre la conexión a la base de datos usando un contexto 'with' para asegurar el cierre correcto
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cur:
                    # Ejecuta la consulta SQL definida en grua_queries.py
                    cur.execute(OBTENER_GRUAS)
                    gruas = cur.fetchall()
            # Convierte los resultados en una lista de diccionarios para fácil manejo en el backend
            return [
                {"modelo": g[0], "capacidad_kg": g[1], "pluma_max_m": g[2]}
                for g in gruas
            ]
        except Exception as e:
            # Manejo de errores: imprime el error y retorna una lista vacía
            print(f"Error al obtener grúas: {e}")
            return []