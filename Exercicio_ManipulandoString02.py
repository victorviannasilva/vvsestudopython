fname = input("Enter file name: ")
fh = open(fname, "r")
for line in fh:
 line = line.upper().rstrip()
 print(line)
