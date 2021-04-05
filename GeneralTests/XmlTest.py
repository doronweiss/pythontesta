import sys
import xml.etree.ElementTree as ET

fpath='c:/Projects/Weldobot/temp/workplan.wpln'
try:
    tree = ET.parse(fpath)
except Exception as e:
    print("Could not load file {0}, {1}".format(fpath, e ))
    sys.exit(-1)

fileRoot = tree.getroot()
dataRoot = fileRoot[0]
cmds = dataRoot.findall ('command')
if cmds is not None:
    for cmd in cmds:
        args = cmd.find ('./argument')
        if args is not None:
            print ("Args =  {0}".format(args.text.strip()))
