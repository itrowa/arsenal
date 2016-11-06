import time
#print("%d %10.8f" % sum_of_n_(100000))

def stopWatch(func):
    def call(n):
        start = time.time()
        func(n)
        end = time.time()
        return end - start
    return call

@stopWatch
def mysum(n):
    the_sum = 0
    for i in range(1, n+1):
        the_sum = the_sum+i
    return the_sum

if __name__ == "__main__":
    s=mysum(1000000)
    # 等价于 StopWatch(summ)(10000)