import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

# Establecer la conexión con la base de datos MySQL de forma segura usando un contexto with
with create_engine('mysql://root@localhost/peps2').connect() as engine:
    # Leer el archivo Excel
    #df = pd.read_excel('/home/cootep/Downloads/peps.xlsx')
    df = pd.read_excel('/home/cootep/Downloads/familiares.xlsx')
    
    
    # Escribir en la base de datos MySQL sin reemplazar la tabla existente
    try:
        #df.to_sql(name='personas_personapep', con=engine, if_exists='append', index=False)
        df.to_sql(name='personas_familiar', con=engine, if_exists='append', index=False)
        print("Datos insertados correctamente en la tabla de la base de datos.")
    except Exception as e:
        print("Error al insertar datos:", e)