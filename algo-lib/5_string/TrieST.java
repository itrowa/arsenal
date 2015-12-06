public class TrieST<Value> {
    private static int R = 256;                                 // 基数
    private Node root;                                          // 单词查找树的根节点

    private static class Node {
        private Object val;
        private Node[] next = new Node[R];
    }

    public value get(String key) {
        Node x = get(root, key, 0);
        if (x == null) return null;
        return (Value) x.val;                                   // 显式类型转换, 从Object转换为Value
    }

    private Node get(Node x, String key, int d) {
        // 返回以x作为根节点的子单词查找树种与key相关的值
        if (x == null)
            return null;
        if (d == key.length())
            return x;
        char c = key.charAt(d);
        return get(x.next[c], key, d+1);
    }

    public void put(String key, Value val) {
        root = put(root, key, val, 0);
    }

    private Node put(Node x, String key, Value val, int d) {
        if (x == null)
            x = new Node();
        if (d == key.length()) {
            x.val = val;
            return x;
        }
        char c = key.charAt(d);
        x.next[c] = put(x.next[c], key, val, d+1);
        return x;
    }

    //@todo: size()

    //@todo: 理解这个查找所有key的算法? 
    public Iterable<String> keys() {
        return keysWithPrefix("");
    }

    public Iterable<String> keysWithPrefix(String pre) {
        Queue<String> q = new Queue<String>();
        collect(get(root, pre, 0), pre, q);
        return q;
    }

    private void collect(Node x, String pre, Queue<String q>) {
        if (x == null) return;
        if (x.val != null) q.enqueue(pre);
        for (char c = 0; c < R; c++)
            collect(x.next[c], pre + c, q);
    }
}