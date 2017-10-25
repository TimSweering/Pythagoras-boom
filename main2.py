
import numpy as np
from matplotlib import pyplot as plt

class Point:
    def __init__(self, x, y, theta, sidelength):
        self.x = x
        self.y = y
        self.theta = theta
        self.sidelength = sidelength
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getTheta(self):
        return self.theta
    def getSideLength(self):
        return self.sidelength
    def translateCenter(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
    def setCoordinate(self, newx, newy):
        self.x = newx
        self.y = newy
    def rotateCenter(self, dtheta):
        self.theta = self.theta + dtheta
    def getSquare(self):
        x1 = - 0.5 * self.sidelength
        x2 =  0.5 * self.sidelength
        x3 =  0.5 * self.sidelength
        x4 = - 0.5 * self.sidelength
        xlocalarray = np.array([x1, x2, x3, x4, x1])
        xarray = np.zeros(5)
        y1 = 0.5 * self.sidelength
        y2 = 0.5 * self.sidelength
        y3 = -0.5 * self.sidelength
        y4 = -0.5 * self.sidelength
        ylocalarray = np.array([y1,y2,y3,y4,y1])
        yarray = np.zeros(5)
        for i in range(0,5):
            xarray[i] = np.cos(self.theta) * xlocalarray[i] - np.sin(self.theta) * ylocalarray[i]
            yarray[i] = np.sin(self.theta) * xlocalarray[i] + np.cos(self.theta) * ylocalarray[i]
        xarray += self.x
        yarray += self.y
        return xarray, yarray
    def createTwoNewCentersLocal(self):
        x1local = - 0.5 * self.sidelength
        y1local =  self.sidelength
        theta1local = 0.25 * np.pi
        sidelength1local = 0.5 * np.sqrt(2) * self.sidelength
        point1local = Point(x1local,y1local,theta1local,sidelength1local)
        x2local = 0.5 * self.sidelength
        y2local = self.sidelength
        theta2local = - 0.25 * np.pi
        sidelength2local = 0.5 * np.sqrt(2) * self.sidelength
        point2local = Point (x2local,y2local,theta2local,sidelength2local)
        return point1local, point2local
    def rotateTwoNewCenters(self, p1, p2):
        xtemp = np.cos(self.theta) * p1.getX() - np.sin(self.theta) * p1.getY()
        ytemp = np.sin(self.theta) * p1.getX() + np.cos(self.theta) * p1.getY()
        p1.setCoordinate(xtemp, ytemp)
        xtemp = np.cos(self.theta) * p2.getX() - np.sin(self.theta) * p2.getY()
        ytemp = np.sin(self.theta) * p2.getX() + np.cos(self.theta) * p2.getY()
        p2.setCoordinate(xtemp, ytemp)
        return p1,p2
    def getChild(self):
        p1, p2 = self.createTwoNewCentersLocal()
        p1, p2 = self.rotateTwoNewCenters(p1, p2)
        p1.translateCenter(self.x, self.y)

        p1.rotateCenter(self.theta)
        p2.translateCenter(self.x, self.y)
        p2.rotateCenter(self.theta)
        return p1,p2


def generatePoints(point1, iterations):
    pointlist = [point1]
    outerlist = [point1]

    for i in range(0, iterations):
        templist = []
        for point in outerlist:
            p1,p2 = point.getChild()
            templist.append(p1)
            templist.append(p2)
            pointlist.append(p1)
            pointlist.append(p2)
        outerlist = templist
    return pointlist
def plotSquares(pointlist):
    plt.figure()
    for point in pointlist:
        x, y = point.getSquare()
        plt.plot(x,y)
    plt.show()



point1 = Point(0,0,0,5)
listpoints = generatePoints(point1, 7)
plotSquares(listpoints)



