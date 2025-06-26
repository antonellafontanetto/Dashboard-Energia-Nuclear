# app.py

import streamlit as st
from kpi_cards import get_kpi_cards
from components import panel1, panel2, panel3, panel4

# Configuración de página
st.set_page_config(page_title="Dashboard Energía Nuclear", layout="wide")

# Título principal
st.title("🌐 Dashboard de Reactores Nucleares")

# Mostrar KPIs
from kpi_cards import show_kpi_cards
show_kpi_cards()

st.markdown("")

# Paneles seleccionables
panel = st.sidebar.radio("Seleccionar panel", ["Panel 1", "Panel 2", "Panel 3", "Panel 4"])

if panel == "Panel 1":
    panel1.show_panel1()
elif panel == "Panel 2":
    panel2.show_panel2()
elif panel == "Panel 3":
    panel3.show_panel3()
elif panel == "Panel 4":
    panel4.show_panel4()
