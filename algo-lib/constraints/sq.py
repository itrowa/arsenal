from constraint import *

bay = connector("bay")
depth = connector("depth")
area = connector("area")

constant(bay, 3200)   # 开间为3200mm

multiplier(bay, depth, area)
 
area['set_val']('user', 100000000)  # 设置目标面积为100m^2
