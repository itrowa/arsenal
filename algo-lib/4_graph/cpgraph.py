# Graph definition in think complexity.
class Graph(dict):
    def __init__(self, vs=[], es=[]):
        """create a new graph. (vs) is a lst of vertices, es is a list of edges."""
        for v in vs:
            self.add_vertex(v)
        for e in es:
            self.add_edge(e)

    def add_vertex(self, v):
        """add v to the graph"""
        self[v] = {}

    def add_edge(self, e):
        """add e to the graph by adding an entry in both directions.
        if there is already an edge connecting these vertices, then replace it."""
        v, w = e
        self[v][w] = e
        self[w][v] = e              # 无向图所以两边都有.

    def get_edge(self, vs):
        """read a list of vertices(vs) and return a edge if they are 
        connected. or return None."""
        v, w = vs
        try:
            if v in self[v][w] and w in self[v][w]:
                return self[v][w]
            elif v in self[w][v] and w in self[w][v]:
                return self[w][v]
        except:
            return None

    def remove_edge(self, e):
        """remove an edge (e) from the graph."""
        for v in self:
            for i in self[v]:
                if self[v][i] == e:
                    del self[v][i]  # 如何直接把它删除掉?

    def vertices(self):
        """return a list of vertices in the graph."""
        return [v for v in self]

    def edges(self):
        """return a list of edges in the graph."""
        result = []
        for i in self:
            for j in self[i]:
                if self[i][j] not in result:
                    result.append(self[i][j])
        return result

    def out_vertices(self, v):
        """return a list of vertices that come out from given vertice (v).
        """
        return [i for i in self[v] if self[v][i]]

    def out_edges(self, v):
        """return a list of edges that come out from given vertex (v)."""
        return [self[v][i] for i in self[v] if self[v][i]]


    def add_all_edges(self):
        """connect each vertices from scratch to produce a complete graph."""



class Vertex(object):
    def __init__(self, label=''):
        self.label = label
    def __repr__(self):
        return 'Vertex(%s)' % repr(self.label)
    __str__ = __repr__

class Edge(tuple):
    def __new__(cls, e1, e2):
        return tuple.__new__(cls, (e1, e2))
    def __repr__(self):
        return 'Edge(%s, %s' % (repr(self[0]), repr(self[1]))
    __str__ = __repr__

v = Vertex('v')
w = Vertex('w')
e = Edge(v, w)
print(e)

g = Graph([v, w], [e])
print(g)

# test get_edge()
x = Vertex('x')
y = Vertex('y')
f = Edge(x,y)

g.add_vertex(x)
g.add_vertex(y)
g.add_edge(f)

g.edges()
g.get_edge([x,y])

g.edges()