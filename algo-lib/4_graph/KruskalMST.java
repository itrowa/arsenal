// 计算最小生成树的Kruskal算法
// @todo : 结果不太对, 尽管程序正常运行了.
public class KruskalMST {
    private Queue<Edge> mst;                // 保存最小生成树的队列

    public KruskalMST(EdgeWeightedGraph G) {
        mst = new Queue<Edge>();
        MinPQ<Edge> pq = new MinPQ<Edge>();         // 存储图的边按权重排序的结果

        // 把所有边装进去
        for (Edge e : G.edges())
            pq.insert(e);
        UF uf = new UF(G.V());                      // 这个对象用于判断这些边是否会生成环.

        while (!pq.isEmpty() && mst.size() < G.V() - 1) {
            Edge e = pq.delMin();                   // 取出所有边种权重最小的一条
            int v = e.either();
            int w = e.other(v);
            if (uf.connected(v, w))
                continue;                           // 忽略失效的边
            uf.union(v, w);                         // 合并分量
            mst.enqueue(e);                         // 将e添加到最小生成树中
        }
    }

    // 返回最小生成树所有的边
    public Iterable<Edge> edges() {
        return mst;
    }

    //public double weight()
    // @todo
    
    // test
    // $ java KruskalMST tinyEWG.txt
    public static void main(String[] args) {
        In in = new In(args[0]);
        EdgeWeightedGraph G = new EdgeWeightedGraph(in);
        KruskalMST mst = new KruskalMST(G);
        for (Edge e : mst.edges()) {
            StdOut.println(e);
        }
    }
}