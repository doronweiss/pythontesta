data="""
UIDefinitions
      SERVER_NO_COMM = 0x0001,
      Main_DISK_FULL = 0x0032,
      USERS_SYNC = 0xFFFF,
      USERS_SYNC_FAILED_3__TIMES = 0xFFEE,
      STATION_ON = 0x1500,
      STATION_RESET = 0x1501,
      RETURN_FULL = 0x0100,
      HOMING_MANUAL = 0x0011,
      CELL_EMPTY = 0x0500,
      ITEM_OUT_OF_STOCK = 0x0550,
      INVENTORY_UNDER_75_PERC = 0x0562,
      INVENTORY_UNDER_50_PERC = 0x0563,
      INVENTORY_UNDER_25_PERC = 0x0564,
      DISPENSE_REFILL = 0x0561,
      INVENTORY_COUNT_REQUEST = 0x0566,
      IOC_COMM_LOST = 0x5033,
      DISPENSING_CELL_BLOCKED = 0x0552,
       IO_CONFIG_MISSING_ERROR = 0x502B,
      INVALID_RFID_SENT_FOR_TRANSACTION = 0x5529,
      SOFTWARE_UPDATE_STARTED = 0x10001,
      SOFTWARE_UPDATE_FINISHED = 0x10002,
      SOFTWARE_UPDATE_FAILD = 0x10003,
      LeftDoorOpen = 0x301,
      RightDoorOpen = 0x302,
      LeftEMO = 0x303,
      RightEMO = 0x304,
      ITEM_DISPENSED_WITHOUT_RFID_CODE = 0xE000,
      EXIT_BIN_BLOCKED = 0x10007
"""


lines = [ln for ln in data.split('\n') if len(ln)>0]
for line in lines:
    if len(line) == 0:
        continue
    parts = line.split('=')
    if len(parts)<2:
        continue
    theKey = parts[1].strip().strip(',')
    theKeynum = int (theKey, 16)
    parts = parts[0].strip().split('_')
    print("<txt  key = \"{0}\" desc = \"\" value = \"{1}\" />".format(hex(theKeynum), ' '.join(parts)))
