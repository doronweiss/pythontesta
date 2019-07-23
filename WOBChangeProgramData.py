import sys
import xml.etree.ElementTree as ET

# https://docs.python.org/2/library/xml.etree.elementtree.html#module-xml.etree.ElementTree
#fpath='c:/Users/User/AppData/Local/servotronix/SoftMC Configurator/ConfigPackages/0.4.18.2/robots/standard/pumaprops.xml'
fpath='c:/Projects/Weldobot/tries/plan/workplan.wpln'
fpatho='c:/Projects/Weldobot/tries/plan/workplano.wpln'
try:
    tree = ET.parse(fpath)
except Exception as e:
    print("Could not load file {0}, {1}".format(fpath, e ))
    sys.exit(-1)

root = tree.getroot()
delta = root.findall ('./passes/Pass/sections/Section/motionParameters/travelSpeedCMpM')
if delta is not None:
    for dp in delta:
        dp.text = "{0}".format(6.0*float(dp.text))
        print ("name {0}".format(dp.text))

try:
    tree.write(fpatho)
except Exception as e:
    print("Could not save  file {0}, {1}".format(fpath, e ))
    sys.exit(-1)
