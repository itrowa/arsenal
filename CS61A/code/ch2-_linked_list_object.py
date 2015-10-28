# 用py的OOP系统写一个链表

class Link:
    """A linked list.

    >>> s = Link(3, Link(4, Link(5)))
    >>> len(s)
    3
    >>> s[2]
    5
    >>> s
    Link(3, Link(4, Link(5)))
    """
    empty = () # 这是一个class attr, 我们设置一个empty tuple作为约定的链表结束标记

    def __init__(self, first, rest = empty):
        # rest必须是我们约定的结束标记, 否则rest也必须是Link类的实例
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __getitem__(self, i):
    # 特殊方法, 以后就能用 obj[index]这样的语法来取得item了
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]
    # 其实应该是 return __getitem__(self, i - 1)

    def __len__(self):
        # 特殊方法: 这个使得Links类有len(obj)函数.
        return 1 + len(self.rest)

    def __repr__(self):
        # 它实现Link类的repr()函数
        if self.rest:
        # 如果rest部分存在, 递归处理它的后面部分
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(self.first, rest_str)

s = Link(3, Link(4, Link(5)))
square = lambda x: x * x
odd = lambda x: x % 2 == 1

def extend_link(s, t):
    """Return a Link with the elements of s followed by those of t.

    >>> extend_link(s, s)
    Link(3, Link(4, Link(5, Link(3, Link(4, Link(5))))))
    >>> Link.__add__ = extend_link
    >>> s + s
    Link(3, Link(4, Link(5, Link(3, Link(4, Link(5))))))
    """
    # 用递归法. 大概思路是一层一层剥开s的rest部分, 直到链表的末尾. 然后把t插入到这里就行了
    if s is Link.empty:
    	return t
    else:
    	return Link(s.first, extend_link(s.rest, t))

def map_link(f, s):
    """Apply f to each element of s.
    相当于python内置的map函数.

    >>> map_link(square, s)
    Link(9, Link(16, Link(25)))
    """	
    if s is Link.empty:
    	return s
    else:
    	return Link(f(s.first),  map_link(f, s.rest))

def filter_link(f, s):
    """Return a Link with elements of s for which f returns a true value.

    >>> map_link(square, filter_link(odd, s))
    Link(9, Link(25))
    """	
    if s is Link.empty:
        return s
    else:
        # 先用递归过滤找出满足f为真的s的rest部分.
        filterd = filter_link(f, s.rest)
        # 然后再检测s.first是否也满足f, 如果满足, 就加上s.first, 如果不满足就只返回filtered.
        if f(s.first) : 
        # 如果s.first存在
            return Link(s.first, filtered)
        else:
            return filtered

def join_link(s, separator):
    """Return a string of all elements in s separated by separator.

    >>> join_link(s, ", ")
    '3, 4, 5'
    """
    if s is Link.empty:
        return ""
    elif s.rest is Link.empty:
        return str(s.first)
    else:
        return str(s.first) + seperator + join_link(s.rest, seperator)


def partitions(n, m):
    """返回一个Linked list, 它表示用最大为m的部分来分m的结果.
    每个分法表示为一个linked list.
    """
    if n == 0:
        return Link(Link.empty)
    elif n < 0 or m == 0:
        return Link.empty
    else:
        using_m = partitions(n-m, m)
        with_m = map_link(lambda s: Link(m, s), using_m)
        without_m = partitions(n, m - 1)
        return extend_link(with_m, without_m)

def print_partitions(n, m):
    """Print the partitions of n using parts up to size m.

    >>> print_partitions(6, 4)
    4 + 2
    4 + 1 + 1
    3 + 3
    3 + 2 + 1
    3 + 1 + 1 + 1
    2 + 2 + 2
    2 + 2 + 1 + 1
    2 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 1 + 1
    """
    links = partitions(n, m)
    lines = map_link(lambda s: join_link(s, " + "), links)
    map_link(print, lines)

def has_cycle(s):
    """Return whether Link s contains a cycle(a list may contain itself as a sublist.)

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    """
    "*** YOUR CODE HERE ***"
    lists = set()
    while s != Link.empty:
        if s in lists:
            return True
        list.add(s)
        s = s.rest
    return False

