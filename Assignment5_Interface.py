#!/usr/bin/python2.7
#
# Assignment5 Interface
# Name: Satrajit Maitra
#

from pymongo import MongoClient
import os
import sys
import json
from math import sin, cos, sqrt, atan2, radians

def GetDistance(myLocation, latitude, longitude):
    R = 3959
    latitude1 = radians(latitude)
    longitude1 = radians(longitude)
    latitude2 = radians(float(myLocation[0]))
    longitude2 = radians(float(myLocation[1]))

    deltaLat = latitude2 - latitude1
    deltaLon = longitude2 - longitude1

    a = sin(deltaLat / 2)**2 + cos(latitude1) * cos(latitude2) * sin(deltaLon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c


def FindBusinessBasedOnCity(cityToSearch, saveLocation1, collection):
    file = open(saveLocation1, 'w')
    result = collection.find({'city' : cityToSearch.capitalize()})

    for data in result:
        file.write(data['name'].upper() + '$' + data['full_address'].upper() + '$' + data['city'].upper() + '$' + data['state'].upper() + '\n')

    file.close()


def FindBusinessBasedOnLocation(categoriesToSearch, myLocation, maxDistance, saveLocation2, collection):
    file = open(saveLocation2, 'w')
    result = collection.find()

    for data in result:
        count = 0
        for category in categoriesToSearch:
            if category in data['categories']:
                count += 1
        if count == len(categoriesToSearch):
            distance = GetDistance(myLocation, data['latitude'], data['longitude'])
            if distance <= maxDistance:
                file.write(data['name'].upper() + '\n')

    file.close()
