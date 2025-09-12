import psycopg2
from .grua_queries import OBTENER_GRUAS

class GruaDAO:
    _instance = None

    def __new__(cls, db_params=None):
        if cls._instance is None:
            cls._instance = super(GruaDAO, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, db_params=None):
        if not self._initialized:
            self.db_params = db_params
            self._initialized = True

    def obtener_gruas(self):
        if not self.db_params:
            # Datos de ejemplo para pruebas sin base de datos
            return [
                {"modelo": "GR-350XL Tadano", "capacidad_kg": 35000, "pluma_max_m": 30},
                {"modelo": "GMK 3050 Grove", "capacidad_kg": 50000, "pluma_max_m": 38},
                {"modelo": "LTM 1100 Liebherr", "capacidad_kg": 100000, "pluma_max_m": 52},
            ]
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cur:
                    cur.execute(OBTENER_GRUAS)
                    gruas = cur.fetchall()
            return [
                {"modelo": g[0], "capacidad_kg": g[1], "pluma_max_m": g[2]}
                for g in gruas
            ]
        except Exception as e:
            print(f"Error al obtener grúas: {e}")
            return []