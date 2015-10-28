# implementation list and dict.

#list
def mutable_link():
    """Return a functional implementation of a mutable linked list."""
    contents = empty
    def dispatch(message, value=None):
        # 注意参数: 第一个是message, 第二个是作用于message的"参数"
        nonlocal contents
        if message == 'len':
            # 返回长度信息
            return len_link(contents)
        elif message == 'getitem':
            # 取出item并返回之
            return getitem_link(contents, value)
        elif message == 'push_first':
            # 追加到列表第一个
            contents = link(value, contents)
        elif message == 'pop_first':
            # 从列表第一个拿去
            f = first(contents)
            contents = rest(contents)
            return f
        elif message == 'str':
            # 打印?
            return join_link(contents, ", ")
    return dispatch

# 这个列表是用函数实现的.


# 在构建一个函数,它可以方便地构建一个基于func的linked list.
def to_mutable_link(source):
        """Return a functional list with the same contents as source."""
        s = mutable_link()
        for element in reversed(source):
            # 从最后一个开始, 倒数第二个push到list中, 倒数第三个Push到list中..类推
            s('push_first', element)
        return s

# work & test like this:
suits = ["heart", "diamond", "spade", "club"]
s = to_mutable_link(suits)
print(s('str'))
s('pop_first')
print(s('str'))


# message passing to implement dict.

def dictionary():
    """
    Return a functional implementation of a dictionary.
    """

    records = []
    def getitem(key):
        matches = [r for r in records if r[0] == key]
        if len(matches) == 1:
            key, value = matches[0]
            return value
    def setitem(key, value):
        nonlocal records
        non_matches = [r for r in records if r[0] != key]
        records = non_matches + [[key, value]]
    def dispatch(message, key=None, value=None):
        if message == 'getitem':
            return getitem(key)
        elif message == 'setitem':
            setitem(key, value)
    return dispatch


# dispatch dict

def account(initial_balance):
    # 首先用函数实现一个dict: account
    def deposit(amount):
        dispatch['balance'] += amount
        return dispatch['balance']
    def withdraw(amount):
        if amount > dispatch['balance']:
            return 'Insufficient funds'
        dispatch['balance'] -= amount
        return dispatch['balance']
    dispatch = {'deposit':   deposit,
                'withdraw':  withdraw,
                'balance':   initial_balance}
    return dispatch
  
def withdraw(account, amount):
    # 返回取款后剩余的balance（存款量）
    return account['withdraw'](amount)
def deposit(account, amount):
    # 返回存款后剩余的balance（存款量）
    return account['deposit'](amount)
def check_balance(account):
    # 检查存款量
    return account['balance']

a = account(20)
deposit(a, 5)
withdraw(a, 17)
check_balance(a)
