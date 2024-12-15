import matplotlib.pyplot as plt
import pandas as pd
# Faz a leitura do arquivo e aplica um filtro na coluno 'uf'.

df_left = pd.read_csv('area_urbana.csv')
df_filtered=df_left[(df_left['uf'] == 'São Paulo')&\
(df_left['ranking'] < 30)]

#Aplica uma contagem na coluna 'municipio no arquivo filtrado para elaboração de um gráfico.
municipio = df_filtered['municipio'].value_counts()
graf= pd.DataFrame({'municipio':municipio.index, 'cont': municipio.values}).sort_values(by='municipio')
graf[(graf['cont'] < 40)] #seleciona apenas as contagems inferiores a 40.

#Realiza a plotagem do gráfico 
plt.plot(graf['cont'],graf['municipio']) #define as coordenadas x e y, respectivamente.
plt.xlabel('qtde')
plt.ylabel('Cidades')
plt.show()
df_filtered.to_csv('df_grafpandas5.csv', index=True) #Gera um arquivo .csv usado para gerar o gráfico.
