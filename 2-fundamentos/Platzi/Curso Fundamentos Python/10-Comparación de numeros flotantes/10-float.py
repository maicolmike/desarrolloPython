x = 3.3
print(x)

y = 1.1 + 2.2
print(y)

print(x==y)

#1ra forma volver str
y_str = format(y, ".2g")
print("str", y_str)

print("Comparacion string")
print(y_str == x)
print(y_str == str(x))

# 2da forma matematica
print("Comparacion forma matematica")
tolerance = 0.0001
print(abs(x - y) < tolerance)