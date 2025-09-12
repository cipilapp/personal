"""
view1.py
--------
Vista principal del Simulador Logístico de Grúas.

Este archivo implementa la interfaz de usuario usando Streamlit, permitiendo al usuario ingresar los datos del plan de izaje y visualizar la recomendación de grúa. 
Incluye carga de estilos personalizados, validación de datos y presentación de resultados.

Estructura:
- Carga de estilos CSS y logo de la empresa.
- Formulario de ingreso de datos técnicos del izaje.
- Validación de campos y presentación de errores.
- Llamado al controlador para obtener la recomendación.
- Visualización de resultados en tabla.

Autor: Ing. Elkin Moreno
Fecha: 12 Sept 2025
Versión: 0.1
"""

import streamlit as st
import pandas as pd
import re
from controller import GruaController

# Instancia del controlador principal
controller = GruaController()

# --- Carga de estilos personalizados ---
# Carga y aplica los estilos CSS desde archivos externos para personalizar la apariencia de la app.
with open("estilos/estilosSimulador.css") as formStyles:
    st.markdown(f"<style>{formStyles.read()}</style>", unsafe_allow_html=True)

with open("estilos/mainStyles.css") as mainStyles:
    st.markdown(f"<style>{mainStyles.read()}</style>", unsafe_allow_html=True)

# --- Encabezado de empresa ---
# Muestra el logo y la información de la empresa en la parte superior de la app.
st.image("img/logo.jpg", width=180)

st.markdown("""
    <div class="company-header">
        <div class="company-title">GRUPO TRANSPORTADOR LOGIPEX</div>
        <div class="company-desc">
            Transporte Internacional de Cargas Pesadas y Extra Dimensionadas<br>
            Especialistas en transporte de carga extra dimensionada y extra pesada.<br>
            <a href="http://www.grupotransportadorlogipex.com" style="color:#ffcc00;" target="_blank">www.grupotransportadorlogipex.com</a>
        </div>
    </div>            
""", unsafe_allow_html=True)

# --- Formulario de ejemplo (puedes eliminarlo si no lo usas) ---
with st.form("mi_formulario"):
    st.text_input("Campo de ejemplo")
    st.number_input("Otro campo")
    st.form_submit_button("Enviar")

# --- Formulario principal de Plan de Izaje ---
st.title("Formulario de Plan de Izaje")

with st.form("izaje_form"):
    # Campos de entrada para los datos técnicos del izaje
    peso_carga = st.number_input("Peso de carga (kg)", min_value=0, key="pesoCarga")
    largo_carga = st.number_input("Largo de carga (m)", min_value=0.0, step=0.1, key="largoCarga")
    forma_carga = st.selectbox("Forma de carga", ["cilindro", "rectangular", "otro"], key="formaCarga")
    angulo_slingas = st.number_input("Ángulo slingas (grados)", min_value=0.0, max_value=90.0, step=1.0, key="anguloSlingas")
    distancia_horizontal = st.number_input("Distancia horizontal (m)", min_value=0.0, step=0.1, key="distanciaHorizontal")
    altura_izaje = st.number_input("Altura de izaje (m)", min_value=0.0, step=0.1, key="alturaIzaje")
    submitted = st.form_submit_button("Procesar")

if submitted:
    errores = []
    # Validación del campo peso_carga: obligatorio, solo dígitos, rango válido
    if not peso_carga:
        errores.append("El campo numérico es obligatorio.")
    elif not re.match(r"^\d+$", str(peso_carga)):
        errores.append("El campo numérico solo debe contener números del 0 al 9, sin decimales ni otros caracteres.")
    else:
        valor_num = int(peso_carga)
        if not (1 <= valor_num <= 1000000):
            errores.append("El campo numérico debe ser un número entero entre 1 y 1,000,000.")

    # Muestra los errores encontrados en la validación
    if errores:
        for err in errores:
            st.error(err)
    else:
        # Si no hay errores, prepara los datos para el controlador
        datos = {
            "peso_carga_kg": peso_carga,
            "largo_carga_m": largo_carga,
            "forma_carga": forma_carga,
            "angulo_slingas_deg": angulo_slingas,
            "distancia_horizontal_m": distancia_horizontal,
            "altura_izaje_m": altura_izaje
        }
        st.success("Formulario enviado correctamente.")

        # Llama al controlador para obtener la recomendación de grúa
        resultado = controller.recomendar_grua(datos)

        # Presenta el resultado en una tabla
        st.write("### Plan de Izaje")
        st.table(pd.DataFrame([resultado]))