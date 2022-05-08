import re

data = """1, Safety (E.Stop)
2, Major Temp Ctrl
3, Purge Error
4, Feeder 1 Error
5, Feeder 2 Error
6, Feeder 3 Error
7, Oven 1 Error
8, Oven 2 Error
9, Oven 3 Error
10, Print Tray Error
11, Homing Error
12, Axis (Any) Error
13, Missing Turkey
14, Missing Pork
15, res1
16, res2
17, Ovens Temperature Error 2 Min
18, Ovens Temperature Error 15 Min
19, Refrigerator Temperature Error
20, Feeder Refill
21, Ready to Open Feeder
22, Oven 1 Ready
23, Oven 2 Ready
24, Oven 3 Ready
25, Missing Classic
26, Missing Sporty
27, Missing Chef
28, Expired Cartridge (Feeder 1)
29, Expired Cartridge (Feeder 2)
30, Expired Cartridge (Feeder 3)
31, Oven in Sleeping Mode
32, Expect Classic Replacement
33, Expect Sporty Replacement
34, Expect Chef Replacement
35, Expect Turkey Replacement
36, Expect Pork Replacement
"""

if __name__ == "__main__":
    rx = "SW\.+[0-9]+"
    lines = data.split('\n')
    for line in lines:
        #print (line)
        parts = [ln for ln in line.split(',') if len(ln) > 0]
        warnNum = parts[0]
        warnStr = parts[1].replace(" ", "")
        print('const int {0} = {1};'.format(warnStr, warnNum))
