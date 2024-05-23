import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime


# Definir las columnas que pueden contener valores nulos
nullable_columns = ['nombre', 'identificacion', 'es_pep', 'estado', 'tipo_pep',
                    'cargo', 'fecha_vinculacion', 'fecha_desvinculacion',
                    'cuentas_extranjeras', 'fecha_registro_pep', 'fecha_actualizacion']

# Definir el valor predeterminado para llenar los valores nulos en las columnas de fecha
default_date = datetime.now()

# Establecer la conexión con la base de datos MySQL de forma segura usando un contexto with
with create_engine('mysql://root@localhost/peps3').connect() as engine:
    # Leer el archivo Excel
    df = pd.read_excel('/home/cootep/Downloads/peps.xlsx')
    
    # Llenar los valores nulos en las columnas especificadas
    for column in nullable_columns:
        if column in df.columns:
            if df[column].dtype == 'datetime64[ns]':
                df[column] = df[column].fillna(default_date)
            else:
                df[column] = df[column].fillna('')
    
    # Escribir en la base de datos MySQL sin reemplazar la tabla existente
    try:
        df.to_sql(name='personas_personapep', con=engine, if_exists='append', index=False)
        print("Datos insertados correctamente en la tabla de la base de datos.")
    except Exception as e:
        print("Error al insertar datos:", e)