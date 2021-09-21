import pandas as pd

df2 = pd.read_csv("2021-02-gasolina-etanol.csv",delimiter=";")

df3 = pd.read_csv("2021-03-gasolina-etanol.csv",delimiter=";")

df4 = pd.read_csv("2021-04-gasolina-etanol.csv",delimiter=";")

df5 = pd.read_csv("2021-05-gasolina-etanol-1.csv",delimiter=";")

df6 = pd.read_csv("2021-06-gasolina-etanol.csv",delimiter=";")

df7 = pd.read_csv("2021-07-gasolina-etanol.csv",delimiter=";")

frames = [df2,df3,df4,df5,df6,df7]

df = pd.concat(frames, sort=False)