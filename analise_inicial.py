import pandas as pd

df = pd.read_csv("case_inadimplencia.csv")

line = df.shape[0] 
column = df.shape[1]
print('O dataset possui {} linhas e {} colunas'. format(line , column))
