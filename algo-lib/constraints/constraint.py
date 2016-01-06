# constraint system which suppor + - * / and its combination.

from operator import add, sub, mul, truediv

def constant(connector, value):
    """ a constraint box that connector = value.
    """
    constraint = {}
    connector['set_val'](constraint, value)
    return constraint

def adder(a, b, c):
    """ a constraint box with 3 terminal a, b, c, hold
        a + b = c.
    """
    return make_ternary_constraint(a, b, c, add, sub, sub)

def multiplier(a, b, c):
    """ 表示 a * b = c的constraint box.
    """
    return make_ternary_constraint(a, b, c, mul, truediv, truediv)

def make_ternary_constraint(a, b, c, ab, ca, cb):
    """ 构造一个标准3路约束关系. a, b, c 是connector, 剩下的是他们之间的函数关系.

        内部构造是一个dispatch dict: Key是object接受的消息.
        Value是要触发的功能.

        过来的connector也让它们忘掉自己的值.
    """
    def new_value():
        """ new_value: 检查哪两个端口
            有值, 然后设置第三个端口的connector的值
        """
        av, bv, cv = [connector['has_val']() for connector in (a, b, c)]

        if av and bv:
            c['set_val'](constraint, ab(a['val'], b['val'])) #?
        elif av and cv:
            b['set_val'](constraint, ca(c['val'], a['val']))
        elif bv and cv:
            a['set_val'](constraint, cb(c['val'], b['val']))

    def forget_value():
        """ 让其他所有连接过来的connector
            忘掉自己的值.
        """
        for connector in (a, b, c):
            connector['forget'](constraint)         #?

    constraint = {'new_val': new_value,
                  'forget' : forget_value}

    # 给连接过来的connector设置好它们应该连接到的constraint.
    for connector in (a, b, c):
        connector['connect'](constraint)

    return constraint

def connector(name = None):
    """ connector: 连接两个constraint box的object.
        这是一个dispatch dict, 通过响应从外界收到的信息和connector连接的
        constraints box 进行交互.
    """
    informant = None                # 记录发送消息的constraint对象
    constraints = []                # 它连接到的constraint.

    def set_value(source, value):
        """ 接受source (一个constraint box)发出的要求: 把值设置为value.
        """
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
        """ source发出请求, 让自己忘掉自己记录的值.
            这里会检查source是否是之前的informant, 如果不是, 不会进行
            "忘记"的操作.
        """
        nonlocal informant
        if informant == source:
            informant, connector['val'] = None, None
            if name is not None:
                print(name, 'is forgotten')
            inform_all_except(source, 'forget', constraints)

    # constructor & attributes
    connector = {'val': None,                       # connector的值
                 'set_val': set_value,
                 'forget': forget_value,
                 'has_val': lambda: connector['val'] is not None,
                 'connect': lambda source: constraints.append(source) }

    return connector

def inform_all_except(source, message, constraints):
    """ inform all constraints of the message, except the source.
    """
    for c in constraints:
        if c != source:
            c[message]()

################################################################
# test
if __name__ == "__main__":
    # 建立两个connector:
    celsius = connector('Celsius')
    fahrenheit = connector('Fahrenheit')

    def converter(c, f):
        """ 建立一系列的primitive constraint box 表示整个约束网络.
            9 * c = 5 * (f - 32)
        """

        # 若干个connector
        u, v, w, x, y = [connector() for _ in range(5)]

        # 若干个constraint
        multiplier(c, w, u)
        multiplier(v, x, u)
        adder(v, y, f)

        # 建立constant constraint
        constant(w, 9)
        constant(x, 5)
        constant(y, 32)

    # 初始化这个网络
    converter(celsius, fahrenheit)

    #  test
    celsius['set_val']('user', 25)
    celsius['forget']('user')
    fahrenheit['set_val']('user', 212)