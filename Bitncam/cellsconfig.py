import numpy as np

#definitions
CellWidth= 200
CellHeight= 400
ServiceWidth= 400
NoOfColumnAtLeft= 4
NoOfColumnAtRight= 4
NoOfRaw= 4
DeltaYFromTop= 30
CellHeightFromHead= 380

NoOfColumn = NoOfColumnAtLeft + NoOfColumnAtRight
NoOfTotalCells = (int) (NoOfColumn * NoOfRaw)
for i in range(NoOfTotalCells):
    idx = i+1
    innerColumn = ((idx - 1) % NoOfColumn) + 1
    innerRaw =  np.floor ((idx - 1) / NoOfColumn)
    if innerColumn == 0:
        InnerColumn = NoOfColumn
    yPosition = innerRaw * CellHeight + DeltaYFromTop
    if innerColumn <= NoOfColumnAtLeft:
        xPosition = CellWidth * innerColumn - CellWidth / 2
        iD = innerRaw * NoOfColumnAtLeft + innerColumn
        if innerRaw == (NoOfRaw - 1):
            shelfNumber = 0
        else:
            shelfNumber = innerRaw + 1
    else:
        xPosition = CellWidth * innerColumn + ServiceWidth - CellWidth / 2
        iD = innerRaw * NoOfColumnAtRight + innerColumn - NoOfColumnAtLeft + 100
        if innerRaw == (NoOfRaw - 1):
            shelfNumber = 0
        else:
            shelfNumber = innerRaw + NoOfRaw
    height = CellHeightFromHead
    tarr = [int(height), int(xPosition), int(yPosition), int(iD), int(shelfNumber)]
    print("new AppConfigSvc.CellDefinition() {{ HeightMM = {0}, XPosMM = {1}, YPosMM = {2}, cellId = {3}, shelfNumber = {4} }},".format(tarr[0], tarr[1], tarr[2], tarr[3], tarr[4]))
