# components/panel1.py

import streamlit as st
import plotly.express as px
from data_loader import load_data

def show_panel1():
    st.header("📊 Evolución de Reactores y Potencia Instalada")
    
    df = load_data()

    # Agrupar cantidad de proyectos por año usando 'Project Name'
    projects_per_year = df.groupby("Year")['Project Name'].count().reset_index()
    projects_per_year.rename(columns={'Project Name': 'Projects Count'}, inplace=True)

    # Agrupar capacidad MW total por año
    capacity_per_year = df.groupby("Year")['Capacity (MW)'].sum().reset_index()

    # Gráfico 1: Evolución de proyectos por año (línea con markers)
    fig1 = px.line(
        projects_per_year, x='Year', y='Projects Count', 
        title='Evolución de Proyectos por Año',
        markers=True,
        labels={'Year': 'Año', 'Projects Count': 'Cantidad de Proyectos'}
    )
    fig1.update_layout(template='plotly_white')

    # Gráfico 2: Evolución de potencia instalada (línea con área y markers)
    fig2 = px.area(
        capacity_per_year, x='Year', y='Capacity (MW)',
        title='Evolución de Potencia Instalada por Año',
        labels={'Year': 'Año', 'Capacity (MW)': 'Capacidad Total (MW)'},
        markers=True
    )
    fig2.update_traces(line_color='orange')
    fig2.update_layout(template='plotly_white')

    # Mostrar gráficos en Streamlit
    st.plotly_chart(fig1, use_container_width=True)
    st.plotly_chart(fig2, use_container_width=True)
