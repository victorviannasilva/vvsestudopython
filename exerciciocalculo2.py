def equacao(x):
#efetua o calculo da equacao de segundo grau com a >0 e b>0
   equacao=float(x**2+4*x+7)
   return equacao

x=eval(input('informe o valor de x:'))
print('o valor da equacao é:',equacao(x))
