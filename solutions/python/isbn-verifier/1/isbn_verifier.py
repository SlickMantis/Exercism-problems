def is_valid(isbn):
    # remove hyphens
    isbn = isbn.replace("-", "")

    # must be 10 characters long
    if len(isbn) != 10:
        return False

    # X is only allowed in last position
    if "X" in isbn[:-1]:
        return False

    # convert to numbers
    digits = []
    for i, char in enumerate(isbn):
        if char.isdigit():
            digits.append(int(char))
        elif char == "X" and i == 9:  # only valid if last char
            digits.append(10)
        else:
            return False  # invalid character

    # compute checksum
    total = sum((10 - i) * num for i, num in enumerate(digits))
    return total % 11 == 0
