#TODO:1.1
def multiply(m, n):
    """
    >>> multiply(5, 3)
    15
    """
    if n == 0 or m == 0:
        return 0
    if n > 0:
        return m + multiply(m, n-1)
    
#TODO:1.3
def hailstone(n):
    """
    Print out the hailstone sequence starting at n, 
    and return the number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """ 
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone(n // 2)
    else:
        return 1 + hailstone(3 * n + 1)
    
#TODO:1.4
def merge(n1, n2):
    """ Merge two numbers
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge(21, 31)
    3211
    """
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    else: 
        if n1 % 10 > n2 % 10:
            return merge(n1, n2 // 10) * 10 + n2 % 10
        else:
            return merge(n1 // 10, n2) * 10 + n1 % 10
        
#TODO:1.5
def make_func_repeater(f, x):
    """
    >>> incr_1 = make_func_repeater(lambda x: x + 1, 1)
    >>> incr_1(2)
    3
    >>> incr_1(5)
    6
    >>> make_func_repeater(lambda x: x + 1, 2)(6)
    8
    """
    def repeat(y):
        if x == 1:
            return f(y)
        else :
            return make_func_repeater(f, x - 1)(f(y))
    return repeat

#TODO:1.6
def is_prime(n):
    """
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """
    if n == 1:
        return False
    return prime_helper(n, n-1)
def prime_helper(n, m):
    if m == 1:
        return True
    elif n % m == 0:
        return False
    else:
        return prime_helper(n, m-1)