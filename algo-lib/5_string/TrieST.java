public class TrieST {
    private static int R = 256;
    private Node root;

    // 表示一个节点的数据结构.
    private static class Node {
        private int val;
        private Node[] next = new Node[R];

    }

    // 空的构造函数
    public TrieST(){}

    public void put(String key, int val) {
        root = put(root, key, val, 0);
    }

    // 将key的第d位放入单词树.
    private Node put(Node x, String key, int val, int d) {

        if (x == null) {
            x = new Node();            // 在此节点的next[]的对应位置插入指向新的Node的链接.
            if (d == key.length()) {
                x.val = val;
                return x;
            }
            char c = key.charAt(d);         // 获得key的第d个下标位置的字符.
            x.next[c] = put(x.next[c], key, val, d+1);
            return x;
        }

        else {
            // key的所有位都已经插入完毕, 结束插入操作.
            if (d == key.length()) {
                x.val = val;
                return x;
            }
            // key还有剩余的部分没插入, 因此递归调用Put函数.
            else {
                char c = key.charAt(d);         // 获得key的第d个下标位置的字符.
                x.next[c] = put(x.next[c], key, val, d+1);
                return x;
                
            }
        }
    }

    public int get(String key) {
        Node n = get(root, key, 0);
        return n.val;
    }

    private Node get(Node x, String key, int d) {
        if (x == null)
            return null;
        else {
            // 查找结束的情况
            if (d == key.length()) {
                return x; // 小心返回空
            }
            char c = key.charAt(d);
            return get (x.next[c], key, d+1);
        }
    }

    // @todo: 参考即时实现.
    public int size() {
        //
    }
 
    // note: 三层嵌套: 
    // 返回st中所有的key, 就是调用以""为字符串的所有Key. 然后又调用..

    // 返回st中所有的key.
    public Iterable<String> keys() {
        return keysWithPrefix("");
    }

    // 返回st中以pre为Key的所有key.
    public Iterable<String> keysWithPrefix(String pre) {
        Queue<String> q = new Queue<String>();
        collect(null, pre, q);
        return q;
    }

    // 被keysWithPrefix()函数使用的辅助函数.
    // 用于求节点x开始的有效key.. 结果会放入q中.
    private void collect(Node x, String pre, Queue<String> q) {
        if (x == null)
            return;
        else {
            // 如果此处节点x有val值, 说明刚才查找到了一个有效的key. 存储之.
            if (x.val != null) q.enqueue(pre); 

            // 遍历x节点的next[]所有指针寻找可能存在的key.
            for (char c = 0; c < R; c++)
                collect(x.nextc[c], pre + c, q);
        }
    }

    // 满足模式pat的所有key.
    // .能匹配任意的字符. 例如s.e可以匹配she.
    public Iterable<String> keysThatMatch(String pat) {
        Queue<String> q = new Queue<String>();
        collect(root, "", pat, q);
        return q;
    }

    private void collect(Node x, String pre, String pat, Queue<String> q) {
        int d = pre.length();
        if (x == null) return;
        if (d == pat.length() && x.val != null) q.enqueue(pre);
        if (d == pat.length()) return;

        char next = pat.charAt(d);
        for (char c = 0; c < R; c++)
            if(next == '.' || next == c)
                collect(x.next[c], pre + c, pat, q);
    }

    // 找到st的key中, 含有字符串s前缀的最长的key.
    public String longestPrefixOf(String s) {
        int length = search(root, s, 0, 0);
        return s.substring(0, length);
    }

    // 得到含有字符串s前缀的最长的key的长度.
    private int search(Node x, String s, int d, int length) {
        if (x == null) 
            return length;
        else {
            if (x.val != null) 
                length = d;
            if (d == s.length())
                return length;
            char c = s.charAt(d);
            return search(x.next[c], s, d+1, length);
        }
    }

    private static void testPut() {
        TrieST st = new TrieST();
        st.put("she", 1);
        //StdOut.println(st.root['A']);

    }

    public static void main(String[] args) {
        TrieST st = new TrieST();

        String input_str = "she sells sea shells by the sea shore";
        String[] str = input_str.split(" ");

        int i = 0;
        for (String s : str) {
            st.put(s, i);
            // StdOut.println(s + " " + i);
            i++;
        }

        StdOut.println(st.get("she"));
        StdOut.println(st.get("shells"));
    }
}