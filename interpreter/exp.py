def curried_pow(x):
    def h(y):
        return pow(x, y)
    return h
    
f = curried_pow(2)
f(3)




(lambda (y) (lambda (x) (* y 2)))