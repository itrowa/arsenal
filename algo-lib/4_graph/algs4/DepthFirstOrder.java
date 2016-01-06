// 有向图中基于深度优先搜索的顶点排序算法.
// 该算法允许用例以3种顺序遍历一个无环图的深度优先搜索经过的所有顶点.
// 前序: 在递归调用dfs搜索节点v之前把v放入queue中
// 后序: 在递归调用dfs搜索节点v之后把v放入queue中
// 逆后序: 在递归调用dfs搜索节点v之后把v放入stack中.

// note: 要求图是无环的, 该class不会检测图是无环的, 而是假设图已经是无环的.

public class DepthFirstOrder {
    private boolean[] marked;
    private Queue<Integer> pre;
    private Queue<Integer> post;
    private Stack<Integer> reversePost;

    public DepthFirstOrder(Digraph G) {
        pre = new Queue<Integer>();
        post = new Queue<Integer>();
        reversePost = new Stack<Integer>();
        marked = new boolean[G.V()];

        for (int v = 0; v < G.V(); v++)
            if (!marked[v]) dfs(G, v);
    }

    private void dfs(Digraph G, int v) {
        pre.enqueue(v);

        marked[v] = true;
        for (int w : G.adj(v))
            if (!marked[w])
                dfs(G, w);

        post.enqueue(v);
        reversePost.push(v);
    }

    public Iterable<Integer> pre() {
        return pre;
    }
    public Iterable<Integer> post() {
        return post;
    }
    public Iterable<Integer> reversePost() {
        return reversePost;
    }

    public static void main(String[] args) {
       // 
    }
}