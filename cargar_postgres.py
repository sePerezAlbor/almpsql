import pandas as pd
from sqlalchemy import create_engine


df = pd.read_csv("Accidentedes_Barranquilla_victimas.csv", encoding='utf-8', delimiter=",")  #Carga cualquier base de tu interés 
print("Primeros registros del archivo:")
print(df.head())


usuario = "postgres"
contraseña = "aulad2024"  
host = "localhost"
puerto = "5432"
base_datos = "proyecto_accidentes_barranquilla"


engine = create_engine(f"postgresql+psycopg2://{usuario}:{contraseña}@{host}:{puerto}/{base_datos}")


df.to_sql("accidentes_barranquilla", engine, if_exists="replace", index=False)
print("\n Datos insertados correctamente en la tabla 'accidentes_barranquilla' .")