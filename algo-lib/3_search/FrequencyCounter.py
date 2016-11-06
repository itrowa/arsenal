# 记录从某个文本文件中得到的一系列字符串并记录每个字符串的出现次数，然后遍历
# 所有键找出频率最高的键.

# 这里自己替换成想要的算法.
from SequentialSearchST import *

# usage: 
# py -3 st-client.py tinyTale.txt

import sys

if __name__ == "__main__":
    # 从命令行参数读取文本文件并截断为单词list
    infile = open(sys.argv[1], "r")
    text = infile.read().split()
    infile.close()

    # 统计单词出现次数并装入symbol table. 
    
    st = SequentialSearchST()
    for word in text:
        if st.contains(word):
            st.put(word, st.get(word)+1)
        else:
            st.put(word, 1)

        
