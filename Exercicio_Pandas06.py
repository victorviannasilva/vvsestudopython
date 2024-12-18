import matplotlib.pyplot as plt
import pandas as pd

#pd.set_option('display.max_rows', None)
df_sentiment= pd.read_csv('sentiment_dataset-v01.csv')
df_sentiment.head()

df_sentiment['Country']=df_sentiment['Country'].str.strip()
df_sentiment['Sentiment']=df_sentiment['Sentiment'].str.strip()

df_country=df_sentiment['Country'].value_counts()
print(df_country)

df_emotions=df_sentiment['Sentiment'].value_counts()
#df_emotions=df_sentiment['Sentiment'].values
print(df_emotions)

df_new=df_sentiment[df_sentiment['Country']=='USA']
df_new.head()

df_newpos=df_sentiment[df_sentiment['Sentiment']=='Positive']

fig,ax= plt.subplots()
ax.boxplot([df_new['Likes'], df_newpos['Likes']],labels=['USA', 'Positive'])
ax.set_title('País, Likes e Sentimentos Positivos')
plt.show()
