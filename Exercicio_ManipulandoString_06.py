fname = input("Enter file name: ")
count = 0
fh = open(fname)

for line in fh:
  line=line.strip()
  if not line.startswith("From "):
    continue
  posi = line.find(" ")
  posf = line.find(" ", posi + 1)
  print(line[posi + 1:posf])
  count = count + 1
print("There were", count, "lines in the file with From as the first word")
