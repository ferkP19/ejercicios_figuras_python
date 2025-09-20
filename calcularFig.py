
import pandas as pd
import math

df = pd.read_csv("figuras.csv")


areas = []
perimetros = []


for i in range(len(df)):
    fig = df.loc[i, "FIGURA"].strip().lower()
    m1 = df.loc[i, "MEDIDA1"]
    m2 = df.loc[i, "MEDIDA2"]

    if fig == "c":  # Círculo
        areas.append(math.pi * m1**2)
        perimetros.append(2 * math.pi * m1)
    elif fig == "r":  # Rectángulo
        areas.append(m1 * m2)
        perimetros.append(2 * (m1 + m2))
    elif fig == "t":  # Triángulo
        areas.append((m1 * m2)/2)
        perimetros.append(m1 + m2 + math.sqrt(m1**2 + m2**2))

df["AREA"] = areas
df["PERIMETRO"] = perimetros

df.to_csv("figuras_resultados.csv", index=False)
print(df)
