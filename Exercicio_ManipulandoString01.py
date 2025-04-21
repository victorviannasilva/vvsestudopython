texto=input("Digite uma palavra para análise:")
escolha=texto.lower().strip()
indice = 0
while indice < len(escolha):
  letra = escolha[indice]
  print(letra)
  indice = indice + 1
print(len(escolha),":essa é a quantidade de letras da palavra",escolha)
print("Fim do loop")

#Manipulando strings:

x = 'From marquard@uct.ac.za'
print(len(x))
print(x[14:17])
print(len(x)*7)

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])

text = "X-DSPAM-Confidence:    0.8475"
zero=text.find("0")
cinco=text.find("5",zero)
host = text[zero:cinco+1]
print(float(host))
