# 主题：myrange：引入lazy computation的概念；

# 接下来介绍python的iterator的接口：__next__()
# 再介绍什么是iterable： 是含有__iter__()方法的对象。
# 最后介绍generator：用更简洁的方式来写iterator.

# 展现implicit seq的威力：按需计算，以下实现一个py range函数的简化版本：

class myrange:
    """
    创建左闭右开的myrange对象，其行为参考py内置的range对象。这是一个lazy computation的例子。

    myrange(1,3) 的长度是2
    这是几种特殊的情况:
    myrange(-2,2) 的长度是4
    myrange(2,-2) 的长度是0


    """
    def __init__(self, start, end=None):
        # 当用户输入的区间只有一个数时我们把区间设置为(0,这个数)
        if end is None:
            start, end = 0, start
        # 然后继续..
        self.start = start
        self.end = end

    def __len__(self):
        # 长度不能是负数，如果区间左边大于右边，那么长度就是负数
        # 这里就可以把长度修正为0
        return max(0, self.end - self.start)        

    def __getitem__(self, k):
        # 这里要下标为负数的情况，如果是-1，我们认为是取range的最后一个，如果k是
        # -2 那么是取倒数第二个..
        if k < 0:
            k = len(self) + k
        if k < 0 or k >= len(self):
            raise IndexError
        return self.start + k;

    def __repr__(self):
        return 'Range({0}, {1})'.format(self.start, self.end)

# ######################################
# __next__()方法与python 中的iterators
# ######################################

class LetterIter:
    """
    一个Iterator，不断遍历ASCII字母表中的字母
    区间是左闭右开：即不包含end所代表的字母.

    >>> a_to_c = LetterIter('a', 'c')
    >>> next(a_to_c)
    'a'
    >>> next(a_to_c)
    'b'
    >>> next(a_to_c)
    Traceback (most recent call last):
        ...
    StopIteration
    """
    def __init__(self, start='a', end='e'):
        self.next_letter = start
        self.end = end

    def __next__(self):
       if self.next_letter == self.end:
           raise StopIteration
       letter = self.next_letter
       self.next_letter = chr(ord(letter)+1)
       # ord()返回一个字符串对应的数字；chr()则反过来。
       return letter

# 一个正整数的class, 每次初始化将产生一个iterator.
class positives:
    def __init__(self):
        self.next_positive = 1

    def __next__(self):
        result = self.next_positive
        self.next_positive += 1
        return result


        
# ######################################
# iterable objects
# ######################################


class Letters:
    # 通过这个class创建的对象是可迭代的(iterable)，因为可以调用__iter__()来返回一个iterator.

    """
    参考：first_iterator和second_iterator都是调用Letters.__iter__()得到的.

    >>> b_to_k = Letters('b', 'k')
    >>> first_iterator = b_to_k.__iter__()
    >>> next(first_iterator)
    'b'
    >>> next(first_iterator)
    'c'
    >>> second_iterator = iter(b_to_k)
    >>> second_iterator.__next__()
    'b'
    >>> first_iterator.__next__()
    'd'
    >>> first_iterator.__next__()
    'e'
    >>> second_iterator.__next__()
    'c'
    >>> second_iterator.__next__()
    'd'
    """
    def __init__(self, start='a', end='e'):
        self.start = start
        self.end = end
    def __iter__(self):
        return LetterIter(self.start, self.end)
    # 这样我们可以创建Letter的实例，然后每次调用instance.__iter__()方法级就能得到一个
    # iterator，多次调用就得到多个iterator.

# ######################################
# 使用Generator
# ######################################

# 使用geneator写一个改良版本的Letter函数，比上面那个更简洁。
def letters_generator():
    current = 'a'
    while current <= 'd':
        yield current
        current = chr(ord(current)+1)

for letter in letters_generator():
    print(letter)