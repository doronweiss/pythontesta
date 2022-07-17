import sys

data="""
  VOLTAGE_STATE_BAD = 0,
  VOLTAGE_STATE_GOOD=1,
  VOLTAGE_STATE_UNKNOWN=2
"""

print ("What do you want to do ?:\n")
print ("For Getters enter            - 1")
print ("For Setter enter             - 2")
print ("For camelCasing              - 3")
print ("For Enum                     - 4")
try:
    opt = int(input("Enter choice: "))
except:
    print("Bad input, exiting")
    sys.exit()
lines = [ln for ln in data.split('\n') if len(ln)>0]
for line in lines:
    if len(line) == 0:
        continue
    parts = line.split('=')
    if len(parts)<2:
        continue
    maskName = parts[0].strip().strip(',')
    idx = maskName.find("Mask")
    if idx>=0:
        methName=maskName[0:idx]
        methName = methName[0].capitalize() + methName[1:]
    else:
        methName=maskName
    # getter
    match opt:
        case 1:
            print("public bool {0} => state[{1}];".format(methName, maskName))
        case 2:
            print("public bool {0} {{set => state[{1}] = value;}}".format(methName, maskName))
        case 3:
            print ("public const int {}".format(line.replace("_", " ").title().replace(" ","")))
        case 4:
            print ("{},".format(methName.replace("_", " ").title().replace(" ","")))
        case default:
            print("Bad input, exiting")
            sys.exit()
    #setter
