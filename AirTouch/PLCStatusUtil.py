import sys
import re

data = """
    Current weight A1
    Current weight A2
    Current weight B1
    Current weight B2
    Low level sensor status A1
    Low level sensor status A2
    Low level sensor status B1
    Low level sensor status B1
    Barrel is about to be empty A1
    Barrel is about to be empty A2
    Barrel is about to be empty B1
    Barrel is about to be empty B2
    Barrel replace command status A1
    Barrel replace command status A2
    Barrel replace command status B1
    Barrel replace command status B2
    Barrel replaced A1
    Barrel replaced A2
    Barrel replaced B1
    Barrel replaced B2
    Mixer status A1
    Mixer status A2
    Pump status A1
    Pump status A2
    Pump status B1
    Pump status B2
    Pump run command for bleeding status A1
    Pump run command for bleeding status A2
    Bleeding push button status A1
    Bleeding push button status A2
    Bleeding valve status A1
    Bleeding valve status A2
    """
# base strings
case1str = "public bool {0} => state[{1}];"
case2str = "public bool {0} {{set => state[{1}] = value;}}"
case3str = "public const int {}"
case4str = "{},"

# in-line delimiters
delimiters = [",", " "]

print("What do you want to do ?:\n")
print("For Getters enter            - 1")
print("For Setter enter             - 2")
print("For camelCasing              - 3")
print("For Enum                     - 4")
try:
    opt = int(input("Enter choice: "))
except:
    print("Bad input, exiting")
    sys.exit()
lines = [ln for ln in data.split('\n') if len(ln) > 0]
for line in lines:
    if len(line) == 0:
        continue
    #parts = line.split()
    parts = re.split(' |,|\t', line)
    if len(parts) < 2:
        continue
    maskName = parts[0].strip().strip(',')
    idx = maskName.find("Mask")
    if idx >= 0:
        methName = maskName[0:idx]
        methName = methName[0].capitalize() + methName[1:]
    else:
        methName = maskName
    match opt:
        case 1:
            print(case1str.format(methName, maskName))
        case 2:
            print(case2str.format(methName, maskName))
        case 3:
            print(case3str.format(line.replace("_", " ").title().replace(" ", "")))
        case 4:
            print(case4str.format(methName.replace("_", " ").title().replace(" ", "")))
        case default:
            print("Bad input, exiting")
            sys.exit()