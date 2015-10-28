def divide(x,y):
    return x / y

try:
    # 可能引发exception的代码放入此处.
    # 试着取消这些注释.

    # 正常代码
    divide(5, 6)

    # 产生ZeroDivisionError
    # divide(5, 0)       

    # 产生NameError  
    #a                   

    # 产生TypeError    
    #'2' + 2             

    # 产生ValueError
    # int("I AM A STRING")
except ZeroDivisionError as zde:
    # 如果try suite的执行中匹配到了ZeroDivisionError:执行这里的suite
    print("** 1st suite executed!")
    print("Error Type:", type(zde))
    print(zde.args)
    print(zde)
except (NameError, TypeError):
    # 如果try suite的执行中匹配到了NameError, TypeError: 执行这里的suite.
    print("** 2nd suite executed!")
else:
    # 如果try suite的执行中没有任何异常被捕获到: 执行这里的suite.
    print("** else suite executed. if u see this line, means no except happend.")
finally:
    # 这个suite总是执行, 且最后执行.
    print("** finally suite executed. this suite always executed and often used for some cleanup. bye!")


# 自己建立异常类
class MyZeroDivisionError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def myDivision(x, y):
    if y == 0:
        raise MyZeroDivisionError(y)
    else:
        return x / y

try:
    myDivision(5,6)
    myDivision(5,0)
except MyZeroDivisionError as e:
    print("**Divider cannot be {0} .".format(e.value))