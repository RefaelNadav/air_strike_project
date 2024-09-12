from target import Target
import math

def calc_distance(target:Target):
    r = 6371.0  # Radius of the Earth in kilometers
    if 'lat' not in target.location or 'lon' not in target.location:
        return "Target location must include 'lat' and 'lon'"

    # Convert degrees to radians
    lat1_rad = math.radians(target.location['lat'])
    lon1_rad = math.radians(target.location['lon'])
    lat2_rad = math.radians(31.7683) #lat in Jerusulem
    lon2_rad = math.radians(35.2137) #lon in Jerusulem
    # print(target.location['lat'], target.location['lon'])
    # Calculate differences between the coordinates
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    # Apply Haversine formula
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    # Calculate the distance
    distance = r * c
    return distance