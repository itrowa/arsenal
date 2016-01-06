// java TestSearch tingG.txt 0
// 仅作为思路演示, 实际并不工作. 必须把Search类替换成对应的类名才能正常工作.

// 接受从标准输入流的名称和起始节点的编号,从输入流中读取一幅图, 用它和给定的起始节点
// 创建一个Search对象, 然后用marked()打印出图中和起点联通的所有顶点.
public class TestSearch {
    public static void main (String[] args) {
        Graph G = new Graph(new In(args[0]));
        int s = Integer.parseInt(args[1]);
        Search search = new Search(G, s);

        for (int v = 0; v < G.V(); v++) {
            if (search.marked(v))
                StdOut.print(v + " ");
        }
        StdOut.println();

        if (search.count() != G.V())
            StdOut.print("NOT ");
        StdOut.println("connected");
    }
}