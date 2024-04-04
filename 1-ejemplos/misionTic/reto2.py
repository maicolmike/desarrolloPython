### Implementar las funciones del ejercicio de la puerta
""" REto 2 Puerta del Castillo #
    Michael yela valencia
    Mayo 23-2021 """
# DefiniciÃ³n de Funciones
# Pruebas automÃ¡ticas
import math as md

#Usar este valor de PI para los calculos
PI = md.pi

def cantidad_vueltas_cierra(largom, dpoleacm):
  """ Parameter
      --------
      largom
        type:int 
        description:operando largo puerta del castillo en metros
      
      rpoleacm:
      type:int
      description:Diametro de la polea en centÃ­metros 

      Returns:
      ----------
      cantidad_vueltas
      type:int
      description:  Cantidad de vueltas que debe dar la polea  para abrir la 
       Parameters
      ---------- 
  """
  altura_muro=largom 
  longitud_cuerda=round(md.sqrt(largom**2+altura_muro**2),3)#con la funcion round redondeo a 3 decimales
  longitud_cuerda_cm= round(longitud_cuerda*100,3)
  longitud_circulo=round(PI*dpoleacm,3)
  numero_vueltas_polea= round(longitud_cuerda_cm/longitud_circulo,3)
  return numero_vueltas_polea


def cantidad_chewebacas(largom, dpoleacm):
  """ Parameter
      --------
      largom
        type:int 
        description:operando largo puerta del castillo en metros
      
      rpoleacm:
      type:int
      description:Diametro de la polea en centÃ­metros 

      Returns:
      ----------
      cantidad_chewebacas
      type:int
      description:  Cantidad de chewebacas  para abrir la puerta
       Parameters
      ---------- 
      Suggestions:
      Trate de usar la funciÃ³n que determina la cantidad de vueltas Para abrir la puerta, sÃ³lo un chewebacas puede dar 3 giros (El valor debe ser la cantidad entera )
  """ 
  altura_muro=largom 
  longitud_cuerda=round(md.sqrt(largom**2+altura_muro**2),3)#con la funcion round redondeo a 3 decimales
  longitud_cuerda_cm= round(longitud_cuerda*100,3)
  longitud_circulo=round(PI*dpoleacm,3)
  numero_vueltas_polea= round(longitud_cuerda_cm/longitud_circulo,3)
  numero_chewbaccas= numero_vueltas_polea//3
  return numero_chewbaccas
def velocidad_cerrar_puerta_min(largom, rpoleacm, minutoss ):
  """ Parameter
      --------
      largom
        type:int 
        description:operando largo puerta del castillo en metros
      
      rpoleacm:
      type:int
      description:Radio de la polea en centÃ­metros 

      minutos:
      type:int
      description:cantidad limite minutos para cerrar la puerta, 

      Returns:
      ----------
      velocidad_cierra
      type:int
      description:  velocidad en cm/seg para girar la polea 
       Parameters
      ---------- 
      Suggestions:
      Tener en cuenta la fÃ³rmula de Velocidad=espacio/tiempo
  """
  altura_muro=largom 
  longitud_cuerda=round(md.sqrt(largom**2+altura_muro**2),3)#con la funcion round redondeo a 3 decimales
  dpoleacm=rpoleacm
  longitud_cuerda_cm= round(longitud_cuerda*100,3)
  longitud_circulo=round(PI*dpoleacm,3)
  numero_max_seg=minutoss*60
  velocidad_cierre_puerta= longitud_cuerda_cm/numero_max_seg
  return velocidad_cierre_puerta 
#final de la funcion 

# inico de la aplicacion  
largom=int(input("digite por favor el largo de puerta en metros:"))
dpoleacm=int(input("digite por favor el diametro de la polea en cm:"))
minutoss=int(input("digite por favor la velocidad maxima en minutos del cierre de la puerta:"))
rpoleacm=dpoleacm

cantidad_vueltas=cantidad_vueltas_cierra(largom,dpoleacm)
cantidad_che=cantidad_chewebacas(largom, dpoleacm)
velocidad=velocidad_cerrar_puerta_min(largom, rpoleacm, minutoss )
print("la cantidad de vueltas es",cantidad_vueltas)
print("la cantidad de chewebaccas es",cantidad_che)
print("la cantidad de velocidad es",velocidad)