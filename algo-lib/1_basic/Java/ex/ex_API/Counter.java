public class Counter
// algos4 2.2节介绍的Counter数据类型的完整实现。
{
    // 实例变量：存储类型的值, 用private修饰符保证对外不可见。
    private final String name;
    private int count;

    // Constructor:
    public Counter(String id)
    { name = id;}

    // instance methods, 类似于java中的static method，对应python中的methods

    // 将计数器的值加1 
    public void increment()
    { count++; }

    // 返回计数器的值
    public int tally()
    { return count; }

    // 对象的字符串表示
    // 因为Counter继承自Object类，toString()是Object类的方法，需要overload.
    public String toString()
    { return count + " " + name; }

    // test case, written in main func.
    public static void main(String[] args)
    {
        Counter heads = new Counter("heads");
        Counter tails = new Counter("tails");

        heads.increment();
        heads.increment();
        tails.increment();

        StdOut.println(heads + " " + tails); // 自动调用heads的toString()方法
        StdOut.println(heads.tally() + tails.tally() );
    }

}