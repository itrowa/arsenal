public class TestVisualAccumulator
// VisualAccumulator的测试用例.
{
    public static void main(String[] args)
    {
        int T = Integer.parseInt(args[0]); // 把main func的参数的第一个元素取出来转为int
        VisualAccumulator a = new VisualAccumulator(T, 1.0);
        for (int t = 0; t<T; t++)
            a.addDataValue(StdRandom.random());
        StdOut.println(a);
    }
}