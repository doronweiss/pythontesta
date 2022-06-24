data="""
sysOkMask = BitVector16.CreateMask();
ackMask = BitVector16.CreateMask(sysOkMask);
systemBusyMask = BitVector16.CreateMask(ackMask);
readyForTargetMask = BitVector16.CreateMask(systemBusyMask);
trolleyInTargetMask = BitVector16.CreateMask(readyForTargetMask);
readyForTransferMask = BitVector16.CreateMask(trolleyInTargetMask);
robotExistMask = BitVector16.CreateMask(readyForTransferMask);
homeSeqDoneMask = BitVector16.CreateMask(robotExistMask);
atAutoMask = BitVector16.CreateMask(homeSeqDoneMask);
robotOnMiddleMask = BitVector16.CreateMask(atAutoMask);
res1Mask = BitVector16.CreateMask(robotOnMiddleMask);
res2Mask = BitVector16.CreateMask(res1Mask);
resetAckMaskMask = BitVector16.CreateMask(res2Mask);
targetNotFoundMask = BitVector16.CreateMask(resetAckMaskMask);
EMPressedMask = BitVector16.CreateMask(targetNotFoundMask);
SWWatchDogMask = BitVector16.CreateMask(EMPressedMask);
"""


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
    print("public bool {0} => state[{1}];".format(methName, maskName))