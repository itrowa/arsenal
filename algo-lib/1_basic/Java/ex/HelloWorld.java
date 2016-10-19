import edu.princeton.cs.algs4.*;

public class HelloWorld{
    public static int sumof_iter(int a, int b){
        // addup integers start from a to b.
        int sum = 0;
        while(a<=b) {
            sum += a;
            a++;
        }
        return sum;
    }
    
    public static int sumof_rec(int a, int b){
        // addup integers start from a to b, inc by 1.
        //recursive version.
        if (a > b) return 0;
        else return a + sumof_rec(a + 1, b);
        }

    public static void main(String[] args){
        // test case
        StdOut.printf("Hello World!\n");
        int sum_iter = sumof_iter(3, 5);
        int sum_recur = sumof_rec(3, 5);
        StdOut.printf("%d, %d", sum_iter, sum_recur);
    }
}
