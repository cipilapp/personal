import streamlit as st
import pandas as pd
import motor
import re

# Cargar estilos de la pagina base
#with open("estilos/estilosSimulador.css") as formStyles:
#    st.markdown(f"<style>{formStyles.read()}</style>", unsafe_allow_html=True)

# Cargar estilos desde el archivo externo
#with open("estilos/mainStyles.css") as mainStyles:
#    st.markdown(f"<style>{mainStyles.read()}</style>", unsafe_allow_html=True)


# --- Encabezado de empresa ---
# Muestra el logo con st.image
#st.image("img/logo.jpg", width=180)



# --- ESTILOS BÁSICOS ---
st.markdown("""
<style>
body, .stApp {
    background-color: #161616;
    color: #bdd5ed;
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
}
h1, h2, h3, h4 {
    color: #bdd5ed;
    font-family: 'League Spartan', Arial, sans-serif;
}
.stButton>button {
    background-color: #bdd5ed;
    color: #161616;
    border-radius: 4px;
    font-weight: bold;
}
.stButton>button:hover {
    background-color: #7b97b2;
    color: #fff;
}
a {
    color: #ffcc00;
}
hr {
    border: 1px solid #bdd5ed;
}
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("""
<div style="display:flex;align-items:center;gap:2rem;margin-bottom:1.5rem;">
    <img src="https://www.grupotransportadorlogipex.com/wp-content/uploads/2021/03/logo-logipex.png" width="110" style="background:#fff;border-radius:8px;padding:8px;">
    <div>
        <h1 style="margin-bottom:0.2rem;">Grupo de Logística Internacional de Pesados y Extradimensionados</h1>
        <span style="color:#fff;">Transporte Internacional de Cargas Pesadas y Extra Dimensionadas</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center; margin-bottom:2rem;">
    <span style="font-size:1.2rem; color:#7b97b2;">
        Soluciones logísticas seguras y eficientes para tu carga.<br>
        <a href="http://www.grupotransportadorlogipex.com" target="_blank">www.grupotransportadorlogipex.com</a>
    </span>
</div>
""", unsafe_allow_html=True)

# --- SOBRE NOSOTROS ---
st.markdown("---")
st.markdown("## Sobre Nosotros")
st.markdown("""
<div style="display:flex;gap:2rem;flex-wrap:wrap;">
    <img src="https://img1.wsimg.com/isteam/getty/2025407654/:/cr=t:4.9%25,l:0%25,w:100%25,h:90.2%25/rs=w:400,h:200,cg:true" width="320" style="border-radius:8px;">
    <div style="flex:1;min-width:220px;">
        <h4>Nuestra Historia</h4>
        <p style="color:#fff;">
        Con más de 45 años de experiencia, somos líderes en el sector de la logística y el transporte. Nos especializamos en proyectos de ingeniería integral en energía, construcción, exportaciones e importaciones.<br><br>
        Todas nuestras operaciones son 100% seguras y cuentan con aseguramiento de hasta 20.000 millones de pesos en infraestructura vial y póliza de mercancía hasta por 1.500 millones.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# --- SERVICIOS ---
st.markdown("---")
st.markdown("## Servicios Ofrecidos")
st.markdown("""
<div style="display:flex;gap:2rem;flex-wrap:wrap;">
    <img src="https://img1.wsimg.com/isteam/getty/1449484368/:/cr=t:0%25,l:2.29%25,w:95.41%25,h:100%25/rs=w:400,h:200,cg:true" width="320" style="border-radius:8px;">
    <div style="flex:1;min-width:220px;">
        <h4>Soluciones de Transporte y Logística</h4>
        <p style="color:#fff;">
        Ofrecemos transporte de cargas pesadas y extradimensionadas, OTM, DTA, DTAI, izaje con grúas hasta 500 tons y más.<br>
        Modalidades: tractomulas, patinetas, cama bajas, modulares, exportación/importación, y gestión portuaria.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)




# fromulario personalizado

with st.form("mi_formulario"):
    st.text_input("Campo de ejemplo")
    st.number_input("Otro campo")
    st.form_submit_button("Enviar")
    

st.title("Formulario de Plan de Izaje")

with st.form("izaje_form"):
    peso_carga = st.number_input("Peso de carga (kg)", min_value=0)
    largo_carga = st.number_input("Largo de carga (m)", min_value=0.0, step=0.1)
    forma_carga = st.selectbox("Forma de carga", ["cilindro", "rectangular", "otro"])
    angulo_slingas = st.number_input("Ángulo slingas (grados)", min_value=0.0, max_value=90.0, step=1.0)
    distancia_horizontal = st.number_input("Distancia horizontal (m)", min_value=0.0, step=0.1)
    altura_izaje = st.number_input("Altura de izaje (m)", min_value=0.0, step=0.1)
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

    resultado = motor.motor_izaje(datos)
    st.write("### Plan de Izaje")
    st.table(pd.DataFrame([resultado]))


    # --- PIE DE PÁGINA ---
st.markdown("""
<hr>
<div style="text-align:center; color:#bdd5ed; font-size:0.9rem; margin-top:2rem;">
    Copyright © 2025 Grupo de Logistica Internacional de Pesados y Extradimensionados SAS - Todos los derechos reservados.<br>
    Email: contacto@grupologipex.com. Bogotá, Colombia
</div>
""", unsafe_allow_html=True)