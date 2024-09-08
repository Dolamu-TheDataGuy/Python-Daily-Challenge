"""
Use the geopy library to get the coordinates of particular places based on 
their addresses
"""
from geopy.geocoders import Nominatim

locations = [
    ('Norman Thomas HS (ECF)', '111 E 33rd St, NYC, New York'),
    ('Midtown East Campus', '233 E 56th St, NYC, New York'),
    ('Louis D. Brandeis HS', '145 W 84th St, NYC, New York'),
    ('Martin Luther King, Jr. Hs', '122 Amsterdam Avenue, NYC, New York'),
    ('P.S. 48', '4360 Broadway, NYC, New York')
]

address_cordinates: list[tuple[str, float, float]] = []

for location in locations:
    geolocator = Nominatim(user_agent = "address_geocoder")
    addr = geolocator.geocode(location[-1])
    address_cordinates.append((location[0], addr.latitude, addr.longitude))
    
print(address_cordinates)