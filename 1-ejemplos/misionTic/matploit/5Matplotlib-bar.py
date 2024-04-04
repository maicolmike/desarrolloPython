import matplotlib.pyplot as plt

plt.figure(dpi=300)

x=["Gatos","Perros","Lobos","Zorros"]
y = [10,12,9,2]

plt.bar(x,height=y)
plt.savefig("figura.png",format="png")