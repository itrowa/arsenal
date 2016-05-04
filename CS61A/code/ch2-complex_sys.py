# multiple representation, 对应composing program 2.7

from math import atan2, sin, cos, pi

class Number:
	# 这个类作为Complex的父类的目的只是为了能使用加法和乘法 + *
	def __add__(self, other):
		return self.add(other)
	def __mul__(self, other):
		return self.mul(other)

class Complex(Number):
	# 这个类创建的目的是让add和mul分别都能被ComplexRI和ComplexMA创建的实例所使用.
	# 继承可以让我们少写代码!
	def add(self, other):
		# 加法取的是复数的实部和虚部分别相加
		return ComplexRI(self.real + other.real, self.imag + other.imag)
	def mul(self, other):
		# 乘法取的是复数的极角相加
		magnitude = self.magnitude * other.magnitude
		return ComplexMA(magnitude, self.angle + other. angle)
	# 这个class 假定complexRI 和MA都已经存在; 
from fractions import gcd

# @@ 新加的
class Rational(Number):
	# 实数构造器, 利用class实现
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
		return 'ComplexRI({0:g},{1:g})'.format(self.real, self, imag)
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


# 搞懂class的继承关系:

# 	Number
# 	  |
# 	Complex
# |            |
# ComplexRI	ComplexMA

# 实例化一个复数对象的时候,要么通过ComplexRI, 要么通过ComplexMA来完成. 这也解释了为什么__init__方法会写在这两个地方.

# 然后,因为这两个class都继承自Complex, 所以都有add,mul方法.