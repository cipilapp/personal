import streamlit as st
import pandas as pd
import motor

# --- Estilos personalizados ---
st.markdown("""
    <style>
        .main {
            background-color: #f4f6f8;
        }
        .company-header {
            background-color: #003366;
            color: #fff;
            padding: 2rem 1rem 1rem 1rem;
            border-radius: 8px;
            margin-bottom: 2rem;
        }
        .company-logo {
            width: 180px;
            margin-bottom: 1rem;
        }
        .company-title {
            font-size: 2.2rem;
            font-weight: bold;
            letter-spacing: 1px;
        }
        .company-desc {
            font-size: 1.1rem;
            margin-bottom: 0.5rem;
        }
        .stButton>button {
            background-color: #003366;
            color: #fff;
            font-weight: bold;
            border-radius: 5px;
        }
        .stTable {
            background-color: #fff;
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Encabezado de empresa ---
# CSS personalizado
st.markdown("""
    <style>
        /* Fondo del formulario */
        div[data-testid="stForm"] {
            background-color: #e6f0fa;
            padding: 2rem 2rem 1rem 2rem;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
            border: 1px solid #b3c6e0;
        }
        /* Botón del formulario */
        .stButton>button {
            background-color: #003366;
            color: #fff;
            font-weight: bold;
            border-radius: 6px;
            padding: 0.5rem 2rem;
            border: none;
        }
        /* Etiquetas de los campos */
        label {
            color: #003366 !important;
            font-weight: 600;
        }
        /* Cambia el ancho de la tabla */
        [data-testid="stTable"] {
            width: 100% !important;
            max-width: 500px;
            margin-left: auto;
            margin-right: auto;
        } 
        /* Cambia el ancho de los campos del formulario */
        .stNumberInput, .stSelectbox, .stTextInput {
            width: 100% !important;
            max-width: 250px;
        }
        /* Opcional: centra el formulario */
        div[data-testid="stForm"] {
            max-width: 650px;
            margin-left: auto;      
            margin-right: auto;
        }                       
    </style>
    <div class="company-header">
        <img src="https://www.grupotransportadorlogipex.com/wp-content/uploads/2021/03/logo-logipex.png" class="company-logo" />
        <div class="company-title">GRUPO TRANSPORTADOR LOGIPEX</div>
        <div class="company-desc">
            Especialistas en transporte de carga extra dimensionada y extra pesada.<br>
            <a href="http://www.grupotransportadorlogipex.com" style="color:#ffcc00;" target="_blank">www.grupotransportadorlogipex.com</a>
        </div>
    </div>            
""", unsafe_allow_html=True)

with st.form("mi_formulario"):
    st.text_input("Campo de ejemplo")
    st.number_input("Otro campo")
    st.form_submit_button("Enviar")
    

st.title("Formulario de Plan de Izaje")

with st.form("izaje_form"):
    peso_carga = st.number_input("Peso de carga (kg)", min_value=0.0, step=100.0)
    largo_carga = st.number_input("Largo de carga (m)", min_value=0.0, step=0.1)
    forma_carga = st.selectbox("Forma de carga", ["cilindro", "rectangular", "otro"])
    angulo_slingas = st.number_input("Ángulo slingas (grados)", min_value=0.0, max_value=90.0, step=1.0)
    distancia_horizontal = st.number_input("Distancia horizontal (m)", min_value=0.0, step=0.1)
    altura_izaje = st.number_input("Altura de izaje (m)", min_value=0.0, step=0.1)
    submitted = st.form_submit_button("Procesar")

if submitted:
    datos = {
        "peso_carga_kg": peso_carga,
        "largo_carga_m": largo_carga,
        "forma_carga": forma_carga,
        "angulo_slingas_deg": angulo_slingas,
        "distancia_horizontal_m": distancia_horizontal,
        "altura_izaje_m": altura_izaje
    }
    resultado = motor.motor_izaje(datos)
    st.write("### Plan de Izaje")
    st.table(pd.DataFrame([resultado]))