import numpy as np

arregloA = np.array([1,2,3])
arregloB = np.array([[1,2,3],[3,4,5],[5,6,7]])

print(arregloA)
print(arregloB)

print(np.sum(arregloA))

print(np.dot(arregloB,arregloB))

"""
3x + 2y - 5z = 3
8x - 3y + 6z = 9
7x - 4y + 9z = 18
"""

a = np.array(
	[
		[3,2,-5],
		[8,-3,6],
		[7,-4,9]
	]
)

b = np.array([3,9,18])

x = np.linalg.solve(a,b)
print(x)

print(np.dot(a,x))

arregloC = np.zeros((3,4))
print(arregloC)

arregloD = np.ones((4,5))
print(arregloD)

arregloD = np.random.randint(2,100,(10,4))
print(arregloD)

print(arregloD[0])
print(arregloD[0][0])
arregloD[0][0] = 1
arregloD[1] = [1,2,3,4]
print(arregloD)
print(arregloD[:,3])


arregloD[:,3]=[1,2,3,4,5,6,7,8,9,10]
print(arregloD)