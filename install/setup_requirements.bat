#!/bin/bash

echo "==== Instalador de requerimientos para el proyecto /personal ===="

# 1. Instalar Python (si no está instalado)
echo "Asegúrate de tener Python 3.8+ instalado. Descárgalo de https://www.python.org/downloads/ si es necesario."

# 2. Instalar Git (si no está instalado)
echo "Asegúrate de tener Git instalado. Descárgalo de https://git-scm.com/downloads si es necesario."

# 3. Clonar el repositorio de GitHub (si aún no lo has hecho)
# Sustituye la URL por la de tu repositorio
# git clone https://github.com/usuario/tu-repo.git

# 4. Crear y activar entorno virtual de Python
python -m venv venv
# Para Linux/Mac
source venv/bin/activate
# Para Windows (descomenta la siguiente línea si usas Windows)
# venv\Scripts\activate

# 5. Actualizar pip
pip install --upgrade pip

# 6. Instalar librerías de Python necesarias
pip install streamlit
pip install googlemaps
pip install psycopg2-binary
pip install pillow
pip install pandas

# 7. Instalar PostgreSQL
echo "Instala PostgreSQL desde https://www.postgresql.org/download/ si no lo tienes."

# localhost:5432 
#maintenaince_db: postgres 
#usuarioserver: postgres  password: admin

echo "Recuerda anotar el usuario, contraseña y puerto configurados."

# 8. Crear la base de datos y tabla en PostgreSQL
echo "Ejecutando script para crear la base de datos y tabla..."
echo "
CREATE DATABASE simuladorLogistico;
" > crear_db.sql

echo "
-- Ejecuta esto conectado a la base de datos simuladorLogistico:
CREATE TABLE IF NOT EXISTS gruas (
    id SERIAL PRIMARY KEY,
    modelo VARCHAR(100),
    capacidad_kg INTEGER,
    pluma_max_m REAL,
    otras_caracteristicas TEXT
);
" > crear_tabla.sql

echo "Para crear la base de datos y la tabla, ejecuta:"
echo "psql -U TU_USUARIO -f crear_db.sql"
echo "psql -U TU_USUARIO -d simuladorLogistico -f crear_tabla.sql"

# 9. Configurar credenciales de Google Maps y variables de entorno
echo "Configurando credenciales de Google Maps y variables de entorno..."

echo "
# Crea un archivo .env en la raíz del proyecto con el siguiente contenido:
GOOGLE_MAPS_API_KEY=TU_API_KEY
DB_USER=TU_USUARIO
DB_PASSWORD=TU_PASSWORD
DB_HOST=localhost
DB_PORT=5432
DB_NAME=simuladorLogistico
" > .env.example

echo "Recuerda copiar .env.example a .env y poner tus credenciales reales."

echo "Para cargar variables de entorno en tu código Python, puedes usar la librería python-dotenv:"
echo "pip install python-dotenv"
echo "Y en tu código:"
echo "from dotenv import load_dotenv; load_dotenv()"

# 10. (Opcional) Instalar JupyterLab
pip install jupyterlab

#11. Instalar manejo de archivos de .env
echo "Instalar libreria .env"
pip install python-dotenv
echo "Finalización instalacion .env"

echo "==== Instalación completada ===="
echo "Recuerda:"
echo "- Configurar las credenciales de Google Maps en tu archivo .env."
echo "- Crear la base de datos y tablas necesarias en PostgreSQL."
echo "- Configurar las variables de entorno si es necesario."