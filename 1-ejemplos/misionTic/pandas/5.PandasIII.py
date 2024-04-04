import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv("GOT_episodes_v4.csv")

print(datos.head())

temporada1 = datos[datos["Season"]==1]

print(temporada1)

datos.plot(y="Rating")
plt.grid()
plt.savefig("ratingGOT.png",format="png")

datos["num_episodio"]=range(1,len(datos)+1)

print(datos)

datos.plot(kind="scatter",y="Rating", x="num_episodio")
plt.grid()
plt.savefig("rantingGOT2.png",format="png")

datos.plot(y="Votes")
plt.grid()
plt.savefig("votosGOT.png",format="png")