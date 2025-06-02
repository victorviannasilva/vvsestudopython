fname = input("Enter file name: ")
count = 0
fh = open(fname)

for line in fh:
  line=line.strip()
  if line.startswith("From "):
    words=line.split()
    if len(words)>=1:
      print(words[1])
      count = count + 1
fh.close()
print("There were", count, "lines in the file with From as the first word")
