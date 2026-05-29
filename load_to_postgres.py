import pandas as pd
from sqlalchemy import create_engine

# leer csv
df = pd.read_csv("data/sales_data_powerbi.csv", sep=";")

from datetime import datetime

# Crear columna con fecha/hora de carga
df['load_time'] = datetime.now()

# conexión postgres
engine = create_engine(
    "postgresql+psycopg2://postgres:1234@localhost:5432/bike_sales_db"
)

# subir tabla
df.to_sql(
    "sales_data",
    engine,
    if_exists="replace",
    index=False
)

print("Datos cargados correctamente 🚀")