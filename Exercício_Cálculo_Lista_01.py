#Operações matemáticas com Listas em Python
#Operações com listas usando For.

lista_produto=["carro", "lápis","caderno"]
lista_precos=[50000.0,40000.0,10000.00,20000.00]
lista_final=[]
correcao=1.089

for i in lista_precos:
  calculo=round(i*correcao,2)
  lista_final.append(calculo)  
print(lista_produto)
print(lista_precos)
print(lista_final)
