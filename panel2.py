# components/panel2.py

import streamlit as st
import plotly.express as px
from data_loader import load_data

def show_panel2():
    st.header("🗺️ Mapa Mundial de Reactores Nucleares")

    df = load_data()
    df = df.dropna(subset=["Latitude", "Longitude"])

    fig = px.scatter_geo(
        df,
        lat="Latitude",
        lon="Longitude",
        hover_name="Project Name",
        hover_data={"Country/Area": True, "Capacity (MW)": True},
        size="Capacity (MW)",
        color="Country/Area",
        title="Ubicación de Reactores Nucleares en el Mundo",
        projection="natural earth"
    )

    fig.update_layout(
        height=700,
        margin={"r":0,"t":50,"l":0,"b":0},
        paper_bgcolor='#4B5320',   # Verde militar para todo el fondo
        font=dict(color='white'),  # Texto en blanco para contraste (títulos, hover)
        geo=dict(
            bgcolor='#4B5320',  # Verde militar para el fondo del mapa
            showland=True,
            landcolor='#556B2F',  # Verde oliva oscuro para tierra
            showocean=True,
            oceancolor='#3B5323',  # Verde militar un poco distinto para océanos
            showlakes=True,
            lakecolor='#2E4A1F',  # Verde oscuro para lagos
            showcountries=True,
            countrycolor='white',  # Bordes de países en blanco para resaltar
            showcoastlines=True,
            coastlinecolor='white',
            showframe=False,
            showrivers=True,
            rivercolor='white',
            countrywidth=1,
            coastlinewidth=1,
            riverwidth=1,
            lataxis=dict(
                showgrid=True,
                gridcolor='white',
                dtick=10,
                tick0=0
            ),
            lonaxis=dict(
                showgrid=True,
                gridcolor='white',
                dtick=10,
                tick0=0
            ),
        )
    )

    st.plotly_chart(fig, use_container_width=True)
