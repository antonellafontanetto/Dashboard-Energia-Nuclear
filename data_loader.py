# utils/data_loader.py
import pandas as pd

def load_data(filepath="C:/Users/antob/Documents/Nuclear_dashboard/data/reactores_nucleares.xlsx"):
    df = pd.read_excel(filepath, sheet_name='Data')
    # resto del código...

    # Convertir columnas de fecha
    df['First Grid Connection'] = pd.to_datetime(df['First Grid Connection'], errors='coerce')

    # Agregar columna de año
    df['Year'] = df['First Grid Connection'].dt.year

    # Filtrar filas útiles
    df = df[df['Capacity (MW)'].notna()]
    
    return df

