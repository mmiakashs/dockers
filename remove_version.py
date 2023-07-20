f = open("pt_1-11_pl_1-6-1", "r")
lines = []
for x in f:
    tm = ''
    flag=True
    for ch in x:
        if(ch=='='):
            flag=False
        if(ch=='\\'):
            flag=True
        if(flag):
            tm += ch
    with open("out", "a") as fo:
        fo.write(tm)
 

