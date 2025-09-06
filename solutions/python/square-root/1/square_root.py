def square_root(number):
    # Checks is given number is whole and positive
    if number % 1 == 0 and number > -1:
        # Checks for factors of number and appends them to factors list
        factors = []
        for i in range(1, number + 1):
            if number % i == 0:
                factors.append(i)
        # If a factor in the factors list times itself equals given number, return the factor
        for i in factors:
            if i * i == number:
                return i
