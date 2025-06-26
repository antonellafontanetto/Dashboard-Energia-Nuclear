# components/panel4.py

import streamlit as st
import plotly.express as px
from data_loader import load_data

def show_panel4():
    st.header("⚛️ Distribución Global por Tipo de Reactor")

    df = load_data()

    # Agrupar por tipo de reactor
    type_counts = df["Reactor Type"].value_counts().reset_index()
    type_counts.columns = ["Reactor Type", "Cantidad"]

    # Selector de tipo de gráfico
    chart_type = st.radio("Seleccioná tipo de gráfico:", ["Torta", "Barras"], horizontal=True)

    if chart_type == "Torta":
        fig = px.pie(type_counts,
                     names="Reactor Type",
                     values="Cantidad",
                     title="Distribución Global por Tipo de Reactor",
                     hole=0.4)  # dona opcional
    else:
        fig = px.bar(type_counts,
                     x="Reactor Type",
                     y="Cantidad",
                     title="Cantidad de Reactores por Tipo",
                     text="Cantidad")
        fig.update_traces(textposition='outside')
        fig.update_layout(xaxis_tickangle=-45)

    st.plotly_chart(fig, use_container_width=True)


