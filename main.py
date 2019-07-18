import numpy as np
import Meshing
import cv2
import os
import SSD
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D


currPath = os.getcwd()
changPath = "\\data\\"
currPath = currPath+changPath
print(currPath)
try:
    tempPathL = currPath+"Pic_R.png"
    print(tempPathL)
    imgL = cv2.imread(tempPathL, 0)
    cv2.imshow("Left", imgL)
    tempPathR = currPath+"Pic_L.png"
    print(tempPathR)
    imgR = cv2.imread(tempPathR, 0)
    cv2.line(imgR, (0, 0), (150, 150), (255, 255, 255), 15)
    cv2.imshow("Right", imgR)
except IOError:
    print("the program cant open your image")
    print("every things are done")


[MeshingArray, Composition] = Meshing.meshing(40, 60, 4)
print(MeshingArray)
x = np.arange(0, 60)
y = np.arange(0, 40)
(x,y)= np.meshgrid(x,y)
z = MeshingArray
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.viridis)
plt.show()
SSD.my_ssd(tempPathL, tempPathR, 15, 30)
cv2.waitKey(0)
cv2.destroyAllWindows()

