import os

def changeFileName (lfn):
    lfnnoext = os.path.splitext(lfn)[0]
    inp=lfnnoext.replace('$','_')
    toks=inp.split("_")
    if len(toks)==5:
        print ("Already good format")
        return ""
    i=0
    nameis=toks[0]+"_"+toks[1]+"_"+toks[2]
    i=1
    s=toks[3][0:i]
    while s.isdigit():
        i=i+1
        s = toks[3][0:i]
    i=i-1
    s=s[:-1]
    nameis = nameis + "_" + s + "_" + toks[3][i:] + ".csv"
    return nameis

lfn='CCWRobot_04032020_141422$2True.csv'
#lfn='CCWRobot_04032020_141422_2True.csv'
#changeFileName(lfn)

f = []
for (dirpath, dirnames, filenames) in os.walk(r'c:\temp\logs'):
    f.extend(filenames)
    break
for s in f:
    oldname = os.path.join(r'c:\temp\logs', s)
    newname = changeFileName(s)
    if len(newname)>10:
        newname = os.path.join(r'c:\temp\logs', newname)
        if oldname.lower() != newname.lower():
            os.rename(oldname, newname)
