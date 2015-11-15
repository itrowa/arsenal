public class Graph {
    private final int V;                // vertices
    private int E;                      // edges
    private Bag<Integer>[] adj;         // 存储邻接信息的数组

    // constructor: 通过V构造一张图
    public Graph(int V) {
        this.V = V;
        this.E = 0;
        adj = (Bag<Integer>[]) new Bag[V];
        for (int v = 0; v < V; v++)
            adj[v] = new Bag<Integer>();
    }

    // constructor: 通过标准输入流 构造一张图: 注意课本上对输入流格式的要求.
    public Graph(In in)
    {
        this(in.readInt());
        int E = in.readInt();
        for (int i = 0; i < E; i++) {
            int v = in.readInt();
            int w = in.readInt();
            addEdge(v, w);
        }
    }

    // 返回V
    public int V() {
        return V;
    }

    // 返回E
    public int E() {
        return E;
    }

    // 添加一条边
    public void addEdge(int v, int w) {
        adj[v].add(w);
        adj[w].add(v);
        E++;
    }

    // 返回和顶点v邻接的顶点.
    public Iterable<Integer> adj(int v) {
        return adj[v];
    }

    public String toString() {
        String s = V + " vertices, " + E + " edges\n";
        for (int v = 0; v < V; v++) {
            s += v + ": ";
            for (int w : this.adj(v))
                s += w + " ";
            s += "\n";
        }
        return s;
    }
}