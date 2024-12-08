import pandas as pd
#Importação de dados em arquivo em formato json usando Pandas.

pd.set_option('display.max_columns', None)
df_json = pd.read_json('cidades.json') 
df_json.head(1) #  .head() é o método para exibir os primeiros.
print(df_json) #   print() é o método para exibir os dados. 
