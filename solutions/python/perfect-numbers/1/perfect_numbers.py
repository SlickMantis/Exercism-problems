def is_positive(number):
    return number > 0

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if is_positive(number) == True:
        factors = []
        for i in range(1,number + 1):
            if number % i == 0:
                factors.append(i)
        aliquot_sum = sum(f for f in factors if f != number)
        if aliquot_sum < number:
            return "deficient"
        if aliquot_sum == number:
            return "perfect"
        if aliquot_sum > number:
            return "abundant"
    else:
        raise ValueError("Classification is only possible for positive integers.")
