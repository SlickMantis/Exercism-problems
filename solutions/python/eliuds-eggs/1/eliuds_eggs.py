def egg_count(display_value):
    binary_values = []
    while display_value > 0:
        binary_values.append(display_value % 2)
        display_value //= 2

    empty_spots = []
    for i in binary_values:
        if i == 1:
            empty_spots.append(i)
    return len(empty_spots)
