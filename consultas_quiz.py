import pandas as pd
from sqlalchemy import create_engine

usuario = "postgres"
contraseña = "aulad2024"  
host = "localhost"
puerto = "5432"
base_datos = "ventas_mundiales"

engine = create_engine(f"postgresql+psycopg2://{usuario}:{contraseña}@{host}:{puerto}/{base_datos}")

# Q1 Total de registros
print('--------- TOTAL DE REGISTROS ---------')
query = 'SELECT COUNT(*) AS total_registros FROM ventas;'
df = pd.read_sql(query, engine)
print(df)
print("")


# Q2 Región con más ventas
print('--------- Región con más ventas ---------')
query = '''
WITH cte AS (
    SELECT region, SUM(monto_venta) AS total_ventas
    FROM ventas
    GROUP BY region
)
SELECT * 
FROM cte
WHERE total_ventas = (SELECT MAX(total_ventas) FROM cte);
'''
df = pd.read_sql(query, engine)
print(df)
print(" ")


# Q3 Producto con mayor promedio de ventas en 2024
print('--------- Producto con mayor promedio de ventas en 2024 ---------')
query = '''
WITH cte AS (
    SELECT producto, AVG(monto_venta) AS promedio_ventas 
    FROM ventas v
    WHERE EXTRACT(YEAR FROM v.fecha_venta) = 2024
    GROUP BY v.producto
)
SELECT producto, ROUND(promedio_ventas, 2) AS promedio_ventas
FROM cte
WHERE promedio_ventas = (SELECT MAX(promedio_ventas) FROM cte);
'''
df = pd.read_sql(query, engine)
print(df)
print(" ")


# Q4 Cliente top 1 por región
print('--------- Cliente top 1 por región ---------')
query = '''
WITH cte AS (
    SELECT v.id_cliente, 
           v.region, 
           SUM(v.monto_venta) AS total_compras,
           DENSE_RANK() OVER (PARTITION BY v.region ORDER BY SUM(v.monto_venta) DESC) AS rank
    FROM ventas v
    GROUP BY v.id_cliente, v.region
)
SELECT id_cliente, region, total_compras
FROM cte
WHERE rank = 1;
'''
df = pd.read_sql(query, engine)
print(df)
print(" ")


# Q5 Mes con mayores ventas
print('--------- Mes con mayores ventas ---------')
query = '''
WITH cte AS (
    SELECT  
        EXTRACT(MONTH FROM fecha_venta) AS mes, 
        SUM(monto_venta) AS total_mensual
    FROM ventas
    GROUP BY EXTRACT(MONTH FROM fecha_venta)
)
SELECT * 
FROM cte 
WHERE total_mensual = (SELECT MAX(total_mensual) FROM cte);
'''
df = pd.read_sql(query, engine)
print(df)
