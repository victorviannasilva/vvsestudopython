def equacao(x):
#efetua o calculo da equacao de segundo grau com a >0 e b>0
   equacao=int(x**2+4*x+7)
   return equacao
for x in range(0,11):
   l=[x,equacao(x)]
   print(l)
   
   z=len(l)
