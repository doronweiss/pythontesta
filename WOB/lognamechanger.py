import os

lfn='CCWRobot_04032020_141422$2True.csv'
lfn='CCWRobot_04032020_141422_2True.csv'
lfnnoext = os.path.splitext(lfn)[0]
inp=lfnnoext.replace('$','_')
toks=inp.split("_")
if len(toks)==5:
    print ("Already good format")
    os._exit(0)
i=0
for s in toks:
    print ("Tok[{}]={}".format(i, s))
    i=i+1
nameis=toks[0]+"_"+toks[1]+"_"+toks[2]
print ("Nameis: {}".format(nameis))
i=1
s=toks[3][0:i]
while s.isdigit():
    i=i+1
    s = toks[3][0:i]
i=i-1
s=s[:-1]
nameis = nameis + "_" + s + "_" + toks[3][i:]
print ("Nameis: {}".format(nameis))
