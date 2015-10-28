
# linked list

empty = 'empty'
def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair."""
    return s == empty or (len(s) == 2 and is_link(s[1]))

def link(first, rest):
    """
    Construct a linked list from its first element and the rest.

    """

    assert is_link(rest), "rest must be a linked list."
    return [first, rest]

def first(s):
    """Return the first element of a linked list s."""
    assert is_link(s), "first only applies to linked lists."
    assert s != empty, "empty linked list has no first element."
    return s[0]

def rest(s):
    """Return the rest of the elements of a linked list s."""
    assert is_link(s), "rest only applies to linked lists."
    assert s != empty, "empty linked list has no rest."
    return s[1]
    
    
# link是作为一个constructor的角色. 
# first 和rest则是作为selector的角色.

# 测试
>>> four = link(1, link(2, link(3, link(4, empty))))
>>> first(four)
1
>>> rest(four)
[2, [3, [4, 'empty']]]

# length和element selection和sequence abstration中很重要的东西
def len_link(s):
    """Return the length of linked list s."""
    length = 0
    while s != empty:
        s, length = rest(s), length + 1
    return length


def getitem_link(s, i):
    """Return the element at index i of linked list s."""
    while i > 0:
        s, i = rest(s), i - 1
    return first(s)
"""
s = rest(s)是说,把s的后半部分取出来, 放入循环就是说, 把s的后半部分的后半部分的后半部分取出来, 从外到内.一直取到第i层. 这时i就归零了. 然后return i层的第一个元素.

"""
# 测试
>>> len_link(four)
4
>>> getitem_link(four, 1)
2

# 递归式
def len_link_recursive(s):
    """Return the length of a linked list s."""
    if s == empty:
        return 0
    return 1 + len_link_recursive(rest(s))

def getitem_link_recursive(s, i):
    """Return the element at index i of linked list s."""
    if i == 0:
        return first(s)
    return getitem_link_recursive(rest(s), i - 1)

# 例如, 
# [1, [2, [3, empty]]] 作为linked list的第2个,也就是
# [2, [3, empty]] 作为linked list的第1个,也就是
# [3, empty] 作为linked list的第0个,也就是 3

>>> def extend_link(s, t):
        """
        Return a list with the elements of s followed by those of t.
        extend的意思是把t弄到s的后面, 也就是里面.
    
        """
        
        assert is_link(s) and is_link(t)
        if s == empty:
            return t
        else:
            return link(first(s), extend_link(rest(s), t))
        # 很像是cons()的那种写法
        # 如果看成列表的话, t是包裹在s的最里面的.

>>> extend_link(four, four)
[1, [2, [3, [4, [1, [2, [3, [4, 'empty']]]]]]]]
   s            ------ t ------------------

>>> def apply_to_all_link(f, s):
        """Apply f to each element of s."""
        assert is_link(s)
        if s == empty:
            return s
        else:
            return link(f(first(s)), apply_to_all_link(f, rest(s)))
        # 每次就把first(s)取出来应用函数f,然后剩下的根据same nature递归即可.

>>> apply_to_all_link(lambda x: x*x, four)
[1, [4, [9, [16, 'empty']]]]

>>> def keep_if_link(f, s):
        """Return a list with elements of s for which f(e) is true."""
        assert is_link(s)
        if s == empty:
            return s
        else:
            kept = keep_if_link(f, rest(s))
            if f(first(s)):
                return link(first(s), kept)
            else:
                return kept

>>> keep_if_link(lambda x: x%2 == 0, four)
[2, [4, 'empty']]

>>> def join_link(s, separator):
        """Return a string of all elements in s separated by separator."""
        if s == empty:
            return ""
        elif rest(s) == empty:
            return str(first(s))
        else:
            return str(first(s)) + separator + join_link(rest(s), separator)
        # so much like the TLS programming style.

>>> join_link(four, ", ")
'1, 2, 3, 4'
