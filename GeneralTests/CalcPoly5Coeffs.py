import os, sys
import numpy as np
import matplotlib.pyplot as plt

xs=[]
ys=[]
b0=[]
b1=[]
b2=[]
b3=[]
b4=[]
b5=[]

fileName = r'c:\Projects\Servotronix\tries\Coeffs\CAM1.CSV'
try:
    fi = open (fileName,'r',encoding='Windows-1252',errors='replace')
except:
    print ("Could not open file: {0}".format(fileName))
    sys.exit()
ln = fi.readline()
#try:
while ln and ln != "":
    parts = [x for x in ln.split(',') if x]
    xs.append(float(parts[0]))
    ys.append(float(parts[1]))
    ln = fi.readline()
#except:
 #   print ("Exception on line: {0}".format(lnidx))
fi.close();
plt.plot(xs, ys)
plt.ylabel('Data')
plt.show()
