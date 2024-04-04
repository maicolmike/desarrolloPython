import pandas as pd
import matplotlib.pyplot as plt

datos = {
	"fruta":["Mango","Uva","Papaya","Zapayo"],
	"calorias":[10,20,40,80]
}

df = pd.DataFrame(datos)
print(df)

df.plot(x="fruta")
plt.savefig("figura1.jpg",format="jpg")

df.plot(kind="scatter",x="fruta",y="calorias")
plt.savefig("figura2.jpg",format="jpg")

diccionario_violento={
	"nombre":["Carlos","Juan","Paola","Maria","Claudia"],
	"edad":[33,18,33,33,18]
}

df2 = pd.DataFrame(diccionario_violento)
df2.plot(kind="hist")
plt.savefig("figura3.jpg",format="jpg")

nombres = df2["nombre"].values

df2.plot(kind="bar",x="nombre",y="edad")
plt.tight_layout()
plt.savefig("figura4.jpg",format="jpg")
