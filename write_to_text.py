from data import *

def writePlaceNames():
    # Create or overwrite the file placeNames.txt
    with open("placeNames.txt", "w") as file:
        # Join the keys with commas and write to the file
        file.write(",".join(campusMappings.keys()))
    print("placeNames.txt has been created with the campus names.")
    return

def writePlaceCodes():
    # Create a list to hold the formatted strings
    formatted_strings = []

    # Iterate through the dictionary and create the desired format
    for key, value in campusReversedMappings.items():
        # Calculate the number of 'x' characters needed
        num_xs = len(value)
        # Create the formatted string
        formatted_string = f"{key}{'x' * (num_xs - len(key))}"  # Ensure it matches the length of the value
        formatted_strings.append(formatted_string)

    # Join the formatted strings with commas and write them them
    with open("placeKeys.txt", "w") as file:
        file.write(",".join(formatted_strings))
    return

writePlaceNames()
writePlaceCodes()