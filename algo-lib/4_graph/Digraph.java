// 有向图API的实现.

public class Digraph {
    private final int V;
    private int E;
    private Bag<Integer>[] adj;

    // 创建一幅含有V个顶点但没有边的有向图
    public Digraph(int V) {
        this.V = V;
        this.E = 0;
        adj = (Bag<Integer>[]) new Bag[V];
        for (int v = 0; v < V; v++)
            adj[v] = new Bag<Integer>();
    }

    // 求顶点总数
    public int V() {
        return V;
    }

    // 求边的总数
    public int E() {
        return E;
    }

    // 添加一条边v -> w
    public void addEdge(int v, int w) {
        adj[v].add(w);                      // 只是一个单向的, 因此没有adj[w].add(v)
        E++;
    }

    // 从v指出的边连接的所有顶点
    public Iterable<Integer> adj(int v) {
        return adj[v];
    }

    // 该图的反向图(将所有的边方向反转)
    public Digraph reverse() {
        Digraph R = new Digraph();
        for (int v = 0; v < V; v++)
            for (w : adj(v))
                R.addEdge(w, v);
        return R;
    }

    // 字符串表示
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