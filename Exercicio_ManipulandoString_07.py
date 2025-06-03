fname = input("Enter file name: ") # Pede ao usuário o nome do arquivo
fh = open(fname) # Abre o arquivo

base = dict() # Dicionário para armazenar a contagem de cada e-mail
for line in fh: # Percorre cada linha do arquivo
  line=line.strip() # Remove espaços em branco do início/fim da linha
  if not line.startswith("From "): continue  # Ignora linhas que não começam com 'From '
  words=line.split() # Divide a linha em palavras
  if len(words)>=2:  # Garante que haja pelo menos duas palavras
    email=words[1]  # O e-mail está na segunda posição
    base[email]=base.get(email,0)+1 # Conta quantas vezes o e-mail aparece
    
listaemail =None  # Variável que guardará o e-mail com maior contagem
maxemail= 0  # Inicializa a contagem máxima com zero

for email,count in base.items():  # Percorre os pares e-mail/contagem no dicionário
    if maxemail is None or count>maxemail:
      maxemail=count  # Atualiza o valor máximo
      listaemail=email # Atualiza o e-mail mais frequente
print(listaemail, maxemail) # Exibe a cada atualização de máximo
fh.close()  # Fecha o arquivo
