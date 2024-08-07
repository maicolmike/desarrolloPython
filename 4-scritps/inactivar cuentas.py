'''
Instrucciones de uso

se debe poner el archivo


'''


#pip install pandas openpyxl
import pandas as pd

# Cargar el archivo Excel
#file_path = 'C:\Users\COOTEP\Documents\cuentas.xlsx'  # Reemplaza con la ruta a tu archivo Excel
file_path = 'C:/Users/COOTEP/Documents/cuentas.xlsx'
df = pd.read_excel(file_path)

# Asegurarse de que el DataFrame contiene una columna con las cuentas
# Supongamos que la columna se llama 'A_NUMCTA'
if 'A_NUMCTA' in df.columns:
    cuentas = df['A_NUMCTA'].astype(str).tolist()
else:
    raise ValueError("La columna 'A_NUMCTA' no se encuentra en el archivo Excel.")

# Generar el script SQL
cuentas_str = "',\n'".join(cuentas)
sql_script = f"""
UPDATE AH136MCUENTA SET I_ESTADO = 'I'
WHERE A_NUMCTA IN(
'{cuentas_str}'
)
"""

# Guardar el script SQL en un archivo
with open('inactivar_cuentas.sql', 'w') as file:
    file.write(sql_script)

print("El script SQL se ha generado y guardado en 'script.sql'.")
