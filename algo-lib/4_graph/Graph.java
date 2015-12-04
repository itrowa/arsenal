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

    // constructor: 通过一个In对象 构造一张图: 注意课本上对输入流格式的要求.
    public Graph(In in)
    {
        this(in.readInt());             // 调用同名构造函数~
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
    
    // 返回v的度数
    public static int degree(Graph G, int v) {
        int degree = 0;
        for (int w : G.adj(v)) degree++;
        return degree;
    }
            
    // main test
    public static void main(String[] args) {
        Graph G = new Graph(new In(args[0]));
        StdOut.println(G.E());
        StdOut.println(degree(G, 0));
    }
    // note: 关于In class的解释http://algs4.cs.princeton.edu/12oop/In.java.html
}