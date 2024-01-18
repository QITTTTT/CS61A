"""
    disc01
"""
def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    return temp < 60 or raining

def square(x):
    """
    test
    """
    print("here!")
    return x * x

def so_slow(num):
    """
    test
    """
    x = num
    while x > 0:
        x = x + 1
    return x / 0

def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    count = 0
    for i in range(n)[2:]:
        if n % i == 0:
            count = count + 1
    return count == 0
