# Segunda solução usa a função len para saber a quantidade de linhas da matriz.

a=eval(input('Informe o valor de a: '))
b=eval(input('Informe o valor de b: '))
c=eval(input('Informe o valor de c: '))
matriz=[[1,2,3],[a,b,c]]

e=len(matriz[0])
g=len(matriz)

for i in range(g):
  for j in range(e):
    matriz[i][j]=float(matriz[i][j]*2+2)
print(matriz)
print(g)
print(matriz[1])
