# solution of Question_1.1
def count_stair_ways(n):
    """
    You want to go up a flight of stairs that has n steps. You can either take 1
    or 2 steps each time. How many different ways can you go up this flight of
    stairs?

    >>> count_stair_ways(20)
    10946
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return count_stair_ways(n - 1)+count_stair_ways(n - 2)
    
# solution of problem_1.2
def count_k(n ,k):
    """
    >>> count_k(3, 3)
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1)
    1
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif k == 1:
        return 1
    else:
        count, i= 0, 1
        while i <= k:
            count += count_k(n - i, k)
            i = i + 1
    return count

# solution of problem_2.2
def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [s[i] * i for i in range(len(s)) if i % 2 == 0]

# solution of problem_2.3
def max_product(s):
    """"Return the maximum product that can be formed using non-consecutive
    elements of s.
    
    >>> max_product([10, 3, 1, 9, 2])
    90
    >>> max_product([5, 10, 5, 10, 5])
    125
    >>> max_product([])
    1
    """
    if len(s) == 0:
        return 1
    else:
        return max(s[0] * max_product(s[2:]), max_product(s[1:]))

