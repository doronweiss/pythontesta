import math
from math import *
import numpy as np
import matplotlib.pyplot as plt

# https://www.pveducation.org/pvcdrom/properties-of-sunlight/elevation-angle
# https://www.pveducation.org/pvcdrom/properties-of-sunlight/declination-angle
hours=range(25)
latitude = radians(31.240239)
longitude = radians(34.454592)
earthTilt = radians(23.45)
HRA = radians(-90.0)
dayOfYear = 90

for i in hours:
    print("Hour= {}".format(i))


# calc
currDeclination = -earthTilt * cos(360.0/365.0 * (dayOfYear+10.0))
aux = sin(currDeclination)*sin(latitude) + cos(currDeclination)*cos(latitude)*cos(HRA)
sunElev = asin(aux)

print ("currDeclination={0}, elevation={1}".format(degrees(currDeclination),degrees(sunElev)))
