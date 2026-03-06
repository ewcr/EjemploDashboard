import streamlit as st

def verificar_acceso():
    # Si no existe la variable o es False, detenemos todo
    if "logeado" not in st.session_state or not st.session_state.logeado:
        st.warning("⚠️ Por favor, inicia sesión para acceder a esta página.")
        st.info("Ve a la página principal para identificarte.")
        st.stop()  # Detiene la ejecución del script aquí mismo