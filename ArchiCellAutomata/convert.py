import pprint
import clr
clr.AddReference("Grasshopper")
import Grasshopper as gh


# 目前最后一个分支还不能正常工作. 看来判断条件还有点问题.

class PytoGHTree:
    def __init__(self, data):
        self.dataTree = gh.DataTree[int]()
        self.data = data

    def __repr__(self):
        return "a Object that has method to convert to TH Tree."

    def ToGhDataTree(self):
        """ 转换任意多维的python list到GH的DataTree.
        """

        def recAdd(data, path):
            # @todo : 处理第三个情况时 还不行!!
            path = list(path)
            # 1. 不是list , 而就是一个对象(item).
            if type(data) != list:
                self.dataTree.Add(data, gh.Kernel.Data.GH_Path(tuple(path)))

            # 2. 是个list, 里面不再包含list 判断条件还要再加强..
            elif type(data) == list and not isinstance(data[0], list):
                for i in data:
                    self.dataTree.Add(i, gh.Kernel.Data.GH_Path(tuple(path)))
            # 3. 是list, 但是里面还是有list
            elif type(data) == list: 
                path.insert(0, 0) # 给path最前面增加一个0
                recAdd(data[0], tuple(path))
                path[-1] += 1
                print "current path: ", path
                print "current data: ", data
                recAdd(data[1:], tuple(path))

        recAdd(self.data, [0])
        return self.dataTree



# s1 = 5
# s2 = [1, 2, 3]
# s3 = [[1, 2, 3], [4, 5, 6]]

# p1 = PytoGHTree(s1)
# p2 = PytoGHTree(s2)
# p3 = PytoGHTree(s3)
