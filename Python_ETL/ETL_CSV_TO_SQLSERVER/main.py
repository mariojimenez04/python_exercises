import pandas as pd
import os
from sqlalchemy import *
from sqlalchemy.types import *

server = os.getenv('DB_HOST_STG')
db_user = os.getenv('DB_USER_STG')
db_pass = os.getenv('DB_PASS_STG')
db = os.getenv('DB_DATABASE_STG')

ruta_csv = 'C:/Users/e-mario_jimenez/Downloads/SQ01 INVENTORY.csv'

db_table = os.getenv('DB_TABLE_STG')

df = pd.read_csv(ruta_csv)

print("Tipos de datos originales:")
print(df.dtypes)

# for columna in df.columns:
#     if 'fecha' in columna.lower():
#         df[columna] = pd.to_datetime(df[columna], errors='coerce')
#     elif df[columna].dtype == 'object':
#         df[columna] = df[columna].astype(str)
#     elif df[columna].dtype == 'float64':
#         df[columna] = df[columna].astype(float)

conexion = f'mssql+pyodbc://{db_user}:{db_pass}@{server}/{db}?driver=ODBC+Driver+17+for+SQL+Server'
engine = create_engine(conexion)
meta = MetaData()

with engine.connect() as conection:
    if not engine.has_table(db_table):
        print(f"\nLa tabla {db_table} no existe, creando...")
        
        columnas = [column('id', Integer, primary_key=True, autoincrement=True)]
        for columna, tipo in df.dtypes.items():
            if tipo == 'int64':
                columnas.append(Column(columna, Integer))
            elif tipo == 'float64':
                columnas.append(Column(columna, Float))
            elif tipo == 'datetime64[ns]':
                columnas.append(Column(columna, DateTime))
            else:
                columnas.append(Column(columna, String(255)))
        tabla = Table(db_table, meta, *columnas)
        meta.create_all(engine)
        print(f"\nTabla '{db_table}' creada exitosamente")
    else:
        print(f"\nLa tabla '{db_table}' ya existe, insertando datos")


df.to_sql(name=db_table, con=engine, if_exists='append', index=False)

print('\nDatos cargados en la tabla correctamente')