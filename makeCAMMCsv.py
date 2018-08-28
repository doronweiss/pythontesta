import sys
import numpy as np


try:
    fi = open ("c:\\temp\\cam.csv",'w') # ,encoding='Windows-1252',errors='replace')
except:
    print ("Could not open file")
    sys.exit()
r=range(100)
for i in r:
    fi.write("{0},{1}\n".format(i/10, np.sin(i/10)))
fi.close()