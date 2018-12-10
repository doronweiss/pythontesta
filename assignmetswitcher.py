import string

data="""
      resolutionNUD.Value = (int)profCfg.resolution;
      bufferCountNUD.Value = (int)profCfg.bufferCount;
      packetSizeNUD.Value = (int)profCfg.packetSize;
      shutterTimeNUD.Value = (int)profCfg.shutterTime;
      idleTimeNUD.Value = (int)profCfg.idleTime;
      measDataThresholdNUD.Value = (int)profCfg.measDataThreshold;
      laserPowerNUD.Value = (int)profCfg.laserPower;
      measurmentFieldNUD.Value = (int)profCfg.measurmentField;
      profileDataNUD.Value = (int)profCfg.profileData;
      maintenanceFunctionsNUD.Value = (int)profCfg.maintenanceFunctions;
      profileFilterNUD.Value = (int)profCfg.profileFilter;
      sharpnessNUD.Value = (int)profCfg.sharpness;
      mainReflectionNUD.Value = (int)profCfg.mainReflection;
"""

data2="""
visLotNumber
visResultID
visDateTime
visResult
visJigNumber
visBottomLuerAdhesiveTestPass
visLeftLuerAdhesiveTestPass
visRightLuerAdhesiveTestPass
visPositionsMidTiptoJigDistance
visPositionsChipYPosition
visPositionsChipAngle
visPositionsTestPass
visPositionsOuterTipsDistance
visChipExcessAdhesivePercentage
visChipExcessAdhesiveTestPass
visChipMissingAdhesiveTestPass
visLateralAdhesiveShortageTestPass
visLateralAdhesiveShortageTestDone
visLeftNeedleCleanLength
visMiddleNeedleCleanLength
visRightNeedleCleanLength
visNeedleCleanLengthTestPass
visYZAngle
visYZAngleTestPass
visYZAngleTestDone
visSideAdhesiveToTipHeightLeft
visSideAdhesiveToTipHeightRight
visSideAdhesiveToTipHeightTestPass
visSideAdhesiveToTipHeightTestDone
visTipsOKTestPass
visFrontAdhesiveTestPass
visTopCamHighExposureSavedImagePath
visTopCamLowExposureSavedImagePath
visSideCamBacklightSavedImagePath
visSideCamCoaxLightSavedImagePath
visResultComments
"""

def assignmentChanger (str):
    lines = str.split('\n')
    for line in lines:
        if len(line)==0:
            continue
        line = line.replace(';','')
        parts=line.split ('=')
        print ("%s=%s;"%(parts[1], parts[0]))

def nanopassAssigner (str):
    lines = str.split('\n')
    for line in lines:
        if len(line)==0:
            continue
        print ("%s=vValid? visData.%s : \"\", "%(line,line))


#nanopassAssigner(data2)
assignmentChanger(data)
