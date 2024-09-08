import requests
import json
from key import API_KEY

url = "https://www.spatialthoughts.com"

response = requests.get(url)

print(response.status_code)


san_francisco = (37.7749, -122.4194)
new_york = (40.661, -73.944)

def get_driving_distance(source: tuple[float, float], destination: tuple[float, float]):
    parameters = {
        'api_key': API_KEY,
        'start': f"{source[1]}, {source[0]}",
        'end': f"{destination[1]}, {destination[0]}"
    }

    url = "https://api.openrouteservice.org/v2/directions/driving-car"
    resp = requests.get(url, params=parameters)

    if resp.status_code == 200:
        print("Request successful.")
        data = resp.json()
    else:
        print("Request failed!")
        
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)
        
    summary = data["features"][0]["properties"]["segments"]
    distance = summary[0]["distance"]
    return distance

if __name__ == "__main__":
    print(get_driving_distance(san_francisco, new_york), "km")