'''
Instrucciones de uso

se debe poner el archivo


'''


#pip install pandas openpyxl
import pandas as pd

# Cargar el archivo Excel
#file_path = 'C:\Users\COOTEP\Documents\cuentas.xlsx'  # Reemplaza con la ruta a tu archivo Excel
file_path = 'C:/Users/COOTEP/Documents/asociados.xlsx'
df = pd.read_excel(file_path)

# Asegurarse de que el DataFrame contiene una columna con las cuentas
# Supongamos que la columna se llama 'A_NUMCTA'
if 'aanumnit' in df.columns:
    cedulas = df['aanumnit'].astype(str).tolist()
else:
    raise ValueError("La columna 'aanumnit' no se encuentra en el archivo Excel.")

# Generar el script SQL
cedulas_str = "',\n'".join(cedulas)
sql_script = f"""
UPDATE info_terceros SET ESTADO = 'I'
WHERE aanumnit IN(
'{cedulas_str}'
)
"""

# Guardar el script SQL en un archivo
with open('estado_asociados.sql', 'w') as file:
    file.write(sql_script)

print("El script SQL se ha generado y guardado en 'script.sql'.")
