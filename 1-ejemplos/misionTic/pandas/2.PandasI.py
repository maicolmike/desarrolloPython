
import pandas as pd

datos = {
	"fruta":["Mango","Uva","Papaya","Zapayo"],
	"calorias":[10,20,40,80]
}

df = pd.DataFrame(datos)

print(df)
print(df.columns)

print(df["calorias"])

print(df.head(2))

df.tail(2)

df.info()

df.describe()

print(df["calorias"].mean())
print(df["calorias"].std())
print(df["calorias"].min())
print(df["calorias"].sum())

a = list(df["fruta"])
print(a)

print(df["calorias"])

df

df.loc[1]
