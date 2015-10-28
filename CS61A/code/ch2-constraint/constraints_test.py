from operator import add, sub, mul, truediv

def multiplier(a, b, c):
    """The constraint that a * b = c."""
    return make_ternary_constraint(a, b, c)


def make_ternary_constraint(a, b, c):
    def new_value():
        av, bv, cv = [connector['has_val']() for connector in (a, b, c)]  #关键还是在于这一句看不懂!!!!
        # connector['has_val']()是一句调用那个dict中的匿名函数的call expression.
        # 所以它们三个的值要么是True,要么是False
        print("....")
        print(av)
        print(bv)
        print(cv)
        if av and bv:
            c['set_val'](constraint, add(a['val'], b['val']))
        elif av and cv:
            b['set_val'](constraint, add(c['val'], a['val']))
        elif bv and cv:
            a['set_val'](constraint, add(c['val'], b['val']))
    def forget_value():
        for connector in (a, b, c):
            connector['forget'](constraint)
    constraint = {'new_val': new_value, 'forget': forget_value}
    for connector in (a, b, c):
        connector['connect'](constraint)

    constraint = {'new_val': new_value}

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

c = connector('Celsius')
w = connector()
u = connector()
multiplier(c, w, u)

# 这个程序  那个if测试语句... 完全就没跑过