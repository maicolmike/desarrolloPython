import matplotlib.pyplot as plt


x = ["Niños","Niñas","Mujeres","Hombres"]

y = [10,12,23,12]

plt.pie(y,labels=x,explode=[0,0,0.1,0],shadow=True,autopct="%1.2f%%")
plt.show()