import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
import pandas as pd


# Configurações do gráfico
plt.figure(figsize=(12, 6))
valores=[2000,5000,13957.98,14040.79,149,4500,4500,2128.00]

#Ddados Estatísticos
datavalores = pd.Series(valores)
datastatistics = datavalores.describe()
print(datastatistics)

# Histograma
plt.subplot(1, 2, 1)
plt.hist(valores, bins=8, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Histograma dos Preços')
plt.xlabel('Preços em Reais')
plt.ylabel('Frequência')

# Curva de Distribuição t-Student
alfa = 0.05
graus_de_liberdade = len(valores) - 1
media = np.mean(valores)
desvio_padrao = np.std(valores, ddof=1)

# Intervalo de valores para a curva t-Student
x_vals = np.linspace(min(valores) - 1000, max(valores) + 1000, 1000)
t_dist = stats.t.pdf(x_vals, df=graus_de_liberdade, loc=media, scale=desvio_padrao)

plt.subplot(1, 2, 2)
plt.plot(x_vals, t_dist, color='blue', label='Distribuição t-Student')
plt.fill_between(x_vals, t_dist, where=(x_vals <= media + stats.t.ppf(1 - alfa/2, graus_de_liberdade) * desvio_padrao) & 
                 (x_vals >= media - stats.t.ppf(1 - alfa/2, graus_de_liberdade) * desvio_padrao), color='orange', alpha=0.5, label='Intervalo de Confiança 95%')
plt.title('Curva de Distribuição t-Student')
plt.xlabel('Preços em Reais')
plt.ylabel('Densidade de Probabilidade')
plt.legend()

plt.tight_layout()
plt.show()
