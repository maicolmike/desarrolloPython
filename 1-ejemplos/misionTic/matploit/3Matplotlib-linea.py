import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10]

y_1 = []
y_2 = []

for elm in x:
	y_1.append(2*elm)
	y_2.append(elm**2)

print(y_1)
print(y_2)

plt.plot(x,y_1,color="red",label="2x")
plt.plot(x,y_2,color="blue",label="x^2")
plt.legend()
plt.grid()
plt.show()