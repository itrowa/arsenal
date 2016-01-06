// 算法:有向图的dfs搜索: 对于有向图G而言, 从顶点s或者一系列顶点sources开始, 是否存在到v的路径?
// java DirectedDFS tinyDG.txt 1
// java DirectedDFS tinyDG.txt 1 2 6

public class DirectedDFS() {
    private boolean[] marked;

    // 构造函数.
    public DirectedDFS(Digraph G, int s) {
        marked = new boolean[G.V()];
        dfs(G, s);
    }

    // 针对有多个顶点作为开始搜死的起点的情况.
    public DirectedDFS(Digraph G, Iterable<Integer> sources) {
        marked = new boolean[G.V()];
        for (int s : sources)
            if (!marked[s] dfs(G, s))
    }

    public dfs(Diraph G, int v) {
        marked[v] = true;
        for (int w : G.adj(v))
            if(!marked[w]) dfs(G, w);
    }

    public marked(int v) {
        return marked[v];
    }

    // test routine
    public static void main(String[] args) {
        // 根据输入流的第一个参数读取并生成有向图G
        Digraph G = new Digraph(new In(args[0]));

        // 根据后面的几个参数读取并作为搜索开始的点.点是多个.
        Bag<Integer> sources = new Bag<Integer>();
        for (int i = 1; i < args.length; i++)
            sources.add(Integer.parseInt(args[i]));

        DirectedDFS reachable = new DirectedDFS(G, sources);

        for (int v = 0; v < G.V(); v++)
            if (reachable.marked(v)) 
                StdOut.print(v + " ");
        StdOut.println();
    }
}