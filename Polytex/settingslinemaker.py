data="""
      int timeoutToLogoutFromLastActivityMS = 2500;
"""

typedict={
    "string" : "JSONDataType.text",
    "short" : "JSONDataType.number",
    "int" : "JSONDataType.number",
    "long" : "JSONDataType.number",
    "float" : "JSONDataType.number",
    "double" : "JSONDataType.number",
    "bool" : "JSONDataType.checkbox"
}

def getrelevant (alist):
    parts= list(map(str.strip, alist))
    parts = [x for x in parts if len(x)>0]
    return parts

lines = data.split(';\n')
for line in lines:
    if len(line) == 0:
        continue
    parts = line.split(' ')
    if len(parts)<2:
        continue
    parts= getrelevant(parts) #list(map(str.strip, parts))
    typestr=""
    if parts[0] in typedict:
        typestr=typedict[parts[0]]
    else:
        typestr="JSONDataType.unknown"
    print("ct.data.Add(CreateSVD(\"{0}\", \"{0}\", {0}.ToString(), false, {1}, new OptionValueType[] {{ }}, new string[] {{\"required\"}}));".format(parts[1], typestr))