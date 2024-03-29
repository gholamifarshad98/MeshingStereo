import numpy as np
import Meshing
import cv2
import os
import SSD
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

kernelSize = 15
maxOffset = 30
thicknessOfLayers = 30
currPath = os.getcwd()
changPath = "\\data\\"
currPath = currPath+changPath
print(currPath)
try:
    tempPathL = currPath+"view0.png"
    print(tempPathL)
    imgL = cv2.imread(tempPathL, 0)
    cv2.imshow("Left", imgL)
    tempPathR = currPath+"view1.png"
    print(tempPathR)
    imgR = cv2.imread(tempPathR, 0)
    cv2.line(imgR, (0, 0), (150, 150), (255, 255, 255), 1)
    cv2.imshow("Right", imgR)
except IOError:
    print("the program cant open your image")
    print("every things are done")
height, width = imgL.shape
[MeshingArray, Composition] = Meshing.meshing(height, width, thicknessOfLayers, kernelSize, maxOffset)
x = np.arange(0, 400)
y = np.arange(0, 354)
(x, y) = np.meshgrid(x, y)
z = MeshingArray
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.viridis)
print("hello before go to my_ssd function.")
[temp_mean, temp_var] = SSD.my_ssd(tempPathL, tempPathR, kernelSize, maxOffset, Composition)
print("hello after go to my_ssd function.")
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

