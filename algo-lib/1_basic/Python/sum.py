# 几种典型程序的倍率实验.

import numpy as np
import matplotlib.pyplot as plt  
from stopwatch import stopWatch
from random import randint

def threeSum(l):
    """
    找出l中N个数中和为0的组合的数量.
    """
    # 要注意返回值可能是0!
    cnt = 0
    N = len(l)
    for i in range(0, N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if l[i] + l[j] + l[k] == 0:
                    # print("{0},{1},{2}\n".format(i, j, k))
                    cnt += 1
    return cnt

#ThreeSum()

@stopWatch
def testCase(N):
    # 生成一个长度为N的随机数列表, 每个随机数都是6位的整数
    # 然后将这个统计此列表中3个数和为0的组合出现次数.
    numlst = []
    for i in range(N):
        numlst.append(randint(-100000,100000))
    # print(numlst)
    return threeSum(numlst)

if __name__ == "__main__":
    cnt=250
    timelog=[]
    sizelog=[]
    while(cnt <= 10000):
        timelog.append(testCase(cnt))
        sizelog.append(cnt)
        cnt *= 2

    # evenly sampled time at 200ms intervals  
    t = np.arange(0., 5., 0.2)  
    # red dashes, blue squares and green triangles  
    plt.plot(sizelog, timelog)  
    plt.xlabel('size')  
    plt.ylabel('time consumed')  
    plt.show()  