import pandas as pd
import matplotlib.pyplot as plt

# Limpeza e padronização do dataset

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
print(df['INADIMPLENTE_90D'].value_counts())

# Taxa de inadimplência acima de 90 dias na carteira de clientes

taxa_inadimplencia_90d = df['INADIMPLENTE_90D'].mean()*100
print('Taxa de inadimplentes acima de 90 dias: {:.2f}%'.format(taxa_inadimplencia_90d))

# Associação de inadimplência com classe social

print(df.groupby('CLASSE_SOCIAL')['INADIMPLENTE_90D'].mean())





