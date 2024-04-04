import cx_Oracle
#si se llega a presentar el ellor de falta Oracle Client library se pondria la siguiente linea de comando 
#cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle\instantclient_21_8") #descargar la libreria Oracle Client library y extraerla en una carpeta luego decirle donde deve enlazarse

try:
    connection=cx_Oracle.connect(
        user='LINIX',
        password= 'LNXPROD2022',
        dsn= '10.180.131.2:1521/LINIX',
        encoding = 'UTF-8'
    )
    print ('Conectado a Oracle Database',connection.version)
    cursor=connection.cursor()
    cursor.execute("select CLIENTE.AANUMNIT, (SELECT UNIQUE CG_REF_CODES.RV_MEANING FROM CG_REF_CODES WHERE CG_REF_CODES.RV_DOMAIN = 'DM_IDETER' AND CG_REF_CODES.RV_LOW_VALUE = TERCERO.I_IDETER)TIPO_DOCUM, CLIENTE.NNASOCIA, DIRECCION.T_TERCEL, SUCURSAL.N_SUCURS, CLIENTE.F_ULTAFI,CLIENTE.F_ULTACT, CLIENTE.I_ESTASO from AP014MCLIENTE CLIENTE, GR005MDIRECCIO DIRECCION, GR001MTERCERO TERCERO, GR021MSUCURSAL SUCURSAL where CLIENTE.K_IDTERC = TERCERO.K_IDTERC AND TERCERO.K_IDTERC = DIRECCION.K_IDTERC AND CLIENTE.K_SUCURS = SUCURSAL.K_SUCURS AND DIRECCION.I_TIPDIR= 'C' AND CLIENTE.I_ESTASO='A' AND SUCURSAL.N_SUCURS= 'Puerto Asis' AND CLIENTE.F_ULTACT between '30/01/2023'AND '31/01/2023' order by CLIENTE.F_ULTACT asc")
    rows=cursor.fetchall()
    for row in rows:
        print(row)
except Exception as ex:
    print('Error en la conexion a la base',ex)
finally:
    connection.close()
    print("Conexion finalizada")