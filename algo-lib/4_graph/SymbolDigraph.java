// 符号有向图的实现. 和符号无向图完全一样.
public class SymbolDigraph {
    private ST<String, Integer> st;                 // 一个符号表, 存储vertex name -> vertex index
    private String[] keys;                          // 一个数组, 存储vertex index -> vertex name
    private Digraph G;

    public SymbolDigraph(String stream, String sp) {
        st = new ST<String, Integer>();

        // 建立st符号表.
        In in = new In(stream);
        while(in.hasNextLine()) {
            String[] a = in.readLine().split(sp);

            for (int i = 0; i < a.length; i++) {
                if (!st.contains(a[i]))
                    st.put(a[i], st.size());
            }
        }

        // 建立keys数组
        keys = new String[st.size()];
        for (String name : st.keys()) {
            keys[st.get(name)] = name;
        }

        G = new Digraph(st.size());
        in = new In(stream);
        while (in.hasNextLine()) {
            String[] a = in.readLine().split(sp);
            for (int i = 1; i < a.length; i++) {
                int v = st.get(a[0]);
                G.addEdge(v, st.get(a[i]));
            }
        }
    }

    public boolean contains(String key) {
        return st.contains(key);
    }

    public int index(String v) {
        return st.get(v);
    }

    public String name(int v) {
        return keys[v];
    }

    public Digraph G() {
        return G;
    }

}