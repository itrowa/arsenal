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
size = input_size      # 格点数量
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
    def __init__(self, indx, indy, indz):
        self.indx = indx
        self.indy = indy
        self.indz = indz

        self.state = random.randint(0, 1)
        self.previous = self.state

    def savePrevious(self):
        """ 将当前状态保存下来. """
        self.previous = self.state

    def newState(self, s):
        """ 用状态s更新此元胞的状态. """
        self.state = s

    def getState(self):
        """ 返回元胞的状态 """
        return self.state

class CelluarSpace:
    """ 元胞空间的生成和演化控制."""
    def __init__(self, gridSize, interval):
        self.gridSize = gridSize            # 格点数量
        self.interval = interval            # 格点距离
        self.board = [[[Cell(i, j, k) for k in range(self.gridSize)] for j in range(self.gridSize)] for i in range(self.gridSize)]

    def __repr__(self):
        return "a Celluar Space obj."

    def getState(self):
        """ 返回一个三维数组, 记录当前各个格点的状态 """
        return [[[self.board[i][j][k].getState() for k in range(self.gridSize)] for j in range(self.gridSize)] for i in range(self.gridSize)]

    def generate(self):
        """ 计算下一个状态. (规则集和DSL可以在这里开始发挥.)"""

        # 先保存每一个元胞的当前状态.
        for i in range(self.gridSize):
            for j in range(self.gridSize):
                for k in range(self.gridSize):
                    self.board[i][j][k].savePrevious()

        for j in range(1, self.gridSize - 1):
            for k in range(1, self.gridSize - 1):
                self.board[0][j][k]

        # 更新每一个元胞的状态. ()
        # for i in range(1, self.gridSize - 1):
        #     for j in range(1, self.gridSize - 1):
        #         for k in range(1, self.gridSize - 1):
        #             neighbors = 0
        #             if self.board[i][j][k+1].state == 1:
        #                 neighbors += 1
        #             elif self.board[i][j][k-1].state == 1:
        #                 neighbors += 1
        #             elif self.board[i-1][j][k].state == 1:
        #                 neighbors += 1
        #             elif self.board[i+1][j][k].state == 1:
        #                 neighbors += 1
        #             elif self.board[i][j-1][k].state == 1:
        #                 neighbors += 1
        #             elif self.board[i][j+1][k].state == 1:
        #                 neighbors += 1

        #             if self.board[i][j][k].state == 1 and neighbors < 1:
        #                 self.board[i][j][k].newState(0);
        #             elif self.board[i][j][k].state == 1 and neighbors > 4:
        #                 self.board[i][j][k].newState(0);
        #             elif self.board[i][j][k].state == 0 and neighbors >= 3:
        #                 self.board[i][j][k].newState(1);

    def isAtBorder(self, cell):
        """ 测试元胞是否在格点边界上."""
        if cell.indx == 0 or cell.indx == gridSize:
            return True
        elif cell.indy == 0 or cell.indy == gridSize:
            return True
        elif cell.indz == 0 or cell.indz == gridSize:
            return True
        else:
            return False

    def retrieveNeighborsAttr(cell, attr):
        # 顺序: 上-下-左-右-前-后
        attrList = []
        # if cell.indz == gridSize:





#############################################
# 初始化相关数据
#############################################

# 初始化状态列表
space = CelluarSpace(size, interval)

# 初始化格点网
grid = [[[rg.Point3d(i*interval, j*interval, k*interval) for k in range(size)] for j in range(size)] for i in range(size)]
grid = WorldToGH(grid, rg.Point3d)


#############################################
# Output to GH
#############################################
# 把生成为一个gh的树形数据, 每个path下就只有一个item 要么true要么false
# 再生成一个同样规模的格点, 用cull pattern筛选掉那些不是true的格点

# 状态列表
# a = WorldToGH(space.getState(), int)

# 格点网
# b = grid


for t in range(time):
    space.generate()
    a = WorldToGH(space.getState(), int)

b = grid
