fname = input("Enter file name: ")
fh = open(fname)

base = dict()
tempo= dict()

for line in fh:
  line=line.strip()
  if not line.startswith("From "): continue
  words=line.split()
  if len(words)>=2:
    email=words[1]
    base[email]=base.get(email,0)+1

  if len(words)>=6:
    time=words[5]
    hora=time.split(":")[0]
    tempo[hora]=tempo.get(hora,0)+1

for hora,count in sorted(tempo.items()):
      maxhora=count
      listahora=hora
      print(f{listahora} {maxhora})
fh.close()
