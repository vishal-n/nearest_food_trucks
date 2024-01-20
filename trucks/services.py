import csv
from math import sin, cos, sqrt, atan2, radians

def find_distance_between_locations(loc1, loc2):
    R = 6373.0
    
    lat1 = radians(float(loc1[0]))
    lat2 = radians(float(loc2[0]))
    long1 = radians(float(loc1[1]))
    long2 = radians(float(loc2[1]))

    dlon = long2 - long1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance


with open('food-truck-data.csv', mode ='r') as file:
    csv_file = csv.reader(file)
    total_count = 0
    lat_longs = []
    for row in csv_file:
        total_count += 1
        # print((row[14], row[15]))
        lat_longs.append((row[14], row[15]))
    
    lat_longs = lat_longs[1:]