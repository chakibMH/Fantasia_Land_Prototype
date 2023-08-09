import googlemaps

import math

def get_coordsPOI(POI, maps_api_key = "gmapsAPIKeys"):
    
    """this function will return the radians coordinates of a point of intrest (POI).
    We'll use those coordinates to show them on our interactive map.
    """

    # client object
    client = googlemaps.Client(key = maps_api_key)
    
    res = client.geocode("POI")[0]
    
    rad_coords = res['geometry']['location']
    
    return rad_coords


def get_directions(api_key, origin, destination):
    """this function will return the directions from an origin point (the position of the user) to a destination.
    We'll use show the direction on our interactive map.
    """
  
    gmaps = googlemaps.Client(key=api_key)
    
    try:
        directions_result = gmaps.directions(origin, destination, mode="driving")
        
        if directions_result:
            route = directions_result[0]
            steps = route['legs'][0]['steps']
            directions = [step['html_instructions'] for step in steps]
            return directions
        else:
            print("No directions found.")
    except Exception as e:
        print("Error:", e)
    
    return None



