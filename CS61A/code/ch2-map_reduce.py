def reduce(reduce_fn, s, initial):
    """
     >>> reduce(mul, [2, 4, 8], 1)
     64
    """
    reduced = initial
    for x in s:
        reduced = reduce_fn(reduced, x)
    return reduced

def divisors_of(n):
    """
    >>> divisors_of(12)
    [1, 2, 3, 4, 6]
    """
    divides_n = lambda x: n % x == 0
    return [1] + keep_if(divides_n, range(2, n))

from operator import add
def sum_of_divisors(n):
    return reduce(add, divisors_of(n), 0)


def perfect(n):
    return sum_of_divisors(n) == n


# keep_if(perfect, range(1, 1000))
# [1, 6, 28, 496]

# map & reduce
# applying the list constructor to the result of built-in map and filter calls.
apply_to_all = lambda map_fn, s: list(map(map_fn, s))
keep_if = lambda filter_fn, s: list(filter(filter_fn, s))

# reduce的使用
from functools import reduce
from operator import mul
def product(s):
    """
    >>> product([1, 2, 3, 4, 5])
    120
    """
    return reduce(mul, s)

