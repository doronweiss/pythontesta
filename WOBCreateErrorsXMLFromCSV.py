import sys

fileName = r"c:\Projects\Weldobot\AROW OMRON Error Codes.csv"
try:
    fi = open(fileName, 'r', encoding='Windows-1252', errors='replace')
except:
    print("Could not open file: {0}".format(fileName))
    sys.exit()
ln = fi.readline()  # skip header line
ln = fi.readline()
prevT0 = ""
prevT2 = ""
while ln and ln != "":
    toks = ln.split(",")
    if not toks[0]:
        toks[0] = prevT0
    else:
        prevT0 = toks[0]
    if not toks[2]:
        toks[2] = prevT2
    else:
        prevT2 = toks[2]
    print('<ErrorDesc family="Motion" errorCode="{0}" severity="{1}" userDescrition="{2}"/>'.format(toks[1], toks[2], toks[0] + ':' + toks[3]))
    ln = fi.readline()
fi.close();
