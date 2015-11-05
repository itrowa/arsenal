# dict
# 是key-value 的 pair. 这些pair的 order是不确定的,没有先后顺序的.尽管写起来是有先后顺序的.

# "声明" 一个空的dict(实际是引用一个空dict)
d1 = {}

# 正常的dict的创建并用变量引用它.

numerals = {'I': 1.0, 
            'V': 5, 
            'X': 10
           }

# print
print(numerals)

# 通过Key查找value:
q = numerals['X']

# 给Key设置新的Value, 或者增加新的pair:
numerals['I'] = 1
numerals['L'] = 50

# 查找key是否存在：
'V' in numerals
# note: 不要使用if numeral['V'] 这样的判断,因为解释器会先去求值numeral['V']并可能返回异常

#or:
if 'V' in numerals:
    pass



# old,, another ------------------------------------

# ab = {	'Swaroop'	: 'swarropch@byteofpython.info',
# 		'Larry'		: 'larry@wayy.org',
# 		'Matsumoto'	: 'matz@ruby-lang.org',
# 		'Spammer'	: 'spammer@hotmail.com'
# 	}
	
# print "Swaroop's address is %s" % ab['Swaroop']

# # Adding a key/value pair
# ab['Guido'] = 'guido@python.org'

# # Del a key/value pair
# del ab['Spammer']

# print '\nThere are %d contacts in the address-book\n' % len(ab)
# for name, address in ab.items():
# 	print 'Contact %s at %s' % (name, address)
	
# if 'Guido' in ab: # OR ab.has_ley('Guido')
# 	print "\nGuido's address is %s" % ab['Guido']
