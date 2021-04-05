import sys
import xml.etree.ElementTree as ET

# https://docs.python.org/2/library/xml.etree.elementtree.html#module-xml.etree.ElementTree
fpath='c:/Users/User/AppData/Local/servotronix/SoftMC Configurator/ConfigPackages/0.4.18.2/robots/standard/pumaprops.xml'
try:
    tree = ET.parse(fpath)
except:
    print("Could not load file {0}".format(fpath))
    sys.exit(-1)

root = tree.getroot()
delta = root.findall ('./robotgeneralprops/dhparams')
if delta is not None:
    for dp in delta[0]:
        print ("name %s  value  %s"%(dp.tag, dp.attrib['value']))

