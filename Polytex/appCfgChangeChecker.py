data="""
UIDefinitions
      public int timeoutToLogoutFromLastActivityMS = 2500;
"""

def getrelevant(alist):
    parts = list(map(str.strip, alist))
    parts = [x for x in parts if len(x) > 0]
    return parts


lines = [ln for ln in data.split('\n') if len(ln)>0]
typename=lines[0].strip().rstrip(';')
for line in lines:
    if len(line) == 0:
        continue
    parts = line.split(' ')
    parts = getrelevant(parts)  # list(map(str.strip, parts))
    if len(parts) < 3:
        continue
    vname=parts[2]
    print("if ({0} != newConfig.{0})".format(vname))
    print ("Add2Set(effects, GetFieldEffect(typeof({0}).GetField(\"{1}\")));".format(typename, vname))

