def value(colors):
    color_codes = {"black": 0,
                   "brown": 1,
                   "red": 2,
                   "orange": 3,
                   "yellow": 4,
                   "green": 5,
                   "blue": 6,
                   "violet": 7,
                   "grey": 8,
                   "white": 9}

    value_codes = []
    for i in colors:
        value_codes.append(color_codes[i])

    for i in value_codes:
        value = str(value_codes[0]) + str(value_codes[1])

    return int(value)
        
