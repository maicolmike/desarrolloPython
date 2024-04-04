import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(0,100,1000)

b = [0,10,20,30,40,50,60,70,80,90,100]

plt.figure(dpi=200)
plt.hist(x,bins=b,color="blue")
plt.title("Cantidad de números")
plt.xlabel("Números")
plt.ylabel("Cantidad")
plt.grid()
plt.savefig("figura.png",format="png")