# 抛弃掉dot exp，直接实现OOP的class和对象

# dispatch dict， 响应get和set
# attributes, 使用local dict attributes来实现。

# 假设我们已经有了一个class(其实它也是个dispatch func, 和make_instance函数
# 返回的那个dispatch_dict结构类似.),,查找任何不属于这个实例的name.然后把这个class
# 传入make_instance作为cls的参数。

def make_instance(cls):
    """Return a new object instance, which is a dispatch dictionary."""
    def get_value(name):
        if name in attributes:
            return attributes[name]
        else:
            value = cls['get'](name)
            return bind_method(value, instance)
    def set_value(name, value):
        attributes[name] = value
    attributes = {}
    instance = {'get': get_value, 'set': set_value}
    # 当访问instance的get key时,即意味着传入get消息, 就相当于调用这个make_instance函数内部的get_value函数.
    # 对于set key来说, 也是如此.
    return instance

def bind_method(value, instance):
    """Return a bound method if value is callable, or value otherwise."""
    if callable(value):
        def method(*args):
            return value(instance, *args)
        return method
    else:
        return value

# When a method is called, the first parameter self will be bound to the value of instance by this definition.

def make_class(attributes, base_class = None):
    '''
    根据attributes(一个字典)创建一个class,class也是用dispatch dict实现的
    '''
    def get_value(name):
        if name in attributes:
            return attributes[name]
        elif base_class is not None:
            return base_class['get'](name)
    def set_value(name, value):
        attributes[name] = value
    def new(*args):
        return init_instance(cls, *args)
    cls = {'get': get_value, 'set': set_value, 'new': new}
    return cls

def init_instance(cls, *args):
    instance = make_instance(cls)
    init = cls['get']('__init__') 
        if init: 
            init(instance, *args)
    return instance


def make_account_class():
    '''
    定义一个和之前Account Class功能相同的class. 不过这次, 使用新的OOP实现.
    到最后, 必须使用make_class函数, 并且把这个frame的name和绑定值传入make_class.
    local()函数搜集这个frame下所有的name和绑定值并打包成为dict,作为make_class()的参数

    '''
    interest = 0.02
    def __init__(self, account_holder):
        # 初始化函数. make_class的实现机制决定了如果需要在new一个object的时候初始化一些变量,必须把这些东西写到__init__这个特定名字的函数中.
        self['set']('holder', account_holder)
        self['set']('balance', 0)
    def deposit(self, amount):
        new_balance = self['get']('balance') + amount
        self['set']('balance', new_balance)
        return self['get']('balance')
    def withdraw(self, amount):
        """
        在balance中减去amount值并返回新的amount值
        """
        balance = self['get']('balance')
        if amount > balance:
            return 'Insufficient funds'
        self['set']('balance', balance - amount)
        return self['get']('balance')
    return make_class(locals())


# 使用

# 调用make_account_class 以得到class
Account = make_account_class()

# 实例化一个Account的object, 这里要使用消息传递机制:
jim_acct = Account['new']('Jim')

# 调用get 方法, 当然也是用消息传递机制
jim_acct['get']('holder')
#'Jim'
jim_acct['get']('interest')
# 0.02 
jim_acct['get']('deposit')(20) 
# 20 
jim_acct['get']('withdraw')(5)
#15


# 在定义一个make_account_class()的子类
def make_checking_account_class():
    """
    和make_account_class()的区别就是withdraw要收费.
    """
    interest = 0.01
    withdraw_fee = 1
    def withdraw(self, amount):
        fee = self['get']('withdraw_fee')
        return Account['get']('withdraw')(self, amount + fee)
    return make_class(locals(), Account)

CheckingAccount = make_checking_account_class()
jack_acct = CheckingAccount['new']('Jack')

# 测试新账户的收费特性
jack_acct['get']('interest')
# 0.01
jack_acct['get']('deposit')(20)
# 20
jack_acct['get']('withdraw')(5)
# 14