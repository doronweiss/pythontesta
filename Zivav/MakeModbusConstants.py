import sys
sys.path.append('../GeneralUtils')
import words2vars as w2v

data="""
Mode of operation
Command1
Command2
ItemID
OvenID
Fdr1_Portion
Fdr1 _Z start
Fdr1_Zend
Fdr2_Portion
Fdr2 _Z start
Fdr2_Zend
Fdr3_Portion
Fdr3 _Z start
Fdr3_Zend
Z_FeedVelocity
OvnInitialPos
OvnInitialRetrPos
OvnCookingPos
OvnReleasPos
OveApproachingVel
OvenPressVel
OvenRetrieveVel
CookingTime
HeatersEnable
PrntTray_SP
Ovn1_UpperPlateSP
Ovn1_LowerPlateSP
Ovn2_UpperPlateSP
Ovn2_LowerPlateSP
Ovn3_UpperPlateSP
Ovn3_LowerPlateSP
CoolerSP
Motor ID
MotorVelocity
AbsoluteTargetPosition
RelativeDistance
"""

rawlines = data.split('\n')
prevline = ""
lines=w2v.line2Vars(rawlines)
idx=0
for line in lines:
    if len(line) == 0:
        continue
    print("public const int outputIdx_{0} = {1};".format(line, idx))
    idx=idx+1