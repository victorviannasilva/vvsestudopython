import pandas as pd

#Uso do pandas para importação(leitura) de dados.
#O arquivo .csv deve estar no mesmo diretório do arquivo .py

pd.set_option('display.max_columns', None)# exibe todas as colunas do arquivo no método print().
df_csv = pd.read_csv('arquivo.csv') #   .read_csv() é o método para importar dados.
df_csv.head(1) #  .head() é o método para exibir os primeiros registros.
print(df_csv) #   print() é o método para exibir os dados. 
#Se possuir o tabulate instalado você pode usar o método display() no lugar do print().
