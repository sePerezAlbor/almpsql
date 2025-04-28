import pandas as pd
from sqlalchemy import create_engine

usuario = "postgres"
contraseña = "aulad2024"  
host = "localhost"
puerto = "5432"
base_datos = "proyecto_accidentes_barranquilla"

engine = create_engine(f"postgresql+psycopg2://{usuario}:{contraseña}@{host}:{puerto}/{base_datos}")


# Query 1 Total de registros 
print('--------- TOTAL DE REGISTROS ---------')
query = "SELECT COUNT(*) FROM accidentes_barranquilla;"
df = pd.read_sql(query, engine)
print(df)

# Query 2 Total de registro por "SEXO_VICTIMA" de la victima
print('--------- Total de registro por "SEXO_VICTIMA" de la victima ---------')
query = 'SELECT "SEXO_VICTIMA", COUNT("SEXO_VICTIMA") AS Total FROM accidentes_barranquilla GROUP BY "SEXO_VICTIMA";'
df = pd.read_sql(query, engine)
print(df)


#Query 3.1. Filtrar por año de accidente Fecha_Accidente
print('--------- Filtrar por año de accidente Fecha_Accidente ---------')
query = 'SELECT COUNT("Fecha_Accidente") AS Total FROM accidentes_barranquilla WHERE EXTRACT(YEAR FROM "Fecha_Accidente") = 2018;'
df = pd.read_sql(query, engine)
print(df)


#Query 3.2. Filtrar por año de accidente Fecha_Accidente
# print('--------- Filtrar por año de accidente Fecha_Accidente ---------')
# query = 'SELECT * FROM accidentes_barranquilla WHERE EXTRACT(YEAR FROM "Fecha_Accidente") == 2018;'
# df = pd.read_sql(query, engine)
# print(df)

#Query 4 Top 5 valores más frecuentes de "CONDICION_VICTIMA"
print('--------- Top 5 valores más frecuentes de "CONDICION_VICTIMA" ---------')
query = 'SELECT "CONDICION_VICTIMA", COUNT("CONDICION_VICTIMA") as total FROM accidentes_barranquilla GROUP BY "CONDICION_VICTIMA" ORDER BY COUNT("CONDICION_VICTIMA") DESC LIMIT 5;'
df = pd.read_sql(query, engine)
print(df)