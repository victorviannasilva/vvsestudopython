import pandas as pd
import statistics

pd.set_option('display.max_columns', None)

df_left = pd.read_csv('area_urbana.csv')
df_right = pd.read_csv('populacao.csv')

df_inner_join = pd.merge(df_left, df_right, on='ranking', how='inner')
df_filtered = df_inner_join[\
(df_inner_join['populacao'] > 1000000) &\
(df_inner_join['ranking'] < 11) &\
(df_inner_join['area urbana km²'] > 300.000)]

media = df_filtered['area urbana km²'].mean()
mediana = df_filtered['area urbana km²'].median()
desvpad = statistics.stdev(df_filtered['area urbana km²'])

print(df_filtered)
print("Média da área urbana=",media)
print("Mediana da área urbana=",mediana)
print("O desvio padrão da área urbana=",desvpad)


df_estatis=df_filtered.describe()
df_corr=df_filtered.corr(numeric_only=True)
df_dataframeinfo=df_filtered.info()

df_filtered.to_csv('df_resultados.csv', index=False)
df_estatis.to_csv('df_estatis.csv',index=True)
df_corr.to_csv('df_corr.csv',index=True)
