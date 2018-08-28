import string

data="""
      redSetter.value = plansMgr.currDisplayed.red;
      greenSetter.value = plansMgr.currDisplayed.green;
      whiteSetter.value = plansMgr.currDisplayed.white;
      blueSetter.value = plansMgr.currDisplayed.blue;
      centerSetter.value = plansMgr.currDisplayed.center;
      dimmingSetter.value = plansMgr.currDisplayed.dimmingPercent;
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


nanopassAssigner(data2)
