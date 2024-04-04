
#La pila es una lista
stack = []

#Si está vacia
print(len(stack)==0)

#Insertar elementos
stack.append(1)
stack.append(3)
stack.append(4)

print(stack.pop())
print(stack.pop())
print(stack.pop())

print(len(stack)==0)
