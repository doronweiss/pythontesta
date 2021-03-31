import words2vars as w2v

data="""
SW.0 Feeder 1 refill completed
SW.1 Feeder 2 refill completed
SW.2 Feeder 3 refill completed
SW.3 Feeder 1 purge completed
SW.4 Feeder 2 purge completed
SW.5 Feeder 3 purge completed
SW.6 res1
SW.7 res2
SW.8 res3
SW.9 res4
SW.10 res5
SW.11 res6
SW.12 res7
SW.13 res8
SW.14 res9
SW.15 res10
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
