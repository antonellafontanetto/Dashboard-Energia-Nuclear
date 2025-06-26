# kpi_cards.py

# kpi_cards.py
import streamlit as st
from data_loader import load_data

def get_kpi_cards():
    df = load_data()
    
    total_reactors = len(df)
    total_capacity_mw = df['Capacity (MW)'].sum()
    latest_year = df['Year'].max()
    return total_reactors, total_capacity_mw, latest_year

def show_kpi_cards():
    total, capacity, latest = get_kpi_cards()

    st.markdown(f"""
        <style>
        .kpi-container {{
            display: flex;
            justify-content: space-around;
            margin-top: 20px;
            margin-bottom: 20px;
        }}
        .kpi-box {{
            background-color: #ffffff;
            border: 2px solid #eeeeee;
            border-radius: 12px;
            padding: 20px;
            width: 30%;
            text-align: center;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.05);
        }}
        .kpi-title {{
            font-size: 20px;
            color: #333;
            font-weight: 600;
        }}
        .kpi-value {{
            font-size: 36px;
            color: #0072B2;
            font-weight: bold;
            margin-top: 10px;
        }}
        </style>

        <div class="kpi-container">
            <div class="kpi-box">
                <div class="kpi-title">Total de Reactores</div>
                <div class="kpi-value">{total}</div>
            </div>
            <div class="kpi-box">
                <div class="kpi-title">Capacidad Total (MW)</div>
                <div class="kpi-value">{int(capacity):,}</div>
            </div>
            <div class="kpi-box">
                <div class="kpi-title">Último Año de Actualización</div>
                <div class="kpi-value">{int(latest)}</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Si querés probar el archivo por separado
if __name__ == "__main__":
    show_kpi_cards()
