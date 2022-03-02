"""EX06- Dictionaries."""

___author___ = "730474696"


def invert(normal: dict[str, str]) -> dict[str, str]:
    """This function will take a dictionary and invert the keys and values."""
    # Creates a new dictionary and list. 
    inverted_dict: dict[str, str] = dict()
    keys_list: list[str] = list()   
    for key in normal:
        # inverts the dictionary by assigning keys in inverted_dict the value in normal. 
        inverted_dict[(normal[key])] = key
        if normal[key] in keys_list:
            # if the value (in normal) appears in the list mpre than once, a key error is raised. 
            raise KeyError("Duplicate key has been found")
        else:
            keys_list.append(normal[key])    
    return inverted_dict


def favorite_color(colors: dict[str, str]) -> str:
    """Goes through a dictionary of names and colors finds the color that appears most often."""
    popular_color: str = ""
    color_values: dict[str, int] = dict()
    i: int = 0
    for key in colors:
        # creates a new dictionary where the color: number of times the color appears is the new dictionary. 
        if colors[key] not in color_values:
            color_values[colors[key]] = 1
        elif colors[key] in color_values:
            color_values[colors[key]] += 1
        for key in color_values:
            # if i is greater than the value of key (color) than popular_color is assigned that key
            if color_values[key] > i:
                i = color_values[key]
                popular_color = key
    return popular_color


def count(given_values: list[str]) -> dict[str, int]:
    """Counts the number of times a value appears and assigns that in the dictionary as value: frequency of value."""
    frequencies: dict[str, int] = dict()
    for value in given_values:
        if value in frequencies:
            # if the value is already in frequencies as a key, then the value is increased by one. 
            frequencies[value] += 1
        elif value not in frequencies:
            # Tests to see if the value is in the frequncies dictionary, 
            # and if it's not then the list value is added to the dictionary as a key and assigned a value of one.
            frequencies[value] = 1
    return frequencies
