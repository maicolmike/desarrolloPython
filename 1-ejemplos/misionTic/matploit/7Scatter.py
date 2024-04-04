import matplotlib.pyplot as plt

x = [0,1,2,3,4,5,6]
y = [2,3,4,5,1,3,4]
x2 = [3,5,6,7,8,0,-1]
y2 = [5,2,3,1,0,4,5]

plt.figure(dpi=300)
plt.scatter(x,y,color="blue",label="relación x vs y")
plt.scatter(x2,y2,color="red",label=r"relación $x_2$  vs $y_2$")
plt.grid()
plt.xlabel("Temperatura")
plt.ylabel("Presión")
plt.title(r"Relación $\Theta^2$ y $\sum_{n=0}^n 2^n$")
plt.legend();
plt.savefig("imagen.png",format="png")