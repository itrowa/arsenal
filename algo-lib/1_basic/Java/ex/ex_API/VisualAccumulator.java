public class VisualAccumulator
// 可视化累加器, 来自algo4 1.2.4.3节
{
    private double total;
    private int N;
    public VisualAccumulator(int trials, double max)
    {
        StdDraw.setXscale(0, trials);
        StdDraw.setYscale(0, max);
        StdDraw.setPenRadius(.005);
    }
    public void addDataValue(double val)
    //添加一个新的数据值
    {
        N++;
        total += val;
        StdDraw.setPenColor(StdDraw.DARK_GRAY);
        StdDraw.point(N, val);
        StdDraw.setPenColor(StdDraw.RED);
        StdDraw.point(N, total / N);
    }
    public double mean()
    // 所有数据的平均值
    { return total / N;}
    public String toString()
    { return "Mean (" + N + " values): " + String.format("%7.5f", mean());}
}