data="""
NoneMOP
ProductionMOP
TechnitionMOP
CleaningMOP
 Initialized
ExecutingHome
 AllAxisHomeDone
 ExecutingPurge
 PurgeCompleted
 PrintTrayReady
 ExecutingPrint
 PrintCompleted
 ExecutingExtractToDrawer
 ExtractToDrawerCompleted
 Started
 Stopped
"""

data2="""
OrderPropRecived
SafetyEventAccure
Oven1Ready
Oven2Ready
Oven3Ready
Oven1Cooking
 Oven2Cooking
 Oven3Cooking
 Oven1ReadyToExtract
 Oven2ReadyToExtract
 Oven3ReadyToExtract
 Res1
 Res2
 Res3
 ACK
 SystemError
"""
lines = data2.split('\n')
prevline = ""
for line in lines:
    ln = line.strip()
    if len(line) == 0:
        continue
    maskName = ln + "Mask"
    print("private static readonly int {0} = BitVector16.CreateMask({1});".format(maskName, prevline)  )
    prevline=maskName

print() # space
print("public BitVector16 state;")
print() # space
print ("#region accessors")
for line in lines:
    ln = line.strip()
    if len(line) == 0:
        continue
    print("public bool {0} => state[{0}Mask];".format(ln))
print ("#endregion accessors")
