from geopy import distance

san_francisco = (37.7749, -122.4194)
new_york = (40.661, -73.944)

straight_line_distance = distance.great_circle(san_francisco, new_york)
print(straight_line_distance)

ellipsoid_distance = distance.geodesic(san_francisco, new_york, ellipsoid='WGS-84')
print(ellipsoid_distance)

