import sys
import xml.etree.ElementTree as ET

fpath='c:/temp/ptest/carconfig.xml'
fpatho='c:/temp/ptest/carconfigout.xml'
try:
    tree = ET.parse(fpath)
except Exception as e:
    print("Could not load file {0}, {1}".format(fpath, e ))
    sys.exit(-1)
root = tree.getroot()

# change protocol from UDP => TCP
protocol = root.find ('./PlcParams/protocol')
if protocol is not None:
    protocol.text="TCP"

# if delta is not None:
#     for dp in delta:
#         dp.text = "{0}".format(6.0*float(dp.text))
#         print ("name {0}".format(dp.text))

try:
    tree.write(fpatho)
except Exception as e:
    print("Could not save  file {0}, {1}".format(fpath, e ))
    sys.exit(-1)
