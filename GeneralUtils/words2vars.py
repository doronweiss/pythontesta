import re

data = """
Reserved CW
Mode of operation
Command
Reserved  commands 2
Item ID
Oven ID
Feeder 1 portion
Feeder 2 portion
Feeder 3 portion
Cooking time
Upper plate position
Print tray SP
Heater 1 upper plate SP
Heater 1 lower plate SP
Heater 2 upper plate SP
Heater 2 lower plate SP
Heater 3 upper plate SP
Heater 3 lower plate SP
Empty
Motor ID
Motor velocity
Absolute Target position
Relative Distance
"""


def line2Vars(lines, rx=""):
    vars = []
    for line in lines:
        if len(line.strip()) == 0:
            continue
        nln = re.sub(rx, '', line.strip()) if rx != "" else line.strip()
        parts = [ln.capitalize() for ln in nln.split(' ') if len(ln) > 0]
        res = ''.join(parts)
        # print (res)
        vars.append(res)
    return vars

if __name__ == "__main__":
    rx = "SW\.+[0-9]+"
    lines = data.split('\n')
    res = line2Vars(lines, rx)
    for str in res:
        print(str)
