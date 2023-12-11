import os, sys
import numpy as np
#import matplotlib.pyplot as plt



fileName = r'c:\temp\traj.out'
try:
    fi = open (fileName,'w') #,encoding='Windows-1252',errors='replace')
except:
    print ("Could not open file: {0}".format(fileName))
    sys.exit()
fi.write("time, x, y, z, vx, vy, vz, alt\n")
d2r = 3.1415926 / 180
g = 9.81
v0=1000
angle=30*d2r
for i in range(10000):
    time = i/100.0
    x = v0*np.cos(angle)*time
    y = np.sin(time/10.0)
    z = v0*np.sin(angle)*time - 0.5*g*time*time
    vx=np.cos(angle)
    vy=np.cos(time/10.0)
    vz=v0 - g*time
    alt = z
    fi.write("{0} {1} {2} {3} {4} {5} {6} {7}\n".format(time, x, y, z, vx, vy, vz, alt))
fi.close()
