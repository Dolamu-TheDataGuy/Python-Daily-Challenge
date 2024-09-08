"""
Standard Library - Build a GIS library that calculates straight line distance between coordinates
assuming the earth is a sphere and spheriod (Ellipsoid)

Research about Haversine Distance -> https://www.educative.io/answers/how-to-calculate-distance-using-the-haversine-formula
"""

import math

def haversine_distance(origin: tuple[float, float], destination: tuple[float, float]) -> float:
    lat1, lon1 = origin
    lat2, lon2 = destination
    
    phi_lat1 = math.radians(lat1)
    phi_lat2 = math.radians(lat2)
    
    radius = 6371000
    dlat = math.radians(lat2-lat1)
    dlon  = math.radians(lon2-lon1)
    
    a = (math.sin(dlat/2))**2 + math.cos(phi_lat1) * math.cos(phi_lat2) * ((math.sin(dlon/2)))**2
    
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    
    distance = radius * c
    return distance

if __name__ == "__main__":
    san_francisco = (37.7749, -122.4194)
    new_york = (40.661, -73.944)
    
    distance = haversine_distance(san_francisco, new_york)
    print(distance/1000, "km")