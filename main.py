# python -m pip install --upgrade pip
# pip install streamlit pyinstaller
# streamlit run main.py

import streamlit as st

# 2. Función de validación (Simulada)
def validar_usuario(usuario, clave):
    # En el futuro, aquí podrías consultar una base de datos
    return usuario == "admin" and clave == "1234"

def main():
    # 1. Configuración de la página (esto debe ir primero)
    st.set_page_config(page_title="Mi App Segura", layout="centered")

    # 2. Inicializar el estado de la sesión
    if "logeado" not in st.session_state:
        st.session_state.logeado = False

    # 3. Lógica de Login
    if not st.session_state.logeado:
        # Creamos 3 columnas: [vacía, formulario, vacía]
        # El ratio 1:2:1 hace que la del medio sea más ancha y esté centrada
        izq, centro, der = st.columns([1, 2, 1])
        
        with centro:
            st.title("🔐 Login")
            
            # Usamos un formulario para agrupar los inputs
            with st.form("formulario_login"):
                usuario = st.text_input("Usuario 👤")
                clave = st.text_input("Contraseña 🔑", type="password")
                boton_enviar = st.form_submit_button("Entrar")
                
                if boton_enviar:
                    if usuario == "admin" and clave == "1234":
                        st.session_state.logeado = True
                        st.rerun()
                    else:
                        st.error("Credenciales incorrectas ❌")
    else:
        # Botón para salir en la barra lateral
        st.sidebar.button("Cerrar Sesión", on_click=lambda: st.session_state.update({"logeado": False}))
        
        st.title("🚀 Bienvenido a la App")
        st.write("Ahora puedes navegar por las páginas del menú lateral.")

if __name__ == "__main__":
    main()
