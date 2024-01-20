import csv
from math import sin, cos, sqrt, atan2, radians

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


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

# Create your views here.
class NearestTrucksView(APIView):
    def get(self, request):
        pos1 = str(request).find('lat')
        pos2 = str(request).find('&')
        lat = str(request)[pos1+4:pos2]
        long = str(request)[pos2+6:-2]
        current_location = (lat, long)
        result = []
        nearest_trucks_count = 0
        print("Lat: ", lat)
        print("Long: ", long)

        with open('food-truck-data.csv', mode ='r') as file:
            rows = []
            csv_file = csv.reader(file)
            lat_longs = []
            for row in csv_file:
                rows.append(row)
                lat_longs.append((row[14], row[15]))
        
        rows = rows[1:]
        lat_longs = lat_longs[1:]

        for i in range(len(lat_longs)):
            current_distance = find_distance_between_locations(lat_longs[i], current_location)
            if current_distance <= 5:
                nearest_trucks_count += 1
                result.append(rows[i])

        return Response({"Nearest Trucks": result, "Count": nearest_trucks_count})
