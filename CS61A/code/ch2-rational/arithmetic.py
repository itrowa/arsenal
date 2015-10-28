from cons2 import *

# +++++++++++++++++++++++++++++++++++++++++++++++++++++
# abstraction barrier
# +++++++++++++++++++++++++++++++++++++++++++++++++++++

# ##############
#
# 以下基于抽象屏障另外一层的constructor和selector实现有理数的运算。 
# 当我们调用这写函数的时候， 所有的参数和返回值都是当成**完整的一个有理数**来看的



def add_rational(x, y):
    """Add rational numbers x and y."""
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)

def mul_rational(x, y):
    """Multiply rational numbers x and y."""
    return rational(numer(x) * numer(y), denom(x) * denom(y))

def rationals_are_equal(x, y):
    """Return whether rational numbers x and y are equal."""
    return numer(x) * denom(y) == numer(y) * denom(x)

def print_rational(x):
    """Print rational x."""
    print(numer(x), "/", denom(x))