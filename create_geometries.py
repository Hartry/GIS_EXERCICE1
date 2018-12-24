# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 10:59:25 2018

@author: schweppes
"""
from shapely.geometry import Point, LineString, Polygon

X=[]

def createPointGeom(x_coord,y_coord):     
    return Point(x_coord,y_coord)

def addPointToList(Point):
    X.append(Point)

def createLineGeom(plistToString):
    return LineString(plistToString)

def createPolyGeom(plistToPoly):
    return Polygon(plistToPoly)

pointA=(2.2, 4.2)
pointB=(7.2, -25.1)
pointC=(7.2, 25.2)
addPointToList(pointA)
addPointToList(pointB)
addPointToList(pointC)
line3 = createLineGeom(X)
poly3 =createPolyGeom(X)
