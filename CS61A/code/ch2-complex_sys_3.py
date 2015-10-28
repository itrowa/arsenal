# type coercion


# 1. first , convert rational to complex:

def rational_to_complex(r):
	return ComplexMA(r.numer / r.denom, 0)

# 2. define the Number class:
class Number:
	def __add__(self, other):
		x, y = self.coerce(other)
		return x.add(y)

	def __mul__(self, other):
		x, y = self.coerce(other)
		return x.mul(y)

	def coerce(self, other):
		# 根据self 和other对象的 type_tag进行coercion
		if self.type_tag == other.type_tag:
			return self, other
		elif (self.type_tag, other.type_tag) in self.coercions:
			# self是rational, other是complex, 所以把self转换成complex
			return (self.coerce_to(other.type_tag), other)
		elif (other.type_tag, self.type_tag) in self.coercions:
			# other是rational, self是complex, 所以把other转换成complex
			return (self, other.coerce_to(self.type_tag))

	def coerce_to(self, other_tag):
		coercion_fn = self.coercions[(self.type_tag, other_tag)]
		return coercion_fn(self)

	coercions = {('rat', 'com'): rational_to_complex}
