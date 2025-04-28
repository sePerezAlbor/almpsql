import pandas as pd
from sqlalchemy import create_engine

usuario = "postgres"
contraseña = "aulad2024"  
host = "localhost"
puerto = "5432"
base_datos = "proyecto_accidentes_barranquilla"

engine = create_engine(f"postgresql+psycopg2://{usuario}:{contraseña}@{host}:{puerto}/{base_datos}")

query = "SELECT * FROM accidentes_barranquilla LIMIT 5;"
df = pd.read_sql(query, engine)

print(df)