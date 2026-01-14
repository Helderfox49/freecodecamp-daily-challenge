import math
def get_number_of_plants(field_size, unit, crop):

    # Conversion to squares meters
    if unit == "acres":
        sq_meters  = field_size * 4046.86
    elif unit == "hectares":
        sq_meters = field_size * 10000 
    
    space_per_plant = {
        "corn": 1,
        "wheat" : 0.1,
        "soybeans" : 0.5,
        "tomatoes" : 0.25,
        "lettuce" : 0.2
    }

    return int(sq_meters / space_per_plant[crop])


if __name__ == "__main__":
    print(get_number_of_plants(1, "acres", "corn")) # should return 4046.
    print(get_number_of_plants(2, "hectares", "lettuce")) # should return 100000.
    print(get_number_of_plants(20, "acres", "soybeans")) # should return 161874.
    print(get_number_of_plants(3.75, "hectares", "tomatoes")) # should return 150000.
    print(get_number_of_plants(16.75, "acres", "tomatoes")) # should return 271139.