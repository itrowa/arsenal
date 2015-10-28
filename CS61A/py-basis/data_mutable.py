lst = [1, 2, 3, 4]
c = b = ['foo', 'bar']
lst[0] = b
print(lst)
# [['foo', 'bar'], 2, 3, 4]

b[1] = 'ply'
print(lst)
# [['foo', 'ply'], 2, 3, 4]

b = ['farply', 'garply']
print(lst)
# [['foo', 'ply'], 2, 3, 4]             
# why??我的理解是， lst[0]引用到是对象是和b引用的对象是同一个对象。 即['foo', 'bar']. b引用到其它对象了， 但是lst[0]还是引用到的['foo', 'bar']

print(c is lst[0])