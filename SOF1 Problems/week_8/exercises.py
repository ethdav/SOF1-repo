"""
Lab exercises for week 8
Author: Ethan Davis
"""
import math

class Circle:
    """Class Circle
    """
    def __init__(self, x=0, y=0, radius=0.0):
        self.centre = (x, y)
        self.radius = radius
    
    def __str__(self):
        return "c = " + self.centre + ", r = " + self.radius
    
    def setx(self, x):
        self.centre = (x, self.centre[1])

    def sety(self, y):
        self.centre = (self.centre[0], y)

    def getArea(self):
        return 3.14159 * (self.radius)**2
    
    def getPerimeter(self):
        return 2 * 3.14159 * self.radius
    
class Triangle:
    def __init__(self, vert1, vert2, vert3):
        self.vert1 = vert1
        self.vert2 = vert2
        self.vert3 = vert3

    def getArea(self):
        x1, y1 = self.vert1
        x2, y2 = self.vert2
        x3, y3 = self.vert3
        area = abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2
        return area
    
    def getPerimeter(self):
        x1, y1 = self.vert1
        x2, y2 = self.vert2
        x3, y3 = self.vert3
        side12 = math.sqrt((x2-x1)**2+(y2-y1)**2)
        side23 = math.sqrt((x3-x2)**2+(y3-y2)**2)
        side31 = math.sqrt((x1-x3)**2+(y1-y3)**2)
        return side12 + side23 + side31

def main():
    circle1 = Circle(5, 2, 5)
    triangle = Triangle((0,0),(4,0),(0,3))
    print(triangle.getPerimeter())

if __name__ == "__main__":
    main()