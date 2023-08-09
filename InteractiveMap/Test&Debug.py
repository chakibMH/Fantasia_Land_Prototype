api_key = 'Our_API_KEY'
origin = 'Hydra'
destination = 'Makam Chahid'

directions = get_directions(api_key, origin, destination)

if directions:
    print("Directions:")
    for idx, step in enumerate(directions, start=1):
        print(f"{idx}. {step}")
else:
    print("Failed to retrieve directions.")
