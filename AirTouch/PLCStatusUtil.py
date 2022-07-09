import sys

data="""
DUMMY_PROTO_CMD = 0;
SET_TIME_PROTO_CMD = 1;
ROBOT_WOKE_UP_PROTO_CMD = 2
DRIVE_STATE_REPORT_PROTO_CMD = 3;
CLEAN_SCHED_PROTO_CMD = 4;
PREVENT_CLEAN_SCHED_PROTO_CMD = 5;
IMMEDIATE_CLEAN_PROTO_CMD = 6;
ROBOT_OPER_ENABLE_PROTO_CMD = 7;
RESET_PROTO_CMD = 8;
CLEANING_PARAMS_PROTO_CMD = 9;
EVENT_REPORT_PROTO_CMD = 0x0A;
SELF_TEST_PROTO_CMD = 0x0B;
QUERY_PROTO_CMD = 0x0C;
START_CLEANING_WITH_DIR_CMD = 0x0D;
GET_ON_VEHICLE_CMD = 0x0E;
GET_OFF_VEHICLE_CMD = 0x0F;

"""

print ("What do you want to do ?:\n")
print ("For Getters enter            - 1")
print ("For Setter enter             - 2")
print ("For camelCasing              - 3")
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
    methName=maskName[0:idx]
    methName = methName[0].capitalize() + methName[1:]
    # getter
    match opt:
        case 1:
            print("public bool {0} => state[{1}];".format(methName, maskName))
        case 2:
            print("public bool {0} {{set => state[{1}] = value;}}".format(methName, maskName))
        case 3:
            print ("public const int {}".format(line.replace("_", " ").title().replace(" ","")))
        case default:
            print("Bad input, exiting")
            sys.exit()
    #setter
