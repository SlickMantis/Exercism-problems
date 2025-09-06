def label(colors):
    # Mapping of colors to digit values
    color_values = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }

    # Extract values for first two and multiplier
    first_digit = color_values[colors[0]]
    second_digit = color_values[colors[1]]
    multiplier = color_values[colors[2]]

    # Build base number and apply multiplier
    value = int(f"{first_digit}{second_digit}") * (10 ** multiplier)

    # Format with units
    if value >= 1_000_000_000:
        return f"{value // 1_000_000_000} gigaohms"
    elif value >= 1_000_000:
        return f"{value // 1_000_000} megaohms"
    elif value >= 1_000:
        return f"{value // 1_000} kiloohms"
    else:
        return f"{value} ohms"


