# coding=utf-8
#constraint system的实现
#constraint 是dict. 是non-local的。
from operator import add, sub, mul, truediv

def adder(a, b, c):
    """
    implement the constraint that a+b = c.
    """
    return make_ternary_constraint(a, b, c, add, sub, sub)

def multiplier(a, b, c):
    """The constraint that a * b = c."""
    return make_ternary_constraint(a, b, c, mul, truediv, truediv)

def constant(connector, value):
    """The constraint that connector = value."""
    constraint = {}
    connector['set_val'](constraint, value)
    return constraint

def make_ternary_constraint(a, b, c, ab, ca, cb):
    """
    The constraint that ab(a,b)=c and ca(c,a)=b and cb(c,b) = a.
    一个3路约束器 
    """
    def new_value():
        av, bv, cv = [connector['has_val']() for connector in (a, b, c)]  #关键还是在于这一句看不懂!!!!
        # connector['has_val']()是一句调用那个dict中的匿名函数的call expression.
        # 所以它们三个的值要么是True,要么是False
        # print("....")
        # print(av)
        # print(bv)
        # print(cv)
        if av and bv:
            c['set_val'](constraint, ab(a['val'], b['val']))
        elif av and cv:
            b['set_val'](constraint, ca(c['val'], a['val']))
        elif bv and cv:
            a['set_val'](constraint, cb(c['val'], b['val']))
    def forget_value():
        for connector in (a, b, c):
            connector['forget'](constraint)
    constraint = {'new_val': new_value, 'forget': forget_value}
    for connector in (a, b, c):
        connector['connect'](constraint)
    return constraint

# 下面是主角：connectors 它是dict，所以有value，但是对local-state有response func.
def connector(name=None):
    """
    A connector between constraints.
    用法：
    connector(name) 返回一个dict.

                 {'val': None,
                 'set_val': set_value,
                 'forget': forget_value,
                 'has_val': lambda: connector['val'] is not None,
                 'connect': lambda source: constraints.append(source)}
                 所有的key的value都是还没应用于参数的。
    connector('celsius')['has_val'] 就对应与这个dict中'vas_val'的value（它是一个函数）
    connector('celsius')['has_val']()调用这个函数。
    """
    informant = None
    constraints = []
    def set_value(source, value):
        nonlocal informant
        val = connector['val']
        if val is None:
            informant, connector['val'] = source, value
            if name is not None:
                print(name, '=', value)
            inform_all_except(source, 'new_val', constraints)
        else:
            if val != value:
                print('Contradiction detected:', val, 'vs', value)
    def forget_value(source):
        nonlocal informant
        if informant == source:
            informant, connector['val'] = None, None
            if name is not None:
                print(name, 'is forgotten')
            inform_all_except(source, 'forget', constraints)
    connector = {'val': None,
                 'set_val': set_value,
                 'forget': forget_value,
                 'has_val': lambda: connector['val'] is not None,
                 'connect': lambda source: constraints.append(source)}
    return connector

def inform_all_except(source, message, constraints):
    """Inform all constraints of the message, except source."""

    for c in constraints:
        if c != source:
            c[message]()

# how to use?

# 假设我们已经有了connector这个constructor了，所以现在
# 创建两个连接器表示celeius和fahrenheit, 得到的只是两个抽象的dict.dict
# Key的value还是没有应用与参数的函数。
celsius = connector('Celsius')
fahrenheit = connector('Fahrenheit')

def converter(c, f):
    """
    Connect c to f with constraints to convert from Celsius to Fahrenheit.
    这个函数把一系列的connector和表示转换关系的constraint都包装起来。 
    仅仅是包装而已。。。
    """
    u, v, w, x, y = [connector() for _ in range(5)]   # 
    # for循环, _的意思就是和x一样，用_是依据惯例，你不想以后使用这个变量。
    # 这一句执行完毕后，u,v,w,等都绑定到了connector()这个函数
    multiplier(c, w, u)    # 在这里开始看不懂
    multiplier(v, x, u)
    adder(v, y, f)
    constant(w, 9)
    constant(x, 5)
    constant(y, 32)

# 最后调用一下完成整个约束网络的创建
converter(celsius, fahrenheit)
# 画一下这个call exp的frame!
#    c: connector('Celsius')
#    f: connector('Fahrenheit')
#    u,v,w,x,y : connector()


# the 'user' set the value of celsius to 25.
celsius['set_val']('user', 25)
# 语法： ['set_val']是一个字典的key,这个key是func,所以整句话是一句call expression.
# 这一句一计算完 connector c 和 f就都出来了,因为celsius的新值通过网络扩散到所有的connector并为他们设置新的值
# Ceisius = 25
# Fahrenheit = 77.0

# 现在再设置fah..的值，会报错。
fahrenheit['set_val']('user', 212)
#返回Contradiction detected: 77.0 vs 212

# 必须要让network忘记celsius的值，才能继续..
celsius['forget']('user')
