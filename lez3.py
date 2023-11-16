def sum_csv(file):
    ff=open(file,"r")
    c=0
    tot=0
    ff.readline()
    for line in ff:
        c=1
        z=line.split(",")
        print(z)
        try:
            tot+=float(z[1])
        except:
            tot+=0
    ff.close()
    if c==0:
        return None
    return tot
