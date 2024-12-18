import pandas as pd
import plotly.express as px 

path='CaminhoDoArquivo'
df_social= pd.read_excel(path)
df_social20=df_social[df_social['year']<2013]
df_social20.head()

met_year= df_social20['year'].value_counts()
met_year=pd.DataFrame({'year':met_year.index, 'count':met_year.values}).sort_values(by='year')
px.line(met_year, x='year', y='count', title='Meteoritos por ano')

met_cat=df_social20.groupby('recclass').agg({'mass (g)':'mean', 'id': 'count'}).reset_index()
px.histogram(df_social20, "reclat", nbins=100)
