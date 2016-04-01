# 通用性四则运算的constraint box, 基于sicp的介绍, 用python的class重写.
from operator import add, sub, mul, truediv

class ternary_constraint:
    # 一个三路约束object.
    def __init__(self, a, b, c, ab, ca, cb, name=None):
        """ a, b, c, 分别是3个 connector obj, 后面三个参数分别是它们
            之间的数学关系(加减乘除的函数名)
        """
        self.a = a
        self.b = b
        self.c = c
        self.ab = ab
        self.ca = ca
        self.cb = cb
        self.name = name

    def __repr__(self):
        s = ""
        if self.name == None:
            s += "Anonymous Constraint with " + "[" + repr(self.a) + "][" + repr(self.a) + "][" + repr(self.a) + "]"
        else:
            s += "Constraint '" + self.name + "' with " + "[" + repr(self.a) + "][" + repr(self.a) + "][" + repr(self.a) + "]"
        return s

    def new_value(self):
        """ 如果3个端口中恰好两个端口有值, 那么
            我根据三个端口中两个端口的值, 设置第三个端口的值.
        """
        # 对于a, b, c而言, 哪两个有值?
        av, bv, cv = [connector.has_val() for connector in (self.a, self.b, self.c)]

        if av and bv:
            self.c.set_value(self, self.ab(self.a.val, self.b.val))
        elif av and cv:
            self.b.set_value(self, self.ca(self.c.val, self.a.val))
        elif bv and cv:
            self.a.set_value(self, self.cb(self.c.val, self.b.val))

    def forget_value(self):
        for connector in (self.a, self.b, self.c):
            connector.forget_value(self)

class constant_constraint:
    """ 一个常量约束object
        常量约束的值是存储在和它连接的connector对象中的.
    """
    def __init__(self, value, connector, name=None):
        # connector: 连接到此常量约束的connector
        # value: 要设置的值
        self.name = name                    # 可选的名字
        self.connector = connector          # 连接到此约束对象的connector
        connector.set_value(self, value)    # 向连接到的connector发送set_value()消息

    def __repr__(self):
        s = ""
        if self.name == None:
            s += "Anonymous constant constraint with [" + repr(self.connector) + "]"
        else:
            s += "constant constraint " + self.name + " with [" + repr(self.connector) + "]"
        return s

class connector:
    # 连接两个ternary constraint obj的连接器.
    # 这个对象存储着一个"值", 它把值送到和它连接的三路约束对象或者是
    # 常量约束对象上.
    def __init__(self, value = None, name = None):
        self.informant = None          # 通知对象(记录着通知到此连接器的对象名)
        self.constraints = []          # 约束中连接到的constraint对象的列表
        self.val = value                # connector的值
        self.name = name               # connector的名字(可选)

    def __repr__(self):
        s = ''
        if self.name != None:
            s += 'Connector ' + self.name + ': '
        else:
            s += 'Anonymous Connector: '
        return s + str(self.val)

    def has_val(self):
        """ 此connector是否有值?
        """
        return self.val is not None

    def connect(self, source):
        """ 连接到一个约束对象
        """
        self.constraints.append(source) 

    def set_value(self, source, value):
        """ source约束传来了设置值的指令. 命令我将所有连接到的约束对象
            的值设置为value.
            source: 可以是其它的sonstraint对象, 也可以是'user'
        """

        if self.val is None:
            self.informant, self.val = source, value
            if self.name is not None:
                print("Connector " + self.name + ' = ' + str(value))

            for c in self.constraints:
                if c != source:
                    c.new_value()
            # self.inform_all_except(source, ternary_constraint.new_value, self.constraints) #~~

    def forget_value(source):
        if self.informant == source:
            informant, self.val = None, None
            if self.name is not None:
                print(self.name, 'has forgot its value')

            for c in self.constraints:
                if c != source:
                    c.forget_value()
            # self.inform_all_except(source, ternary_constraint.forget_value, self.constraints) #~~


    def inform_all_except(source, op, constraints):
        """ 通知所有的(除了source以外的)constraints,执行op这个操作.
        """
        for c in constraints:
            if c != source:
                c.op()

def adder(a, b, c, name=None):
    """ 一个 a + b = c 的约束
    """
    return ternary_constraint(a, b, c, add, sub, sub, name)

def multiplier(a, b, c, name=None):
    """ 一个a * b = c 的约束
    """
    return ternary_constraint(a, b, c, mul, truediv, truediv)

if __name__=="__main__":

    # u+v=w的约束系统.

    # 建立三个connector对象
    u = connector(name="input")
    v = connector(name="v")
    w = connector(name="ouput")
        
    # 建立一个constant_constraint对象
    num = constant_constraint(5, v)

    # 建立一个三路约束对象adder box
    box = adder(u, v, w, "adder")

    # 将u, v, w 连接到box
    u.connect(box)
    v.connect(box)
    w.connect(box)

    # 给input connector设置初始值
    u.set_value('user', 1)
    

