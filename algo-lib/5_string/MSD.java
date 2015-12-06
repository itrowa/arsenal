public class MSD {
    private static int R = 256;                             // 基数
    private static final int M = 15;                        // 小数组的切换阈值
    private static String[] aux;                            // 数据分类的辅助数组

    // 字符串在索引d处的字符的编号...例如, ABCDE第0个字符的编号是65
    private static int charAt(String s, int d) {
        if (d < s.length())
            return s.charAt(d);
        else 
            return -1;
        // 当索引d超过了字符串的末尾时, 直接返回-1
    }

    // 对字符串数组a排序.
    public static void sort(String[] a) {
        int N = a.length;
        aux = new String[N];
        sort(a, 0, N-1, 0);
    }

    // 以第d个字符为key将a[lo]到a[hi]排序
    // d是从0开始, 0代表最高位
    private static void sort(String[] a, int lo, int hi, ind d) {
        // 如果是小数组, 就使用插入排序.
        if (hi <= lo + M) {
            Insertion.sort(a, lo, hi, d);
            return;
        }

        // 计算频率
        int[] count = new int[R+2];                        
        for (int i = lo; i <= hi; i++)
            count[charAt(a[i], d) + 2]++;

        // 把频率转换为索引
        for (int r = 0; r < R+1; r++)
            count[r+1] += count[r];

        // 数据分类
        for (int i = lo; i <= hi; i++)
            aux[count[charAt(a[i], d) + 1]++] = a[i];

        // 回写
        for (int i = lo; i <= hi; i++)
            a[i] = aux[i - lo];

        // 为每个字符为key进行递归排序
        for (int r = 0; r < R; r++)
            sort(a, lo + count[r], lo + count[r+1] -1, d+1);
    }

}