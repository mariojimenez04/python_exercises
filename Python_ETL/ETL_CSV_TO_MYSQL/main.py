import csv
import logging
import pandas as pd
from sqlalchemy import create_engine as ce
from connect.sql import *
import os

csv_route = 'C:/Users/e-mario_jimenez/Downloads/TEST.csv'

user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
db = os.getenv('DB_DATABASE')
table = os.getenv('DB_TABLE')

df = pd.read_csv(csv_route)

print(df.shape)
print(df)

conexion = f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}'
engine = create_engine(conexion)
# with engine.connect() as conexion:
#     print("Conexion exitosa")

# logging.basicConfig()
# logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

df.to_sql(name=table, con=engine, if_exists='replace', index=False)

print(f"Datos cargados en la tabla '{table}' correctamente.")

