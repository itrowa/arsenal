import pprint
import clr
clr.AddReference("Grasshopper")
import Grasshopper as gh
import random

# the Rhino Common SDK access
import Rhino.Geometry as rg
import scriptcontext as sc

#############################################
# input from Grasshopper
#############################################
size = input_size + 1      # 格点数量
interval = 3000            # 格点之间的距离

#############################################
# Tree Data Processing
#############################################

def ghDataTreeToPythonList(dataTree):
    
    """ Converts a GH datatree to a nested Python list """
    
    # Create an empty Python list
    pyList = []
    
    # Add the branches of the Gh datatree to this list
    for i in range(DataTree.BranchCount):
        branch = list(DataTree.Branch(i))
        pyList.append(branch)
        
    return pyList

def pythonListTGhDataTree(pythonList):
    
    """ Converts a  nested Python list to a GH datatree """
    
    # Create GH datatree
    dataTree = gh.DataTree[int]()
    
    # Add pythonlist sub lists to dataTree
    for i,l in enumerate(pythonList):
        for v in l:
            dataTree.Add(v,gh.Kernel.Data.GH_Path(i))
            
    return dataTree

def WorldToGH(world, type):
    """ Convert word to GH Tree.
    """
    # Create GH datatree
    dataTree = gh.DataTree[type]()

    # Add pythonlist sub lists to dataTree
    for x, xs in enumerate(world):
        for y, ys in enumerate(xs):
            for item in ys:
                dataTree.Add(item, gh.Kernel.Data.GH_Path(x, y))
    return dataTree

class Cell:
    """ 最玄学的部分. """


#############################################
# 初始化相关数据
#############################################

# 初始化状态列表
state = [[[random.randint(0, 1) for k in range(size)] for j in range(size)] for i in range(size)]
# state = [[[0, 1, 0], [1, 0, 0], [0, 0, 1]],
#          [[1, 0, 0], [0, 0, 1], [1, 1, 1]],
#          [[0, 0, 1], [0, 1, 0], [0, 0, 0]]]

# 初始化格点网
grid = [[[rg.Point3d(i*interval, j*interval, k*interval) for k in range(size)] for j in range(size)] for i in range(size)]
grid = WorldToGH(grid, rg.Point3d)

#############################################
# Output to GH
#############################################
# 把生成为一个gh的树形数据, 每个path下就只有一个item 要么true要么false
# 再生成一个同样规模的格点, 用cull pattern筛选掉那些不是true的格点

# 状态列表
a = WorldToGH(state, int)

# 格点网
b = grid


