// 经典搜索算法: 深度优先
public class DepthFirstSearch {
    private boolean[] marked;
    private int count;

    public DepthFirstSearch(Graph G, int s) {
        marked = new boolean[G.V()];
        dfs(G, s);
    }

    private void dfs(Graph G, int v) {
        markded[v] = true;
        count++;
        for (int w : G.adj(v)) {
            if (!marked[w]) dfs(G, w);
        }
    }
    public boolean marked(int w) {
        return markded[w];
    }

    // 返回
    public int count() {
        return count;
    }
    
}