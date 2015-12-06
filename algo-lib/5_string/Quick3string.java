public class Quick3string {
    private static int charAt(String s, int d) {
        if (d < s.length())
            return s.charAt(d);
        else return -1;
    }

    public static void sort(String[] a) {
        sort(a, 0, a.length - 1, 0);
    }

    private static void sort(String[] a, int lo, int hi, int d) {
        if (hi <= lo)
            return;
        int lt = lo;
        int gt = hi;
        int v = charAt(a[lo], d);           // 以a[lo]作为切分的主元.
        int i = lo + 1;
        while(i <= gt) {
            int t = charAt(a[i], d);
            if (t < v)
                exch(a, lt++, i++);
            else if (t > v)
                exch(a, i, gt--);
            else i++;
        }

        sort(a, lo, lt-1, d);

        // 如果v<0 代表字符串已经到了末尾 不用再sort了
        if (v >= 0)
            sort(a, lt, gt, d+1);
        sort(a, gt+1, hi, d);
    }

    private static void exch(Comparable[] a, int i, int j) {
        Comparable t = a[i];
        a[i] = a[j];
        a[j] = t;
    }
}