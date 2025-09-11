import streamlit as st
import pandas as pd
import motor
import motorAvanzado as motoravanzado
import re


# Cargar estilos de la pagina base
with open("estilos/estilosSimulador.css") as formStyles:
    st.markdown(f"<style>{formStyles.read()}</style>", unsafe_allow_html=True)

# Cargar estilos desde el archivo externo
with open("estilos/mainStyles.css") as mainStyles:
    st.markdown(f"<style>{mainStyles.read()}</style>", unsafe_allow_html=True)


# --- Encabezado de empresa ---
# Muestra el logo con st.image
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

# CSS personalizado

with st.form("mi_formulario"):
    st.text_input("Campo de ejemplo")
    st.number_input("Otro campo")
    st.form_submit_button("Enviar")
    

st.title("Formulario de Plan de Izaje")

with st.form("izaje_form"):
    peso_carga = st.number_input("Peso de carga (kg)", min_value=0, key="pesoCarga")
    largo_carga = st.number_input("Largo de carga (m)", min_value=0.0, step=0.1, key="largoCarga")
    forma_carga = st.selectbox("Forma de carga", ["cilindro", "rectangular", "otro"], key="formaCarga")
    angulo_slingas = st.number_input("Ángulo slingas (grados)", min_value=0.0, max_value=90.0, step=1.0, key="anguloSlingas")
    distancia_horizontal = st.number_input("Distancia horizontal (m)", min_value=0.0, step=0.1, key="distanciaHorizontal")
    altura_izaje = st.number_input("Altura de izaje (m)", min_value=0.0, step=0.1, key="alturaIzaje")
    submitted = st.form_submit_button("Procesar")

if submitted:
    errores = []
    # Validar campo_num: solo dígitos y rango entre 1 y 1,000,000
    if not peso_carga:
        errores.append("El campo numérico es obligatorio.")
    elif not re.match(r"^\d+$", str(peso_carga)):
        errores.append("El campo numérico solo debe contener números del 0 al 9, sin decimales ni otros caracteres.")
    else:
        valor_num = int(peso_carga)
        if not (1 <= valor_num <= 1000000):
            errores.append("El campo numérico debe ser un número entero entre 1 y 1,000,000.")

    if errores:
        for err in errores:
            st.error(err)
    else:
        datos = {
            "peso_carga_kg": peso_carga,
            "largo_carga_m": largo_carga,
            "forma_carga": forma_carga,
            "angulo_slingas_deg": angulo_slingas,
            "distancia_horizontal_m": distancia_horizontal,
            "altura_izaje_m": altura_izaje
        }
        st.success("Formulario enviado correctamente.")

    #resultado = motor.motor_izaje(datos)
    resultado = motoravanzado.motor_izaje(datos)
    st.write("### Plan de Izaje")
    st.table(pd.DataFrame([resultado]))