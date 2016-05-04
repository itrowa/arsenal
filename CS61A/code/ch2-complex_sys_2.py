# type dispatching 风格的 数理运算系统(包含复数和有理数的相加, 相乘)

# 最顶层的Number class重载了__add__和__mul__两个方法; 使得由Rational 和ComplexRI, ComplexMA创建的obj可以跨类型相加, 相乘.


# 仍然是最顶层的Number class:
from fractions import gcd

def add_complex_and_rational(c, r):
    return ComplexRI(c.real + r.numer/r.denom, c.imag)

def mul_complex_and_rational(c, r):
    r_magnitude, r_angle = r.numer/r.denom, 0
    if r_magnitude < 0:
        r_magnitude, r_angle = -r_magnitude, pi
    return ComplexMA(c.magnitude * r_magnitude, c.angle + r_angle)

def add_rational_and_complex(r, c):
    return add_complex_and_rational(c, r)
def mul_rational_and_complex(r, c):
    return mul_complex_and_rational(c, r)


class Number:
	def __add__(self, other):
		# 根据两个要相加的书的type_tag 来判断
		if self.type_tag == other.type_tag:
			# 相同类型的数据, 共享同一个interface, 所以可以用self.add方法.
			# 而且self.add方法就是在Rational中定义的add方法, 或者是Complex中定义的add方法
			return self.add(other)
		elif self.type_tag != other.type_tag:
			# 不同类型的数据, 根据它们标签的不同和排列顺序, 调用不同的相加方法. 判断的过程用self.cross_apply来处理.
			return self.cross_apply(other, self.adders)   # self.addders 是一个字典.
	def __mul__(self, other):
		if self.type_tag == other.type_tag:
			return self.mul(other)
		elif self.type_tag != other.type_tag:
			return self.cross_apply(other, self.multiplers)

	def cross_apply(self, other, cross_fns):
		# other是另外一个操作数
		cross_fn = cross_fns[(self.type_tag, other.type_tag)]
		return cross_fn(self, other)

	adders = {("com", "rat"): add_complex_and_rational,
			   ("rat", "com"): add_rational_and_complex}
	multiplers = {("com", "rat"): mul_complex_and_rational,
			       ("rat", "com"): mul_rational_and_complex}

class Rational(Number):
	# 实数构造器, 利用class实现

	# 新增type_tag
	type_tag = "rat"

	def __init__(self, numer, denom):
		g = gcd(numer, denom)
		self.numer = numer // g
		self.denom = denom // g
	def __repr__(self):
		return 'Rational({0}, {1})'.format(self.numer, self. denom)
	def add(self, other):
		nx, dx = self.numer, self.denom
		ny, dy = other.numer, other.denom
		return Rational(nx * dy + ny * dx, dx * dy)
	def mul(self, other):
		numer = self.numer * other.numer
		denom = self.denom * other.denom
		return Rational(numer, denom)

class Complex(Number):
	# 这个类创建的目的是让add和mul分别都能被ComplexRI和ComplexMA创建的实例所使用.
	# 继承可以让我们少写代码!

	# 新增type_tag
	type_tag = "com"

	def add(self, other):
		# 加法取的是复数的实部和虚部分别相加
		return ComplexRI(self.real + other.real, self.imag + other.imag)
	def mul(self, other):
		# 乘法取的是复数的极角相加
		magnitude = self.magnitude * other.magnitude
		return ComplexMA(magnitude, self.angle + other. angle)


# +++++++++++++++++++++++++++++++++++++++
# barrier
# +++++++++++++++++++++++++++++++++++++++

class ComplexRI(Complex):
	# 复数的直角坐标表示.
	def __init__(self, real, imag):
		self.real = real
		self.imag = imag

	# 使用Property属性, 函数访问magnitude的时候就直接调用magnitude方法.
	@property
	def magnitude(self):
		return (self.real **2 + self.imag **2) ** 0.5

	@property 
	def angle(self):
		return atan2(self.imag, self.real)

	def __repr__(self):
		return 'ComplexRI({0:g},{1:g})'.format(self.real, self.imag)
	# 现在, ComPlexRI有4个attr了, 分别是real, imag, magnitude, angle. 后两个其实是method.

class ComplexMA(Complex):
	# 复数的极坐标表示
	def __init__(self, magnitude, angle):
		self.magnitude = magnitude
		self.angle = angle

	@property
	def real(self):
		return self.magnitude * cos(self.angle)

	@property
	def imag(self):
		return self.magnitude * sin(self.angle)

	def __repr__(self):
		return 'ComplexMA({0:g}, {1:g} * pi)'.format(self.magnitude, self.angle/pi)
	# 通过ComplexMA创建的对象也同时拥有magnitude, angle, real, imag 4个attr.