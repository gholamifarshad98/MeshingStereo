import numpy
import math


def calculate_distance(r, c):
    return math.sqrt(r ** 2 + c ** 2)


def calculate_layer(distance, thickness):
    return int(distance/thickness)


def meshing(NumOfRow, NumOfColumn, NumOfThickness,kernelSize, maxOffset):
    allowableRow = [i for i in range(int(kernelSize / 2), NumOfRow - int(kernelSize / 2)-2)]
    allowableColumn = [i for i in range(int(kernelSize / 2), NumOfColumn - maxOffset - int(kernelSize / 2)-2)]
    print(allowableRow)
    print(allowableColumn)
    NumOfLayer = int(math.sqrt((NumOfRow-kernelSize) ** 2 + ((NumOfColumn-kernelSize) / 2) ** 2) / NumOfThickness)+1
    print(NumOfLayer)
    print("the NumOfLayer is ", NumOfLayer)
    tempMatrix = numpy.zeros((NumOfRow, NumOfColumn))
    compositionList = []
    for n in range(0, NumOfLayer):
        compositionList.append([])
        # print(CompositionList)
    for i in allowableRow:
        for j in allowableColumn:
            print((i,j))
            tempDistance = calculate_distance((NumOfRow-1-i), (NumOfColumn/2-0.5-j))
            # print(tempDistance)
            tempLayer = calculate_layer(tempDistance, NumOfThickness)
            tempMatrix[i][j] = tempLayer
            # print(tempLayer)
            # print(compositionList)
            # print(len(compositionList))
            compositionList[int(tempLayer)-1].append((i, j))
    return [tempMatrix, compositionList]
