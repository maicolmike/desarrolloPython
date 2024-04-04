f = open("salida.txt","r")

for linea in f:
	print(linea)

f.close()

g = open("index.html","w")
contenido = ["<html>","<head>","<title>","Anonymus Colombia","</title>","</head>","<body>","<h1>","Has sido hackeado","</h1>","</body>","</html>"]

for linea in contenido:
	g.write(linea)

g.close()


h = open("contar.txt","w")
h.write("x\tx^2\n")
h.write("----------------------\n")
for i in range(0,101):
	h.write(f"{i}\t{i*i}\n")

h.close()