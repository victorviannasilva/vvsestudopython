#Operações matemáticas com Arrays e produto entre vetores.
#Uso do módulo Numpy no lugar do For e das Listas.

import numpy as np

lista_produto=["carro", "lápis","caderno"]
lista_precos=[50000.0,40000.0,10000.00,20000.00]
lista_correcao=[1.089,1.055,1.064,1.023]
arr=np.array(lista_precos)
corr=np.array(lista_correcao)

correcao=1.089
matriz=arr*corr
lista_final=arr*correcao
print(lista_final)
print(matriz)
