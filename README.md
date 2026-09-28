# 📊 Case de Análise de Inadimplência

Projeto de **Análise Exploratória de Dados (EDA)** desenvolvido como parte da minha jornada de estudos em **Data Science**, com foco na identificação de padrões relacionados à inadimplência em uma carteira de crédito.

---

## 🎯 Sobre o projeto

O projeto simula o cenário de uma **fintech de crédito**, utilizando uma base fictícia com **5.000 contratos**.

O objetivo da análise foi compreender o comportamento da carteira, calcular a taxa geral de inadimplência e investigar se determinados segmentos de clientes apresentam níveis de risco superiores à média.

A análise foi desenvolvida utilizando **Python para exploração e tratamento dos dados** e **Power BI para visualização e construção do dashboard**.

---

## 🔎 Objetivos da análise

Durante o projeto, busquei responder principalmente:

* Qual é a taxa geral de inadimplência acima de 90 dias?
* Existem segmentos com taxa de inadimplência acima da média da carteira?
* Quais características podem estar associadas a diferentes níveis de risco?
* Como transformar os resultados da análise em uma recomendação de negócio?

---

## 🗂️ Base de dados

A base contém informações relacionadas aos contratos e ao perfil dos clientes, incluindo:

* Idade
* Sexo
* Região
* Renda mensal
* Classe social
* Score interno
* Canal de aquisição
* Número de empréstimos anteriores
* Tempo de relacionamento
* Restrição cadastral
* Valor solicitado
* Prazo do empréstimo
* Comprometimento da renda
* Dias de atraso máximo
* Inadimplência acima de 90 dias

A variável `INADIMPLENTE_90D` foi utilizada como variável-alvo da análise.

---

## 🛠️ Tecnologias e ferramentas

### 🐍 Python

Utilizado principalmente para preparação, exploração e análise dos dados.

* **Pandas** — manipulação e análise de dados
* **Matplotlib** — criação de visualizações
* **Python** — desenvolvimento da análise exploratória

### 📊 Power BI

Utilizado para transformar os resultados da análise em um dashboard interativo.

* Criação de indicadores (KPIs)
* Criação de gráficos e segmentações
* Análise de diferentes perfis de clientes
* Criação de medidas com **DAX**
* Comparação dos segmentos com a média geral da carteira

### 🔧 Git & GitHub

Utilizados para versionamento e organização do projeto.

---

## 📚 Técnicas praticadas

Durante o desenvolvimento do case, foram praticados conceitos como:

* Análise Exploratória de Dados (EDA)
* Limpeza e padronização de dados
* Análise de variáveis categóricas e numéricas
* `groupby()` e agregações com Pandas
* Cálculo de médias e taxas
* Segmentação de clientes
* Criação de faixas de Score
* Criação de faixas de renda
* Análise de comprometimento da renda
* Comparação entre segmentos
* Visualização de dados
* Construção de KPIs
* Criação de medidas em DAX
* Data storytelling
* Interpretação de resultados para apoio à decisão

---

## 📈 Principais resultados

A taxa geral de inadimplência encontrada na carteira foi de:

### **18,10%**

A partir desse valor, os diferentes segmentos foram comparados com a média geral para identificar grupos que apresentassem taxas superiores.

Entre as análises realizadas estão:

* Inadimplência por classe social
* Inadimplência por canal de aquisição
* Inadimplência por região
* Inadimplência por faixa de Score
* Inadimplência por restrição
* Inadimplência por faixa de renda
* Inadimplência por comprometimento da renda
* Inadimplência por número de empréstimos anteriores

> A análise não considera apenas a maior taxa encontrada. O tamanho de cada segmento também deve ser considerado para evitar conclusões baseadas em grupos muito pequenos.

---

## 📊 Dashboard

O dashboard desenvolvido no Power BI foi estruturado em diferentes perspectivas:

### Visão Geral

Apresenta os principais indicadores da carteira:

* Taxa de inadimplência
* Total de contratos
* Valor médio solicitado
* Score médio

Além disso, apresenta a distribuição da inadimplência por diferentes segmentos.

### Análise de Risco

Aprofunda a investigação sobre características relacionadas ao risco, incluindo:

* Faixa de Score
* Faixa de renda
* Comprometimento da renda
* Número de empréstimos anteriores
* Restrição cadastral

### Detalhamento

Permite explorar os registros da base e analisar individualmente características dos contratos.

---

## 🧠 O que aprendi

Este projeto foi importante para entender melhor o fluxo completo de uma análise de dados:

**Dados brutos → Tratamento → Exploração → Análise → Visualização → Interpretação → Recomendação**

Além do desenvolvimento técnico com Python, Pandas, Power BI e DAX, pude praticar uma etapa fundamental da área de dados: **transformar resultados estatísticos em informações que possam ser compreendidas e utilizadas no contexto de negócio.**

---

## 📁 Estrutura do projeto

```text
case-inadimplencia/
│
├── 📄 case_inadimplencia.csv
├── 🐍 analise_inicial.py
├── 📖 dicionario_de_dados.md
└── 📄 README.md
```

---

## 🚀 Próximos passos

Como evolução do projeto, algumas possibilidades seriam:

* Desenvolver uma análise estatística mais aprofundada
* Investigar correlações entre as variáveis
* Testar modelos de Machine Learning para previsão de inadimplência
* Avaliar métricas de classificação
* Comparar diferentes modelos preditivos
* Evoluir o dashboard com novas análises de risco

---

## 👩‍💻 Sobre mim

**Cecília F. Souza**

🎓 Estudante de **Data Science na FIAP**

💻 Interesse em **Data Analytics, Data Science, Python, SQL, Power BI, AWS e Cloud Computing**.

Este projeto faz parte da minha construção de portfólio e da minha jornada de aprendizado na área de dados.

---

⭐ Se este projeto foi útil ou interessante para você, fique à vontade para explorar o repositório!

