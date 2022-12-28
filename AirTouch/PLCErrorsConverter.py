import sys

data="""
1,1,EmergencyCircuit,emergency circuit broken during operation
1,2,TrolleyMotor,trolley motor at error
1,3,AngleMotor,angle motor at error
1,4,ApproachMotor,approach motor at error
1,5,ColumnMotor,column motor at error
1,11,TrolleyTO,Trolley failed to reach target - TO
1,12,AngleTO,Angle failed to reach target - TO
1,13,ApproachTO,Approach failed to reach target - TO
1,14,ColumnTO,Column failed to reach target - TO
1,21,HomingTO,homing time-out
2,22,GoToTargetTO,Find the row (go to target) time-out
2,23,EngageTO,Engage (Search + final attach) panel time-out
2,24,DisangageTO,Disangage time-out
1,25,PrepareTO,Prepare time out
1,26,SearchTO,Search time out (this sequence is part of Engage sequence)
1,27,FinalAttachedTO,Final Attached time out (this sequence is part of Engage sequence)
1,101,HomeIsMissing,can not start any sequence - need to do homing first
1,102,ApproachNotAtCenter,can not move trolley - approach not at center (need to disengage first)
1,103,PrepareIsMissingInSearch,need to do prepare first (Only relevant when operating through a HMI)
1,104,AtErrorFromSearchInFinalAttach,can not start final attach - need to do search for panel first
,105,TrolleyNotAtTarget,can not start engage - trolley not at target
1,105,FrontAntennaNotAtIdel,can not start search sequence - the front antenna analog value is over idel level 
1,106,BackAntennaNotAtIdel,can not start search sequence - the Rear antenna analog value is over idel level 
1,107,FrontAttachedNotAtIdel,can not start search sequence - the front attached sensor is ON 
1,108,RearAttachedNotAtIdel,can not start search sequence - the Rear attached sensor is ON 
1,109,FrontFixedNotAtIdel,can not start search sequence - the front fiexd(digital wheel) sensor is ON 
1,110,RearFixedNotAtIdel,can not start search sequence - the Rear fiexd(analog wheel) sensor is over the engage position
1,111,NotAtAutoMode,can not start - change to auto mode first
2,201,ColumnTooHigh,column reached max limit allowed for this row
2,202,AngleOutOfLimits,angle actual position is out of software limits
1,203,AntennaSensorOutOfRange,atleast one of the antenna sensor is out of allowed range
3,204,ApproachOutOfRange,approach reach the limit allowad for this row and did not find the panel
1,205,AttachSensFrontIsMissing,attach sensor in the front level is missing(only Rear sensor is ON)
1,206,AttachSensRearIsMissing,attach sensor in the Rear level is missing(only front sensor is ON)
3,207,TrolleyTargetOutOfLimit,trolley target is out of limits
3,208,ColumnOutOfLimits,column actual position crossed the up limit (hard stop)
5,209,HomeAngleInterference,attached sensor is on during homing
5,210,HomeApproachInterference,attached sensor is on during homing
5,211,HomeColumnInterference,attached sensor is on during homing
5,212,HomeTrolleyInterference,attached sensor is on during homing
3,213,ApproachTargetTooCloseToPanel,the antenna sensor meets the panel while the approach moves to target target
1,214,AngleAtHardLimit,angle at one of the sensors limit
1,215,AngleCanNotAlignToPanel,the angle is dancing around the panel - can not stabilizing on the panel
2,216,TheSecondFixSensorCanNotFound,the trolley could not find the second fix sensor after search for xx mm 
1,217,AnalogFixSensorCanNotReachedZeroPos,the trolley could not reached the zero position of the analog fix sensor after search for xx mm 
3,221,TrolleyFlagIsMissing,the trolley did not find the row flag
5,222,TrolleyWheelStuck,idel wheel stuck - the encoder (4 ppr) not moving 
5,223,TrolleyWheelSlid,idel wheel slide - the encoder (4 ppr) rotates slowly compared to the driven wheel
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
    print("{0}, {1}, {2}, {3} ".format(parts[1], parts[0], parts[2], parts[3]))
    maskName = parts[0].strip().strip(',')
