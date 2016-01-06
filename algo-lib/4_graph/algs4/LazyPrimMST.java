// 最小生成树的Prim算法的延时实现
// @todo: 没写完
public class LazyPrimMST {
    private boolean[] marked;               // 最小生成树的顶点
    private Queue<edge> mst;                // 最小生成树的边
    private MinPQ<Edge> pq;                 // 横切边, 包括失效的

    public LazyPrimMST(EdgeWeightedGraph G) {
        pq = new MinPQ<Edge>();
        marked = new boolean[G.V()];
        mst = new Queue<Edge>();

        visit(G, 0);                        // 假设G是连通的
        while (!pq.isEmpty()) {
            Edge e = pq.delMin();           // 从pq中获取权重最小的边
            int v = e.either();
            int w = e.other(v);
            if (marked[v] && marked[w])     // 跳过失效的边
                continue;
            mst.enqueue(e);                 // 将边添加到树中
            if (!marked[v]) 
                visit(G, v);
            if (!marked[w])
                visit(G, w);
        }
    }

    private void visit(EdgeWeightedGraph G, int v) {
        marked[v] = true;
        for (Edge e : G.adj(v))
            if (!marked[e.other(v)])
                pq.insert(e);
    }

    public Iterable<Edge> edges() {
        return mst;
    }

    public double weight()  {}
    //...
}