import pandas as pd
from sqlalchemy import create_engine

df = pd.read_excel("DATA_Q.xlsx")
print("Primeros registros del archivo:")
print(df.head())

usuario = "postgres"
contraseña = "aulad2024"  
host = "localhost"
puerto = "5432"
base_datos = "ventas_mundiales"

engine = create_engine(f"postgresql+psycopg2://{usuario}:{contraseña}@{host}:{puerto}/{base_datos}")
df.to_sql("ventas", engine, if_exists="replace", index=False)

print("\n Datos insertados correctamente en la tabla 'ventas' .")