// 这个算法依赖的symbolDiraph还没写.
// 1.DirectedCycle判断一个图是否是无环的.
// 2.DepthFirstOrder返回无环图的拓扑排序结果.

// $ java Topological jobs.txt "/"
public class Topological {
    private Iterable<Integer> order;            // 顶点的拓扑排序结果.

    // 构造函数, 其结果是存储了图顶点的逆后序排序结果.
    public Topological(Digraph G) {
        DirectedCycle cyclefinder = new DirectedCycle(G);
        if (!cyclefinder.hasCycle()) {
            DepthFirstOrder dfs = new DepthFirstOrder(G);
            order = dfs.reversePost();
        }
    }

    // 返回拓扑排序结果
    public Iterable<Integer> order() {
        return order;
    }

    // 图是无环图吗?
    public boolean isDAG() {
        return order != null;
    }

    public static void main(String[] args) {
        String filename = args[0];
        String separator = args[1];
        SymbolDigraph sg = new SymbolDigraph(filename, separator);
        Topological top = new Topological(sg.G());

        for (int v : top.order())
            StdOut.println(sg.name(v));
    }
}