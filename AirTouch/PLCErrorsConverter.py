import sys

data="""
Description,Type,Name,value
emergency circuit broken during operation,1,EmergencyCircuit,1
trolley motor at error,1,TrolleyMotor,2
angle motor at error,1,AngleMotor,3
approach motor at error,1,ApproachMotor,4
column motor at error,1,ColumnMotor,5
Trolley failed to reach target - TO,1,TrolleyTO,11
Angle failed to reach target - TO,1,AngleTO,12
Approach failed to reach target - TO,1,ApproachTO,13
Column failed to reach target - TO,1,ColumnTO,14
homing time-out,-1,HomingTO,21
Find the row (go to target) time-out,2,GoToTargetTO,22
Engage (Search + final attach) panel time-out,2,EngageTO,23
Disangage time-out,2,DisangageTO,24
Prepare time out,-1,PrepareTO,25
Search time out (this sequence is part of Engage sequence),1,SearchTO,26
can not start any sequence - need to do homing first,-1,HomeIsMissing,101
can not move trolley - approach not at center (need to disengage first),-1,ApproachNotAtCenter,102
need to do prepare first (Only relevant when operating through a HMI),-1,PrepareIsMissingInSearch,103
can not start final attach - need to do search for panel first,-1,AtErrorFromSearchInFinalAttach,104
can not start engage - trolley not at target,,TrolleyNotAtTarget,105
can not start search sequence - the front antenna analog value is over idel level ,1,FrontAntennaNotAtIdel,105
can not start search sequence - the Rear antenna analog value is over idel level ,1,BackAntennaNotAtIdel,106
can not start search sequence - the front attached sensor is ON ,1,FrontAttachedNotAtIdel,107
can not start search sequence - the Rear attached sensor is ON ,1,RearAttachedNotAtIdel,108
can not start search sequence - the front fiexd(digital wheel) sensor is ON ,1,FrontFixedNotAtIdel,109
can not start search sequence - the Rear fiexd(analog wheel) sensor is over the engage position,1,RearFixedNotAtIdel,110
column reached max limit allowed for this row,2,ColumnTooHigh,201
angle actual position is out of software limits,2,AngleOutOfLimits,202
atleast one of the antenna sensor is out of allowed range,,AntennaSensorOutOfRange,203
approach reach the limit allowad for this row and did not find the panel,3,ApproachOutOfRange,204
attach sensor in the front level is missing(only Rear sensor is ON),,AttachSensFrontIsMissing,205
attach sensor in the Rear level is missing(only front sensor is ON),,AttachSensRearIsMissing,206
trolley target is out of limits,3,TrolleyTargetOutOfLimit,207
column actual position crossed the up limit (hard stop),3,ColumnOutOfLimits,208
attached sensor is on during homing,5,HomeAngleInterference,209
attached sensor is on during homing,5,HomeApproachInterference,210
attached sensor is on during homing,5,HomeColumnInterference,211
attached sensor is on during homing,5,HomeTrolleyInterference,212
the antenna sensor meets the panel while the approach moves to target target,3,ApproachTargetTooCloseToPanel,213
angle at one of the sensors limit,,AngleAtHardLimit,214
the angle is dancing around the panel - can not stabilizing on the panel,,AngleCanNotAlignToPanel,215
the trolley did not find the row flag,3,TrolleyFlagIsMissing,221
idel wheel stuck - the encoder (4 ppr) not moving ,5,TrolleyWheelStuck,222
idel wheel slide - the encoder (4 ppr) rotates slowly compared to the driven wheel,5,TrolleyWheelSlid,223
"""

lines = [ln for ln in data.split('\n') if len(ln)>0]
for line in lines:
    if len(line) == 0:
        continue
lines = [ln for ln in data.split('\n') if len(ln)>0]
for line in lines:
    if len(line) == 0:
        continue
    parts = line.split(',')
    if len(parts)!=4:
        print ("Parse error in line: {0}".format(line))
        sys.exit(0)
    print("{0}, {1}, {2}, {3} ".format(parts[3], parts[1], parts[2], parts[0]))
    maskName = parts[0].strip().strip(',')
