# 功能不太完善; 第一次所有的值算出来以后程序就不再工作了; 一旦清除某个connector的值, 
# 其它所有连接的全部也被清除掉了.
# square = bay * depth

from operator import add, sub, mul, truediv

class ternary_constraint:
    def __init__(self, a, b, c, f_ab, f_ca, f_cb, name=None):
        """ 把a, b, c 连接到这个constraint box.
            根据标准3路的约束. 根据3个connector值的情况 
            利用其中2个的值设置第三个的值.

            b, b, c: 三个connector
            剩下的三个参数: 两两之间的函数关系.
            eg: 
            constraint(a, b, c, add, sub, sub) ???
        """
        for connector in (a, b, c):
            connector.connect(self)

        # 把指针拷贝过来
        self.a = a
        self.b = b
        self.c = c
        self.f_ab = f_ab
        self.f_ca = f_ca
        self.f_cb = f_cb
        self.name = name

    def __repr__(self):
        if self.name == None:
            return "Anonymous Constraint: "
        else:
            return "Constraint: " + self.name 

    def update_value(self):
        """ 根据标准3路的约束. 根据3个connector值的情况 
            利用其中2个的值设置第三个的值.
        """
        av, bv, cv = [connector.has_value() for connector in (self.a, self.b, self.c)]

        if av and bv:
            self.c.set_value(self, self.f_ab(self.a.value, self.b.value))
        elif av and cv:
            self.b.set_value(self, self.f_ca(self.c.value, self.a.value))
        elif bv and cv:
            self.a.set_value(self, self.f_cb(self.c.value, self.b.value))

    def forget_value(self):

        """ 通知其他所有连接过来的connector忘掉自己的值
        """
        for connector in (self.a, self.b, self.c):
            connector.forget_value(self)


class constant_constraint:
    def __init__(self, connector, value):
        """ 一个常数constraint box. 接受一个connector, 并且为其设置一个值.
        """
        connector.set_value(self, value)

class connector:
    def __init__(self, value=None, name=None):
        self.value = value          # connector的值
        self.name = name            # name是一个connector可选的属性
        self.constraints = []       # connector连接到的constraint列表

    def __repr__(self):
        s = ''
        if self.name != None:
            s += name + 'Connector'
        else:
            s += 'Anonymous Connector: '
        return s + str(self.value)

    def set_value(self, source, value):
        # if self.value is None:
        self.value = value    

        # update other all constraint boxes
        for c in self.constraints:
            if c != source:
                c.update_value()

    def forget_value(self, source):
        self.value = None
        # update other all constraint boxes
        for c in self.constraints:
            if c != source:
                c.forget_value()

    def has_value(self):
        return self.value is not None

    def connect(self, source):
        self.constraints.append(source)

def adder(a, b, c, name=None):
    """ 一个 a + b = c 的约束
    """
    return ternary_constraint(a, b, c, add, sub, sub, name)

def multiplier(a, b, c, name=None):
    """ 一个a * b = c 的约束
    """
    return ternary_constraint(a, b, c, mul, truediv, truediv)

#############################################

# 创建3个connector
b, d, s = [connector() for _ in range(3)]

# 建立1个constant constraint
bc = constant_constraint(b, 8000)


# 建立约束
sqs = adder(b, d, s, 'b+d=s')

# 
# s.set_value('user', 32000)


#############################################
# 摄氏度到华氏度的转换

c = connector()
f = connector()

u, v, w, x, y = [connector() for _ in range(5)]

multiplier(c, w, u)
multiplier(v, x, u)
adder(v, y, f)

constant_constraint(w, 9)
constant_constraint(x, 5)
constant_constraint(y, 32)

c.set_value('user', 25)