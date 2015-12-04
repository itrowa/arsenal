// 加权无向图数据类型
public class EdgeWeightedGraph {
    private final int V;                // 顶点总数
    private int E;                      // 边的总数
    private Bag<Edge>[] adj;            // 邻接表

    public EdgeWeightedGraph(int V) {
        this.V = V;
        this.E = 0;
        adj = (Bag<Edge>[]) new Bag[V];
        for (int v = 0; v < V; v++)
            adj[v] = new Bag<Edge>();
    }

    // 从输入读取一张加权无向图
    public EdgeWeightedGraph(In in) {
        this(in.readInt());
        int E = in.readInt();    // 如果是this.E = ... 就会出错.. why @?@
        StdOut.println(V);
        StdOut.println(E);
        for (int i = 0; i < E; i++) {
            int v = in.readInt();
            int w = in.readInt();
            // 加入一个判断v和w是不是越界的判断 @todo
            double weight = in.readDouble();
            addEdge(new Edge(v, w, weight));
        }
    }

    public int V() {
        return V;
    }

    public int E() {
        return E;
    }

    // 向图中添加一条边e
    public void addEdge(Edge e) {
        int v = e.either();
        int w = e.other(v);
        adj[v].add(e);
        adj[w].add(e);
        E++;
    }

    // 返回和顶点v相关联的所有边
    public Iterable<Edge> adj(int v) {
        return adj[v];
    }

    // 图的所有边
    public Iterable<Edge> edges() {
        Bag<Edge> b = new Bag<Edge>();
        for (int v = 0; v < V; v++)
            for (Edge e : adj[v])
                if (e.other(v) > v)
                    b.add(e);
        return b;
    }

    // 对象的字符串表示
    public String toString() {
        String s = V + " vertices, " + E + " edges\n";
        for (int v = 0; v < V; v++) {
            s +=  v + ": ";
            for (Edge e : adj[v])
                s += e + ", ";
            s += "\n";
        }  
        return s;

    }

    // $ java EdgeWeightedGraph tinyEWG.txt
    public static void main(String[] args) {
        In in = new In(args[0]);
        EdgeWeightedGraph G = new EdgeWeightedGraph(in);
        StdOut.println(G);

    }


}