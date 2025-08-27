import math

def score(x, y):
    distance = math.sqrt(x**2 + y**2)
    
    if distance <= 1:
        return 10   # inner circle
    elif distance <= 5:
        return 5    # middle circle
    elif distance <= 10:
        return 1    # outer circle
    else:
        return 0    # outside target
