Simulador Logístico de Grúas
============================

Descripción General
-------------------
Este proyecto es un simulador logístico para la recomendación de grúas, desarrollado en Python. Permite calcular y sugerir el modelo de grúa más adecuado para una operación de izaje, considerando parámetros técnicos y operativos ingresados por el usuario.

Propósito del Proyecto
----------------------
El propósito principal es facilitar la selección técnica de grúas para operaciones logísticas, optimizando la seguridad y eficiencia en el manejo de cargas. El sistema automatiza el proceso de recomendación, integrando una base de datos de modelos de grúas y una lógica de negocio robusta.

Arquitectura del Proyecto
-------------------------
El proyecto sigue una arquitectura modular inspirada en el patrón MVC (Modelo-Vista-Controlador):

- **View (Vista):** Implementada con Streamlit, permite la interacción con el usuario a través de formularios web.
- **Controller (Controlador):** Orquesta la lógica de negocio, recibe los datos de la vista, consulta la base de datos y llama al backend para procesar la recomendación.
- **Backend (Modelo):** Incluye la lógica de negocio (`motor.py`) y el acceso a datos (`dao/grua_dao.py`). El backend no interactúa directamente con la base de datos, sino a través del DAO.
- **API:** Expuesta mediante FastAPI, permite consumir la lógica de recomendación desde otros sistemas o aplicaciones externas.

Estructura de Carpetas y Archivos
---------------------------------
- `inicio2.py` / `view1.py`         → Vista (Streamlit)
- `controller.py`                   → Controlador principal
- `motor.py`                        → Lógica de negocio (backend)
- `dao/grua_dao.py`                 → Acceso a datos (DAO)
- `dao/grua_queries.py`             → Sentencias SQL centralizadas
- `config/config_db.py`             → Configuración de conexión a la base de datos
- `settings.env`                    → Variables de entorno (no subir a GitHub)
- `api_logisticSimulator.py`        → API REST con FastAPI
- `estilos/`                        → Archivos de estilos CSS para la vista
- `.venv/`                          → Entorno virtual de Python (no subir a GitHub)
- `.gitignore`                      → Exclusiones para el control de versiones

Notas adicionales
-----------------
- La base de datos utilizada es PostgreSQL.
- El proyecto está preparado para ser ejecutado tanto como aplicación web (Streamlit) como servicio API (FastAPI).
- Se recomienda mantener las credenciales y configuraciones sensibles fuera del repositorio público.
