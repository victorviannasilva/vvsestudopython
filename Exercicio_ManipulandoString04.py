fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
  x = line.rstrip().split()
  for i in x:
    if i not in lst:
      lst.append(i)
lst.sort()
print(lst)
