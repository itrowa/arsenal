# how to hidde information from internal

class FibIter:
    """
    一个遍历Fib树的程序。注意内部attr name是戴了一个下划线的，这是python社区的约定，
    如果一个变量名以下划线开头说明它不希望被直接被外部引用（这个变量可能会改名，重写等..）

    """
    def __init__(self):
        self._next = 0
        self._addend = 1

    def __next__(self):
        result = self._next
        self._addend, self_next = self._next, self_addedn + self._next
        return result

def fib_generator():
    """ 生成fib数列

    >>> fibs = fib_generator()
    >>> [next(fibs) for _ in range(10)]
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]    
    """
    yield 0
    previous, current = 0, 1
    while True:
        yield current
        previous, current = current, previous + current

class empty_iterator:
    """iterator for no values.
    """
    def __next__(self):
        raise StopIteration
empty_iterator = empty_iterator()

# ######################
# Stream
# ######################

# 以下介绍stream

# ######################
# Link List
# ######################

# just for review!

# ######################
# Streams
# ######################

# another implicit data sequence.


class Stream:
    """
    lazily computed recursive list.
    """
    class empty:
        def __repr__(self):
            return 'Stream.empty'
    empty = empty()
    # 当调用一个Stream的实例例如s.empty时其实就是调用了一个empty类。

    def __init__(self, first, compute_rest=lambda: Stream.empty):
        assert callable(compute_rest), 'compute_rest must be callable.'
        self.first = first
        self._compute_rest = compute_rest

    @property
    def rest(self):
        """
        return the rest of the stream based on lazy computation.
        """
        if self._compute_rest is not None:
            self._rest = self._compute_rest()
            self._compute_rest = None
        return self._rest

def first_k(s, k):
    """return up to k elements of stream s as a list.

    >>> s = Stream(1, lambda: Stream(4, lambda: Stream(9)))
    >>> first_k(s, 2)
    [1, 4]
    >>> first_k(s, 5)
    [1, 4, 9]
    """
    elements = []    
    while s is not Stream.empty and k > 0:
        elements.append(s.first)
        s, k = s.rest, k-1
    return elements

def integer_stream(first=1):
    def compute_rest():
        return integer_stream(first+1)
    return Stream(first, compute_rest)

def square_stream(s):
    """
    take a stream and return a stream with doubled elements.
    """
    squared = s.first * s.first
    return Stream(squared, lambda: square_stream(s.rest))


def add_streams(s1, s2):
    """ add 2 streams together.
    """
    first = s.first + t.first
    def compute_rest():
        return add_streams(s1.rest, s2.rest)
    return Stream(first, compute_rest)

def primes(s):
    def not_divisible(k):
        return k % s.first != 0
    def compute_rest():
        return primes(filter_stream(not_divisible, s))
    return Stream(s.first, compute_rest)

# 测试
s = integer_stream(1)
ss = square_stream(s)

# 各种行为
s.first
s.rest.first
first_k(s,10)
first_k(ss,10)

# 更复杂的行为
first_k(add_streams(s, s.rest), 10)

ones = Stream(1, lambda:ones)
first_k(ones,10)

ints = Stream(1, lambda: add_streams(ints, ones))
first_k((ints, 10))



## map

def map_stream(fn, s):
    """Map a func fn over the elements of a stream s.
    """
    if s is Stream.empty:
        return s
    def compute_rest():
        return map_stream

def filter_stream(fn, s):
    """ filter a stream with predicate func fn.
    """
    if s is Stream.empty:
        return s
    def compute_rest():
        return filter_stream(fn, s.rest)
    if fn(s.first): # 如果s.first存在：
        return Stream(s.first, compute_rest)
    else:
        return compute_rest()