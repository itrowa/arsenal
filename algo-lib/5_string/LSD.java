public class LSD {
    // 通过前W个字符串将a[]排序
    public static void sort(String[] a, int w) {
        int N = a.length;
        int R = 256;                                        // 基数
        String[] aux = new String[N];

        for (int d = W - 1; d >= 0; d--) {
            // 根据第d个字符用键索引计数法排序. d: w-1, w-2, ... , 2, 1, 0

            // 计算出现频率
            int[] count = new int[R+1];                 
            for (int i = 0; i < N; i++)
                count[a[i].charAt(d) + 1]++;

            // 将频率转换为索引
            for (int r = 0; r < R; r++)
                count[r+1] += count[r];

            // 将元素进行分类
            for (int i = 0; i < N; i++)
                aux[count[a[i].charAt(d)]++] = a[i];

            // 回写
            for (int i = 0; i < N; i++)
                a[i] = aux[i];
        }
    }
}