// 符号图
// $java SymbolGraph routes.txt " "
// 然后输入要查询的顶点名, 程序会返回和其连接的顶点的名字.
public class SymbolGraph {
    private ST<String, Integer> st;             // 存储的是:符号名 -> 索引
    private String[] keys;                      // 存储的是:索引 -> 符号名
    private Graph G;                            // 图

    // 根据file stream指定的文件构造图, 使用delim (sp)来分隔顶点名
    public SymbolGraph(String stream, String sp) {
        st = new ST<String, Integer>();
        
        // 建立st符号表.
        In in = new In(stream);                     // 第一遍
        while (in.hasNextLine()) {
            String[] a = in.readLine().split(sp);  // 读取一行 分割为若干部分,放入数组.

            // 为这一行中的每个字符串关联一个索引
            for (int i = 0; i < a.length; i++) {      
                if (! st.contains(a[i]))
                    st.put(a[i], st.size());
            }
        }

        // 建立keys数组.
        keys = new String[st.size()];
        for (String name : st.keys())
            keys[st.get(name)] = name;
        // StdOut.println(keys);

        // for debug, 列出所有顶点.
        for (int i = 0; i<st.size(); i++) {
            StdOut.println(keys[i]);
        }
        
        // 以st中顶点名对应的索引编号为无向图的节点名, 建立一个Graph G.
        G = new Graph(st.size());
        in = new In(stream);                        // 第二遍
        while (in.hasNextLine()) {                  // 构造图
            String[] a = in.readLine().split(sp);   // 把文件中每一行第一个顶点分别和剩下的顶点连接成边.
            int v = st.get(a[0]);
            for (int i = 1; i < a.length; i++)
                G.addEdge(v, st.get(a[i]));
        }
    }

    // key 是一个顶点吗
    public boolean contains(String key) {
        return st.contains(key);
    }

    // 返回顶点名对应的数组索引.
    public int index(String s) {
        return st.get(s);
    }

    // 返回索引v处的顶点名
    public String name(int v) {
        return keys[v];
    }

    // 隐藏的Graph对象
    public Graph G() {
        return G;
    }
    
    // test client.
    public static void main(String[] args) {
        String filename = args[0];         // 输入文件名
        String delim = args[1];            // 分隔符
        SymbolGraph sg = new SymbolGraph(filename, delim);
        Graph G = sg.G();

        while (StdIn.hasNextLine()) {
            String source = StdIn.readLine();
            if (sg.contains(source)) {
                for (int w : G.adj(sg.index(source)))
                    StdOut.println(" " + sg.name(w));
            }
            else {
                StdOut.println("input not contain '" + source + "'");
            }
        }
    }

}