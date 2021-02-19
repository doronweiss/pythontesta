data="""
"""

def getrelevant(alist):
    parts = list(map(str.strip, alist))
    parts = [x for x in parts if len(x) > 0]
    return parts

lines = [ln for ln in data.split('\n') if len(ln)>0]
print ("Len={0}".format(len(lines)))
for line in lines:
    parts = line.split('\t')
    parts = getrelevant(parts)  # list(map(str.strip, parts))
    fparts = [float(x) for x in parts]
    parts = [str(x) for x in fparts]
    print ("{{ {0} }},".format(", ".join(parts)))
