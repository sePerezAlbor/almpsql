import streamlit as st
from streamlit_option_menu import option_menu

# Configuración de la página
st.set_page_config(page_title="Dashboard Ventas Internacionales", layout="wide")

with st.sidebar:
    selected = option_menu("Menú", ["Inicio", "Dashboard", "Ventas por Producto"],
        icons=["house", "bar-chart", "box"], menu_icon="cast", default_index=0)

if selected == "Inicio":
    st.title("Dashboard Ventas Internacionales")
elif selected == "Dashboard":
    st.switch_page("pages/2_Dashboard.py")
elif selected == "Ventas por Producto":
    st.switch_page("pages/3_Producto.py")
