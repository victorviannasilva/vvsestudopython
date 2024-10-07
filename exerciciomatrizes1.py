#Primeira solução sem usar a função len para identificar a quantidade de linhas da matriz.
'''
a=eval(input('Informe o valor de a: '))
b=eval(input('Informe o valor de b: '))
c=eval(input('Informe o valor de c: '))
matriz=[[1,2,3],[a,b,c]]
d=len(matriz[1])
e=len(matriz[0])

for i in range(d):
  matriz[1][i]=float(matriz[1][i]*2+2)
for j in range(e):
  matriz[0][j]=float(matriz[0][j]*2+2)
print(matriz)
print(g)
