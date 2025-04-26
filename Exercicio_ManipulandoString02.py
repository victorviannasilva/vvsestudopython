fname = input("Enter file name: ")
fh = open(fname)
xline=0
Xdatafloat=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    zero=line.find("0")
    host=line[zero:zero+6]
    #print(host)
    datafloat=float(host)
    Xdatafloat=Xdatafloat+datafloat
    xline=xline+1
valorfinal=Xdatafloat/xline
print(xline)
print(Xdatafloat)
print("Average spam confidence:",valorfinal)
print("Done")
