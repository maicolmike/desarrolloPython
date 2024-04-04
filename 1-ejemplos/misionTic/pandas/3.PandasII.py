
import pandas as pd

datos_productos = {
    "categoria":["limpieza","juguetes","ropa","limpieza","videojuegos"],
    "tienda":["olimpica","super inter","d1","justo y bueno","star store"],
    "precios":[10.5,80.3,10.9,13.3,100.3],
    "calificacion":[4,3,9,8,3]
}

df = pd.DataFrame(datos_productos)
print(df)

df_nuevo = df.sort_values("precios")
print(df_nuevo)

print(df.iloc[1:4])

print(df["categoria"]=="limpieza")

print(df[df["categoria"]=="limpieza"])

