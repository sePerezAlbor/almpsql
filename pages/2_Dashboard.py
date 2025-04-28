import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# Conexión a la base de datos
usuario = "postgres"
contraseña = "aulad2024"  
host = "localhost"
puerto = "5432"
base_datos = "ventas_mundiales"

engine = create_engine(f"postgresql+psycopg2://{usuario}:{contraseña}@{host}:{puerto}/{base_datos}")


st.title('📊 Dashboard de Ventas por Región')

# 1. Dropdown para seleccionar región
@st.cache_data
def obtener_regiones():
    query = "SELECT DISTINCT region FROM ventas ORDER BY region;"
    regiones = pd.read_sql(query, engine)
    return regiones['region'].tolist()

regiones = obtener_regiones()

region_seleccionada = st.selectbox('Selecciona una Región:', regiones)

# 2. Consulta SQL para ventas mensuales en la región seleccionada
@st.cache_data
def obtener_ventas(region):
    query = """
        SELECT EXTRACT(MONTH FROM fecha_venta) AS mes,
               SUM(monto_venta) AS total_mensual
        FROM ventas
        WHERE region = %s
        GROUP BY mes
        ORDER BY mes;
    """
    df = pd.read_sql(query, engine, params=(region,))
    return df

df_ventas = obtener_ventas(region_seleccionada)

# 3. Gráfico de ventas mensuales
st.subheader(f'Evolución Mensual de Ventas en {region_seleccionada}')
fig = px.line(df_ventas, 
              x='mes', 
              y='total_mensual', 
              markers=True,
              labels={'mes': 'Mes', 'total_mensual': 'Total de Ventas'},
              title=f'Evolución Mensual de Ventas en {region_seleccionada}',
              line_shape='linear')


fig.update_traces(line=dict(color='green'))

fig.update_layout(xaxis=dict(tickmode='linear', tick0=1, dtick=1))  

st.plotly_chart(fig, use_container_width=True)
