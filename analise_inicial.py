import pandas as pd

df = pd.read_csv("case_inadimplencia.csv")


line = df.shape[0] 
column = df.shape[1]
print('O dataset possui {} linhas e {} colunas'. format(line , column))

df.fillna(0, inplace=True)
df.columns = df.columns.str.strip().str.upper()
df['FINALIDADE'] = df['FINALIDADE'].str.strip().str.lower()
df['CANAL_AQUISICAO'] = df['CANAL_AQUISICAO'].str.strip().str.lower()
df['REGIAO'] = df['REGIAO'].str.strip().str.lower()

df.drop(columns=[ 'VALOR_PARCELA', 'TAXA_JUROS_AM', 'ID_CLIENTE', 'DATA_CONTRATACAO'], inplace=True)

df.isnull().sum()
df.info()
df.describe()
df.duplicated().sum()

print(df.describe().T)