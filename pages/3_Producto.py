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


st.title('📊 Ventas Mensuales de Producto por Región')

# 1. Dropdown para seleccionar región
@st.cache_data
def obtener_regiones():
    query = "SELECT DISTINCT region FROM ventas ORDER BY region;"
    regiones = pd.read_sql(query, engine)
    return regiones['region'].tolist()

regiones = obtener_regiones()

region_seleccionada = st.selectbox('Selecciona una Región:', regiones)

# 2. Dropdown para seleccionar producto
@st.cache_data
def obtener_productos(region):
    query = """
        SELECT DISTINCT producto
        FROM ventas
        WHERE region = %s
        ORDER BY producto;
    """
    productos = pd.read_sql(query, engine, params=(region,))
    return productos['producto'].tolist()

productos = obtener_productos(region_seleccionada)

producto_seleccionado = st.selectbox('Selecciona un Producto:', productos)

# 3. Consulta SQL para ventas mensuales del producto seleccionado
@st.cache_data
def obtener_ventas_producto(region, producto):
    query = """
        SELECT EXTRACT(MONTH FROM fecha_venta) AS mes,
               SUM(monto_venta) AS total_mensual
        FROM ventas
        WHERE region = %s AND producto = %s
        GROUP BY mes
        ORDER BY mes;
    """
    df = pd.read_sql(query, engine, params=(region, producto))
    return df

df_ventas_producto = obtener_ventas_producto(region_seleccionada, producto_seleccionado)

# 4. Gráfico de barras de ventas mensuales del producto
st.subheader(f'Evolución Mensual de Ventas de {producto_seleccionado} en {region_seleccionada}')

fig_producto = px.bar(df_ventas_producto, 
                      x='mes', 
                      y='total_mensual', 
                      labels={'mes': 'Mes', 'total_mensual': 'Total de Ventas'},
                      title=f'Ventas Mensuales de {producto_seleccionado} en {region_seleccionada}',
                      color='total_mensual',  
                      color_continuous_scale='Viridis'  
                     )

fig_producto.update_layout(xaxis=dict(tickmode='linear', tick0=1, dtick=1))  

st.plotly_chart(fig_producto, use_container_width=True)
