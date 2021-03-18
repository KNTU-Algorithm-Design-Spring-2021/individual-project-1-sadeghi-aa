import matplotlib.pyplot as plt
import random as rand


numPoints = 100

pointsX = [rand.random() for ix in range(numPoints)]
pointsY = [rand.random() for iy in range(numPoints)]

# points = [(1, 2), (1, 3), (2, 0.5)]
#
# pointsX = [point[0] for point in points]
# pointsY = [point[1] for point in points]

bestMinX = min(pointsX[0], pointsX[1])
bestMaxX = max(pointsX[0], pointsX[1])
bestMinY = min(pointsY[0], pointsY[1])
bestMaxY = max(pointsY[0], pointsY[1])

length = len(pointsX)
numPairs = length // 2

for pairIndex in range(1, numPairs):
    curMinX = min(pointsX[2 * pairIndex], pointsX[2 * pairIndex + 1])
    curMaxX = max(pointsX[2 * pairIndex], pointsX[2 * pairIndex + 1])
    curMinY = min(pointsY[2 * pairIndex], pointsY[2 * pairIndex + 1])
    curMaxY = max(pointsY[2 * pairIndex], pointsY[2 * pairIndex + 1])

    if curMinX < bestMinX:
        bestMinX = curMinX
    if curMaxX > bestMaxX:
        bestMaxX = curMaxX
    if curMinY < bestMinY:
        bestMinY = curMinY
    if curMaxY > bestMaxY:
        bestMaxY = curMaxY

if length % 2 == 1:
    if pointsX[-1] > bestMaxX:
        bestMaxX = pointsX[-1]
    elif pointsX[-1] < bestMinX:
        bestMinX = pointsX[-1]
    if pointsY[-1] > bestMaxY:
        bestMaxY = pointsY[-1]
    elif pointsY[-1] < bestMinY:
        bestMinY = pointsY[-1]

plt.scatter(pointsX, pointsY)
plt.hlines(bestMaxY, bestMinX, bestMaxX, 'r')
plt.hlines(bestMinY, bestMinX, bestMaxX, 'r')
plt.vlines(bestMinX, bestMinY, bestMaxY, 'r')
plt.vlines(bestMaxX, bestMinY, bestMaxY, 'r')
plt.show()