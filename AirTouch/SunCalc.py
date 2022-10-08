import math
from math import *
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt

# https://www.pveducation.org/pvcdrom/properties-of-sunlight/elevation-angle
# https://www.pveducation.org/pvcdrom/properties-of-sunlight/declination-angle
latitude = radians(31.240239)
longitude = radians(34.454592)
earthTilt = radians(23.45)
#HRA = radians(-90.0)
dayOfYear = 90

# calc
def calcAngle (HRA):
    currDeclination = -earthTilt * cos(360.0/365.0 * (dayOfYear+10.0))
    aux = sin(currDeclination)*sin(latitude) + cos(currDeclination)*cos(latitude)*cos(HRA)
    return asin(aux)


hours=range(25)
angles = [degrees(calcAngle(radians(15*h))) for h in hours]
fig = px.line(x=hours, y=angles, title='Sun angle through the day')
fig.show()

