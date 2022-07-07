data="""
    gotoTargetMask = BitVector16.CreateMask();
    startProcessMask = BitVector16.CreateMask(gotoTargetMask);
    goToChargeCmdMask = BitVector16.CreateMask(startProcessMask);
    StartHomeCmdMask = BitVector16.CreateMask(goToChargeCmdMask);
    goHomeCmdMask = BitVector16.CreateMask(StartHomeCmdMask);
    disengageCmdMask = BitVector16.CreateMask(goHomeCmdMask);
    firstCycleMask = BitVector16.CreateMask(disengageCmdMask);
    autoCmdMask = BitVector16.CreateMask(firstCycleMask);
    arolleyJumpMask = BitVector16.CreateMask(autoCmdMask);
    res1Mask = BitVector16.CreateMask(arolleyJumpMask);
    res2Mask = BitVector16.CreateMask(res1Mask);
    res3Mask = BitVector16.CreateMask(res2Mask);
    res4Mask = BitVector16.CreateMask(res3Mask);
    res5Mask = BitVector16.CreateMask(res4Mask);
    resetErrorsMask = BitVector16.CreateMask(res5Mask);
    watchDogMask = BitVector16.CreateMask(resetErrorsMask);
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
    # getter
    #print("public bool {0} => state[{1}];".format(methName, maskName))
    #setter
    print("public bool {0} {{set => state[{1}] = value;}}".format(methName, maskName))
