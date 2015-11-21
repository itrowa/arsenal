// 这个算法依赖的symbolDiraph还没写.
public class Topological {
    private Iterable<Integer> order;            // 顶点的拓扑排序

    public Topological(Digraph G) {
        DirectedCycle cyclefinder = new DirectedCyele(G);
        if (!cyclefinder.hasCycle()) {
            DepthFirstOrder dfs = new DepthFirstOrder(G);
            order = dfs.reversePost();
        }
    }

    public Iterable<Integer> order() {
        return order;
    }

    public boolean isDAG() {
        return order != null;
    }

    public static void main(String[] args) {
        String filename = args[0];
        String separator = args[1];
        SymbolDigraph sg = new SymbolDigraph(filaneme, separator);
        Topological top = new Topological(sg.G());

        for (int v : top.order())
            StdOut.println(sg.name(v));
    }
}