data="""
      public int timeoutToLogoutFromLastActivityMS = 2500;
"""


def getrelevant(alist):
    parts = list(map(str.strip, alist))
    parts = [x for x in parts if len(x) > 0]
    return parts


lines = data.split(';\n')
for line in lines:
    if len(line) == 0:
        continue
    parts = line.split(' ')
    if len(parts) < 3:
        continue
    parts = getrelevant(parts)  # list(map(str.strip, parts))
    atype=parts[1]
    vname=parts[2]
    print("res.{0} = {1}.Parse( ct.data.FirstOrDefault(x => x.key == \"{0}\").updateValue);".format(vname, atype))