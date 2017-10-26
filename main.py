import numpy as np
from matplotlib import pyplot as plt
class Point:
    def __init__(self, x, y, theta, radius):
        self.x =x
        self.y = y
        self.theta = theta
        self.radius = radius
    def nextTwoPoints(self):
        x1 = self.x + self.radius * np.cos(self.theta + 0.25 * np.pi)
        y1 = self.y + self.radius * np.sin(self.theta + 0.25 * np.pi)
        theta1 = self.theta + 0.25 * np.pi
        p1 = Point(x1,y1,theta1,self.radius)
        x2 = self.x + self.radius * np.cos(self.theta - 0.25 * np.pi)
        y2 = self.y + self.radius * np.sin(self.theta - 0.25 * np.pi)
        theta2 = self.theta - 0.25 * np.pi
        p2 = Point(x2, y2, theta2, self.radius)
        return p1,p2


    def getY(self):
        return self.y
    def getTheta(self):
        return self.theta
    def getX(self):
        return self.x
    def getRadius(self):
        return self.radius

    def isEqual(self, pointtest):
        if(pointtest.getX()==self.x):
            if(pointtest.getY() == self.y):
                return True
        return False
    def inRadius(self, pointtest):
        dxpower = np.power(self.x - pointtest.getX(),2)
        dypower = np.power(self.y - pointtest.getY(),2)
        quadsum = dxpower + dypower
        if quadsum < np.power(self.radius,2):
            return True
        return False
def getFourPoints(point1):
    radiushalve = 0.5 * point1.getRadius()
    x1, y1 = transformMatrix(-1,  1,point1.getTheta(),radiushalve)
    x2, y2 = transformMatrix( 1,  1, point1.getTheta(),radiushalve)
    x3, y3 = transformMatrix( 1, -1, point1.getTheta(),radiushalve)
    x4, y4 = transformMatrix(-1, -1, point1.getTheta(),radiushalve)
    x1 += point1.getX()
    x2 += point1.getX()
    x3 += point1.getX()
    x4 += point1.getX()
    xarray = np.array([x1,x2,x3,x4,x1])
    y1 += point1.getY()
    y2 += point1.getY()
    y3 += point1.getY()
    y4 += point1.getY()
    yarray = np.array([y1,y2,y3,y4,y1])

    return xarray, yarray


def transformMatrix(x, y, rot, radius):
    x1 = radius*(x * np.cos(rot) - y * np.sin(rot))
    y1 = radius*(x * np.sin(rot) + y * np.cos(rot))
    return x1, y1
def generatingPoints(x0, y0, theta0, radius, iterations):
    totallist = []
    templist = []
    currentpoints = []
    a = Point(x0,y0,theta0,radius)
    currentpoints.append(a)
    totallist.append(a)
    for i in range(0,iterations-1):
        for lol in currentpoints:
            var1 = True
            var2 = True
            point1a = lol.nextTwoPoints()[0]
            point1b = lol.nextTwoPoints()[1]
            for j in range(0,len(currentpoints)):
                if(currentpoints[j].inRadius(point1a)):
                    var1 = False
                if(currentpoints[j].inRadius(point1b)):
                    var2 = False
            if(var1):
                templist.append(lol.nextTwoPoints()[0])
                totallist.append(lol.nextTwoPoints()[0])
            if(var2):
                templist.append(lol.nextTwoPoints()[1])
                totallist.append(lol.nextTwoPoints()[1])
        currentpoints = templist
        templist = []

    xarray = np.zeros(len(totallist))
    yarray = np.zeros(len(totallist))
    tarray = np.zeros(len(totallist))

    for i in range(0,len(totallist)):
        xarray[i] = totallist[i].getX()
        yarray[i] = totallist[i].getY();
        tarray[i] = totallist[i].getTheta();

    return xarray,yarray,tarray
def generateSquares(point1, iterations):

    xarray, yarray, tarray = generatingPoints(point1.getX(), point1.getY(), point1.getTheta(),point1.getRadius(), iterations)
    plt.figure()
    plt.plot(xarray,yarray, 'ro')
    for i in range(0,len(xarray)):
        xsquare, ysquare = getFourPoints(Point(xarray[i],yarray[i],tarray[i],point1.getRadius()))
        plt.plot(xsquare,ysquare)
    plt.show()
point1 = Point(0,0,0,0)
point2 = Point(1,0,0,0)
print(str(point1.isEqual(point2)))
p1 = Point(0,0,0.5*np.pi, 10)
generateSquares(p1, 2)
