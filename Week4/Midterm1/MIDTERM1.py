#TODO:solution of Problem1--Down for the Count
#TODO:1a
def count(element, box):
    """Count how many times digit element appears in integer box.
    >>> count(2, 222122)
    5
    >>> count(0, -2020)
    2
    >>> count(0, 0) # 0 has no digits
    0
    """
    assert element >= 0 and element < 10
    box = abs(box)
    "(a)"
    total = 0
    while box > 0:
        if box % 10 == element:
            "(b)"
            total = total + 1
            "(c)"
        box = box // 10
    return total

#TODO:1b
def count_nine(element, box):
    """Count how many times digit element appears in the non-negative integer
    box in a place that is not next to a 9.
    >>> count_nine(2, 222122)
    5
    >>> count_nine(1, 1911191) # Only the middle 1 is not next to a 9
    1
    >>> count_nine(9, 9)
    1
    >>> count_nine(9, 99)
    0
    >>> count_nine(3, 314159265359)
    2
    >>> count_nine(5, 314159265359)
    1
    >>> count_nine(9, 314159265359)
    2
    >>> count_nine(0, 0) # No digits are in 0
    0
    """
    assert element >= 0 and element < 10
    assert box >= 0
    nine, total = False, 0
    while box > 0:
        if box % 10 ==element and not (nine or box // 10 % 10 == 9):
            # (a)                                   (b)
            total = total + 1
                    #   (c)
        nine = box % 10 == 9
                #   (d)
        box = box // 10
    return total

#TODO:1c
def fit(pegs, holes):
    """Return whether every digit in pegs appears at least as many times in
    holes as it does in pegs.
    >>> fit(123, 321) # Each digit appears once in pegs and in holes.
    True
    >>> fit(1213, 33221) # 1 appears twice in pegs, but only once in holes.
    False
    >>> fit(12, 22) # 1 appears once in pegs, but not at all in holes.
    False
    >>> fit(314159, 112233456789)
    True
    """
    i = 0
    while i <= 9:
                #(a)
        if count(i, holes) < count(i, pegs):
            #(b)
            return False
            #(c)
        i = i + 1
    return True
            #(d)

#TODO:solution of problem2--Mystery Function
"Assume the following functions are also defined:"
def add_two(y):
    return y + 2
def two(y):
    return 2
def constant(k):
    def ignore(x):
        return k
    return ignore
def diff(f, g):
    return lambda z: abs(f(z) - g(z))
"""
    a: . . . two
    b: . . . constant(2)
    c: . . . constant(0)
    d: . . . lambda y: abs(mystery(y))
"""

#TODO:solution of problem3--Please Register to Vote
def vote(vote):
    please = lambda nov: vote(nov) + third
    third = ty + 3
    return please
ty = 1
register = vote(lambda nov: nov + ty)
ty = ty + 2
register(ty * 10) #30

#TODO:solution of problem4--Amazing Job Growth
#(a)
def growth(baseline):
    """Return a function that can be called repeatedly on numbers and prints
    the difference between its argument and the smallest argument used so far
    (including baseline).
    >>> job = growth(148)(149)(150)(130)(133)(139)(137)
    1
    2
    0
    3
    9
    7
    """
    def increase(observed):
        under = min(baseline, observed)
                #(a)
        print(observed - under)
        return growth(under)
                #(b)
    return increase

#(b)
def square(x):
    return x * x
def maxer(smoke):
    """Return a repeatable function fire(y) that prints the largest smoke(y) so far.
    >>> g = maxer(square)
    >>> h = g(2)(1)(3)(2)(-4) # print the largest square(y) so far
    4
    4
    9
    9
    16
    >>> h = maxer(abs)(2)(1)(3)(2)(-4) # print the largest abs(y) so far
    2
    2
    3
    3
    4
    """
    def fire(y):
        print(smoke(y))
        #(a)
        def haze(z):
            if smoke(z) < smoke(y):
                #(b)
                z = y
            return fire(z)
                #(c)
        return haze
    return fire
