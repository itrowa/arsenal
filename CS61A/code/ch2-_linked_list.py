################
# Linked lists #
################
    
# link是作为一个constructor的角色. 
# first 和rest则是作为selector的角色.

# 顺带一提, 这几个函数和scheme中的几个函数功能是一样的, 它们分别是:

# link()      cons
# first()     car
# rest()      cdr

# @todo@ : 把变量名按照scheme的风格进行修改. 或许可以留到写scheme解释器的时候干这件事情

# 定义一个链表结束标记符
empty = 'empty'

def link(first, rest):
    """
    根据输入的两个参数构建一个链表
    first: 第一个元素
    rest: 剩余的元素
    """
    assert is_link(rest), "arg2 must be a linked list"
    return [first, rest]

def first(s):
    """
    返回链表s的第一部分。

    例如;
    >>> first([1, [2, [3, empty]])
    [2, [3, empty]] 
    """
    assert is_link(s), "must apply linked list"
    assert s != empty, "Empty list has no first element"
    return s[0]

def rest(s):
    """
    返回链表s的后面部分。返回值还是一个表.
    """
    assert is_link(s), "must apply linked list"
    assert s != empty, "Empty list has no last element"
    return s[1]

def is_link(s):
    # 要么s是空, 要么s是list,且s的长度为2,且s的[1]也是我们定义的link
    return s == empty or (type(s) == list and len(s) == 2 and is_link(s[1]))

def print_link(s):
    """
    print一种错觉
    虽然链表是层次性结构, 但是我还是要把它打印成扁平式结构. 
    """
    if rest(s) == empty:
        return None
    return str(first(s)) + ' ' + str(print_link(rest(s)))

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# abstraction barrier
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 测试
four = link(1, link(2, link(3, link(4, empty))))
first(four)
# 1
rest(four)
# [2, [3, [4, 'empty']]]

# 实现length 和 element selection
# length和element selection和sequence abstration中很重要的东西
def len_link(s):
    """
    Return the length of linked list s.
    迭代式计算.

    >>> len_link(four)
    4 
    """
    length = 0
    # 用迭代方法计算s的长度
    while s != empty:
        s, length = rest(s), length + 1
    return length


def getitem_link(s, i):
    """
    Return the element at index i of linked list s.
    迭代式计算.

    >>> getitem_link(four, 1)
    2
    """
    # 用迭代方法取出链表s中的第i个元素
    while i > 0:
        s, i = rest(s), i - 1
    return first(s)

def len_link_recursive(s):
    """
    Return the length of a linked list s.
    递归式计算.

    """
    if s == empty:
        return 0
    return 1 + len_link_recursive(rest(s))

def getitem_link_recursive(s, i):
    """
    Return the element at index i of linked list s.
    递归式计算.
    """
    if i == 0:
        return first(s)
    return getitem_link_recursive(rest(s), i - 1)
    # 解释:例如, 
    # [1, [2, [3, empty]]] 作为linked list的第2个,也就是
    # [2, [3, empty]] 作为linked list的第1个,也就是
    # [3, empty] 作为linked list的第0个,也就是 3

def extend_link(s, t):
    """
    Return a list with the elements of s followed by those of t.
    extend的意思是把t弄到s的后面, 也就是里面.
     >>> extend_link(four, four)
    [1, [2, [3, [4, [1, [2, [3, [4, 'empty']]]]]]]]
    #    s            ------ t ------------------   
    """
    assert is_link(s) and is_link(t)
    if s == empty:
        return t
    else:
        return link(first(s), extend_link(rest(s), t))
    # 很像是cons()的那种写法
    # 如果看成列表的话, t是包裹在s的最里面的.

def apply_to_all_link(f, s):
    """Apply f to each element of s.
    相当于map函数。
    """
    assert is_link(s)
    if s == empty:
        return s
    else:
        return link(f(first(s)), apply_to_all_link(f, rest(s)))
    # 每次就把first(s)取出来应用函数f,然后剩下的根据same nature递归即可.

def reverse(s):
    """ 反转一个链表.
    """
    return reverse_to(s, empty)

def reverse_to(s, result):
    """ 取出链表s的第一个元素并附加于result的前面, 不断递归执行这个过程..
    例如, s是 1, 2, 3
    result 是 []

    ->
    2, 3;      1

    ->
    3;        2, 1

    ->
    [];      3, 2, 1
    """
    if s == empty:
        return []
    else:
        return reverse_to(rest(s) , link(first(s), result))


# >>> apply_to_all_link(lambda x: x*x, four)
# [1, [4, [9, [16, 'empty']]]]

def keep_if_link(f, s):
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

# >>> keep_if_link(lambda x: x%2 == 0, four)
# [2, [4, 'empty']]

def join_link(s, separator):
    """Return a string of all elements in s separated by separator."""
    if s == empty:
        return ""
    elif rest(s) == empty:
        return str(first(s))
    else:
        return str(first(s)) + separator + join_link(rest(s), separator)
    # so much like the TLS programming style.

# >>> join_link(four, ", ")
# '1, 2, 3, 4'
