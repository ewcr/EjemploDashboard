import streamlit as st
from auth import verificar_acceso

# Llamamos a la seguridad antes de mostrar nada
verificar_acceso()

st.title("📊 Panel de Control")
st.write("Si puedes ver esto, es porque estás logeado.")
# Aquí irían tus gráficas y datos...