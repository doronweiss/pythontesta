import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread(r'c:\temp\batata.png',cv2.IMREAD_COLOR)
height, width, chans = img.shape
sw=width/4
sh=height/4
ew=sw*3
eh=sh*3
cv2.rectangle(img, (int(sw),int(sh)), (int(ew),int(eh)), (0,0,255),3)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.show()