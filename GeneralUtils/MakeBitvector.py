import words2vars as w2v
# lowLevelSensorStatusA1
# lowLevelSensorStatusA2
# lowLevelSensorStatusB1
# lowLevelSensorStatusB2
# barrelIsAboutToBeEmptyA1
# barrelIsAboutToBeEmptyA2
# barrelIsAboutToBeEmptyB1
# barrelIsAboutToBeEmptyB2
# barrelReplaceCommandStatusA1
# barrelReplaceCommandStatusA2
# barrelReplaceCommandStatusB1
# barrelReplaceCommandStatusB2
# barrelReplacedA1
# barrelReplacedA2
# barrelReplacedB1
# barrelReplacedB2
# """

data="""
    mixerStatusA1
    mixerStatusA2
    pumpStatusA1
    pumpStatusA2
    pumpStatusB1
    pumpStatusB2
    pumpRunCommandForBleedingStatusA2
    pumpRunCommandForBleedingStatusA1
    bleedingPushButtonStatusA1
    bleedingPushButtonStatusA2
    bleedingValveStatusA1
    bleedingValveStatusA2
"""

rawlines = data.split('\n')
prevline = ""
lines=w2v.line2Vars(rawlines,  "SW\.+[0-9]+")
for line in lines:
    if len(line) == 0:
        continue
    maskName = line + "Mask"
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
