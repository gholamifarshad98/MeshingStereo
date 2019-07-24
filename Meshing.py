import numpy
import math


def calculate_distance(r, c):
    return math.sqrt(r ** 2 + c ** 2)


def calculate_layer(distance, thickness):
    return int(distance/thickness)+1


def meshing(NumOfRow, NumOfColumn, NumOfThickness):
    NumOfLayer = int(math.sqrt(NumOfRow ** 2 + (NumOfColumn / 2) ** 2) / NumOfThickness) +2
    print("the NumOfLayer is ",NumOfLayer)
    tempMatrix = numpy.zeros((NumOfRow, NumOfColumn))
    CompositionList = []
    for n in range(1, NumOfLayer):
        CompositionList.append([])
        #print(CompositionList)
    for i in range(0, NumOfRow):
        for j in range(0, NumOfColumn):
            tempDistance = calculate_distance((NumOfRow-1-i), (NumOfColumn/2-0.5-j))
            tempLayer = calculate_layer(tempDistance, NumOfThickness)
            tempMatrix[i][j] = tempLayer
            CompositionList[int(tempLayer)-1].append((i, j))
    return [tempMatrix,CompositionList]
