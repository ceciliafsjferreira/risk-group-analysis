import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

sns.countplot(data=df, x="INADIMPLENTE_90D")


plt.title("Distribuição da Inadimplência")
plt.ylabel("Quantidade de contratos")
plt.bar(
    df["INADIMPLENTE_90D"].value_counts().index,
    df["INADIMPLENTE_90D"].value_counts().values,
    color=["#8E44AD", "#E84393"]
)
plt.xticks([0, 1], ["Não inadimplente(81,9%)", "Inadimplente acima de 90 dias(18,1%)"])

plt.show()

classes = ['C', 'D']
taxas = [16.2015, 18.8898]

plt.bar(classes, taxas, color=["#3498DB", "#E74C3C"])
plt.title('Taxa de inadimplência por classe social')
plt.xlabel('Classe Social')
plt.ylabel('Taxa de inadimplência (%)')

plt.show()

df.groupby("CANAL_AQUISICAO")["INADIMPLENTE_90D"].mean()
df.groupby("POSSUI_RESTRICAO")["INADIMPLENTE_90D"].mean()
df.groupby("REGIAO")["INADIMPLENTE_90D"].mean()
df.groupby("SEXO")["INADIMPLENTE_90D"].mean()
df.groupby("NUM_EMPRESTIMOS_ANTERIORES")["INADIMPLENTE_90D"].mean()

df["FAIXA_SCORE"] = pd.cut(
    df["SCORE_INTERNO"],
    bins=[0, 300, 500, 700, 1000],
    labels=["Baixo", "Médio", "Bom", "Alto"]
)
df.groupby("FAIXA_SCORE", observed=True)["INADIMPLENTE_90D"].mean()

df["FAIXA_RENDA"] = pd.cut(
    df["RENDA_MENSAL"],
    bins=[0, 1500, 2500, 4000, np.inf],
    labels=["Até 1.500", "1.500-2.500", "2.500-4.000", "Acima de 4.000"]
)
df.groupby("FAIXA_RENDA", observed=True)["INADIMPLENTE_90D"].mean()

resultado = (
    df.groupby("CANAL_AQUISICAO")["INADIMPLENTE_90D"]
      .agg(["mean", "count"])
      .sort_values("mean", ascending=False)
)

print("\n--- Canal de Aquisição ---")
print(df.groupby("CANAL_AQUISICAO")["INADIMPLENTE_90D"].mean()*100)

print("\n--- Possui Restrição ---")
print(df.groupby("POSSUI_RESTRICAO")["INADIMPLENTE_90D"].mean()*100)

print("\n--- Região ---")
print(df.groupby("REGIAO")["INADIMPLENTE_90D"].mean()*100)

print("\n--- Sexo ---")
print(df.groupby("SEXO")["INADIMPLENTE_90D"].mean()*100)

print("\n--- Empréstimos Anteriores ---")
print(df.groupby("NUM_EMPRESTIMOS_ANTERIORES")["INADIMPLENTE_90D"].mean()*100)

print("\n--- Faixa de Score ---")
print(df.groupby("FAIXA_SCORE", observed=True)["INADIMPLENTE_90D"].mean()*100)

print("\n--- Faixa de Renda ---")
print(df.groupby("FAIXA_RENDA", observed=True)["INADIMPLENTE_90D"].mean()*100)








