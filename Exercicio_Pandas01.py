import pandas as pd

#Uso do pandas para criação e manipulação de dataframes.

pd.set_option('display.max_columns', None)

cidades=['são paulo','rio de janeiro','salvador','curitiba','guarulhos']
pib=[1000000,2000000,3000000,4000000,5000000]
renda=[6000000,7000000,8000000,9000000,12000000]

cidades_series=pd.Series(cidades)
renda_series=pd.Series(renda).astype(float)
#Manipulação de séries
print(cidades_series[2:4])
print(cidades_series)
pib_series=pd.Series(pib).astype(float)
dobro_pib=pib_series*2
print(dobro_pib)
print(dobro_pib.max())

#Adição de uma nova tabela.
dados_cidades = pd.DataFrame({'cidades': cidades_series, 'pib': pib_series})

#Manipulação de dataframes.
dados_cidades.tail()
dados_cidades.iloc[2]
dados_cidades.head()
print(dados_cidades['pib'].mean())

#Combinação de colunas no dataframe.

dados_cidades['Renda']=renda_series
dados_cidades['Relação Renda por PIB']=dados_cidades['Renda']/dados_cidades['pib']
print(dados_cidades)

#Informações do dataframe.
dados_cidades.info()
