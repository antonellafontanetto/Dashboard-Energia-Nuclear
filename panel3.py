# components/panel3.py

import streamlit as st
import plotly.express as px
from data_loader import load_data

def show_panel3():
    st.header("🌍 Análisis por País")
    
    df = load_data()

    # Dropdown con países únicos
    countries = sorted(df["Country/Area"].dropna().unique())
    selected_country = st.selectbox("Seleccioná un país:", countries)

    df_country = df[df["Country/Area"] == selected_country]

    # Gráfico de línea: capacidad instalada por año
    cap_by_year = df_country.groupby("Year")["Capacity (MW)"].sum().reset_index()

    fig_line = px.line(cap_by_year, x="Year", y="Capacity (MW)",
                       title=f"Evolución de Capacidad Instalada en {selected_country}",
                       markers=True)
    st.plotly_chart(fig_line, use_container_width=True)

    # Gráfico de barras: cantidad por tipo de reactor
    types = df_country["Reactor Type"].value_counts().reset_index()
    types.columns = ["Reactor Type", "Cantidad"]

    fig_bar = px.bar(types, x="Reactor Type", y="Cantidad",
                     title=f"Tipos de Reactores en {selected_country}",
                     text="Cantidad")
    fig_bar.update_traces(textposition='outside')
    st.plotly_chart(fig_bar, use_container_width=True)

