def soma(num1, num2):
  soma=num1+num2
  return soma
def subtracao(num1, num2):
  subtracao=num1-num2
  return subtracao
def multiplicacao(num1, num2):
  multiplicacao=num1*num2
  return multiplicacao  
def divisao(num1, num2):
  divisao=num1/num2
  return divisao

print("Olá, bem vindo a calculadora!")
print("Escolha uma das opções abaixo:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Sair")

opcao = int(input("Digite a opção desejada: "))

if opcao == 5:
  print("Obrigado por usar a calculadora!")
  exit()

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if opcao == 1:
  print("O resultado da soma é:", soma(num1, num2))
elif opcao == 2:
  print("O resultado da subtração é:", subtracao(num1, num2))
elif opcao == 3:
  print("O resultado da multiplicação é:", multiplicacao(num1, num2))
elif opcao == 4:
  if num2 == 0:
    print("Não é possível dividir por zero")
  else:
    print("O resultado da divisão é:", divisao(num1, num2))
else:
  print("Opção inválida!")
