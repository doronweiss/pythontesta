import sys
import pathlib as pl
import json
from json import JSONEncoder


class Row:
    def __init__(self):
        self.rowNum=0
        self.direction=0
        self.rowLengthCM=4000
        self.cleanSpeedM2M = 15
        self.omitted=0


class RowsDef:
    def __init__(self) -> object:
        self.rows = []


rd = RowsDef()
for idx in range(1,90):
    r = Row()
    r.rowNum=idx
    r.direction =0 if idx % 2 == 0 else 1
    rd.rows.append(r)

print("has: {0} rows".format(len(rd.rows)))

jsonString = json.JSONEncoder().encode(rd)
print (jsonString)
