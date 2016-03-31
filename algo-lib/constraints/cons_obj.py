class tenery_constraint:
    # 一个三路约束object.
    def __init__(self, a, b, c, ab, ca, cb):
        # a, b, c, 分别是3个 connector obj, 后面三个参数分别是它们
        # 之间的数学关系(加减乘除的函数名)
        self.a = a
        self.b = b
        self.c = c
        self.ab = ab
        self.ca = ca
        self.cb = cb

    def new_value(self):
        # 如果3个端口中恰好两个端口有值, 那么
        # 我根据三个端口中两个端口的值, 设置第三个端口的值.

        # 对于a, b, c而言, 哪两个有值?
        av, bc, cv = connector.has_val() for connector in (self.a, self.b, self.c)

        if av and bv:
            self.c.set_value(self.ab(self.a.val, self.b.val))
        elif av and cv:
            self.b.set_value(self.ca(self.c.val, self.a.val))
        elif bv and cv:
            self.a.set_value(self.cb(self.c.val, self.b.val))

    def forget_value(self):
        for connector in (self.a, self.b, self.c):
            connector.forget_value(self)

class constant_constraint:
    # 一个常量约束object
    # 常量约束的值是存储在和它连接的connector对象中的.
    def __init__(self, value, connector):
        # connector: 连接到此常量约束的connector
        # value: 要设置的值
        connector.set_value(self, value)

class connector:
    # 连接两个tenery constraint obj的连接器.
    # 这个对象存储着一个"值", 它把值送到和它连接的三路约束对象或者是
    # 常量约束对象上.
    def __init__(self, name = None):
        self.informant = None          # 通知对象(记录着通知到此连接器的对象名)
        self.constraints = []          # 约束中链接到的对象
        self.val = None                # connector的值
        self.name = name               # connector的名字(可选)

    def has_val(self):
        # 此connector是否有值?
        return self.val is not None

    def connect(self, source):
        # 连接到一个约束对象
        self.constraints.append(source) 

    def set_value(self, source, value):
        # source约束传来了设置值的指令. 命令我将所有连接到的约束对象
        # 的值设置为value.
        if val is None:
            self.informant, self.val = source, value
            if name is not None:
                print(name, '=', value)
            inform_all_except(source, new_value, self.constraints) #~~

    def forget_value(source):
        if self.informant == source:
            informant, self.val = None, None
            if name is not None:
                print(name, 'is forgotten')
            inform_all_except(source, forget_value, self.constraints) #~~


    def inform_all_except(source, op, constraints):
        for c in constraints:
            if c != source:
                c.op()

if __name__=="__main__":
    celsius = connector("Celsius")
    fahrenheit = connector('Fahrenheit')

    # 创建一个摄氏度到华氏度的约束系统.
    u, v, w, x, y = [connector() for _ in range(5)]

    

