import math
def estudio_credito(prestamos:list)->list:
  final=[]
  x=0
  y=0
  w=0
  p=0
  for j,i in prestamos:
    dic_valores = {
							"valor_cuota":0,
							"valor_total":0
    }		
    if i<=12:
       w=(0.035)
       x=(j*(1+w*i)/i)#/(len(prestamos))
       y=(j*(1+w*i))#/(len(prestamos))
       
    elif 12<i<=24:
       w=(0.030)
       x=(j*(1+w*i)/i)#/(len(prestamos))
       y=(j*(1+w*i))#/(len(prestamos))
       
    elif 24<i<=36:
       w=(0.023)
       x=(j*(1+w*i)/i)#/(len(prestamos))
       y=(j*(1+w*i))#/(len(prestamos))
       
    elif 36<i<=60:
       w=(0.018)
       x=(j*(1+w*i)/i)#/(len(prestamos))
       y=(j*(1+w*i))#/(len(prestamos))
       
    elif i>60:
       w=(0.010)
       x=(j*(1+w*i)/i)#/(len(prestamos))
       y=(j*(1+w*i))#/(len(prestamos))

    for elm in prestamos:
       dic_valores["valor_cuota"]+=math.ceil(x)
       dic_valores["valor_total"]+=math.ceil(y)
    final.append(dic_valores)
  return final
print()
print()
print()
print()

print(estudio_credito([(50000000,24), (50000000,65), (24000000,48)]))
#print(estudio_credito([(1000000, 24), (5000000, 36), (2500000, 50)]))