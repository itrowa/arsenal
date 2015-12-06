public class Quick {
    public static void sort(Comparable[] a) {
        // 先把要排序的项目打乱
        StdRandom.shuffle(a);
        sort(a, 0, length - 1);
    }

    private static void sort(Comparable[] a, int lo, int hi) {
        if (hi <= lo)
            return;
        int j = partition(a, lo, hi);               // 进行切分, 并取得切分主元的下标
        sort(a, lo, j-1);                           // 排序左半部分
        sort(a, j+1, hi);                           // 排序右半部分
    }

    // 将数组切分为a[lo....i-1], a[i], a[i+1....hi], 且左半部分元素都小于a[i], 又半部分元素都大于a[i]
    private static int partition(Comparable[] a, int lo, int hi) {
        int i = lo, j = hi + 1;
        Comparable v = a[lo];

        while(true) {
            while (less(a[++i], v))
                if (i == hi)
                    break;
            while (less(v, a[--j]))
                if (j == lo)
                    break;
            if (i >= j)                         // i 和 j 相遇时主循环退出.
                break;
            exch(a, i, j);                      // 把v=a[j]放入正确的位置.
            return j;
        }
    }
}