"""
config_db.py
------------
Módulo de configuración para la conexión a la base de datos PostgreSQL.

Este archivo se encarga de cargar las variables de entorno necesarias para la conexión a la base de datos,
leyendo los parámetros desde un archivo de entorno externo (settings.env) mediante la librería python-dotenv.
Centraliza la configuración de la base de datos para facilitar el mantenimiento y la seguridad del proyecto.

Estructura:
- Carga de variables de entorno desde settings.env.
- Definición del diccionario DB_PARAMS con los parámetros de conexión.

Autor: Ing. Elkin Moreno
Fecha: 12 Sept 2025
Versión: 0.1
"""

import os
from dotenv import load_dotenv
from pathlib import Path

# Define la ruta absoluta al archivo settings.env ubicado en la raíz del proyecto.
dotenv_path = Path(__file__).parent.parent / "settings.env"

# Carga las variables de entorno desde el archivo especificado.
load_dotenv(dotenv_path)

# Diccionario con los parámetros de conexión a la base de datos PostgreSQL.
# Estos valores se obtienen de las variables de entorno cargadas previamente.
DB_PARAMS = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT")
}
print(DB_PARAMS)  # <-- Verifica que la contraseña no sea None ni vacía