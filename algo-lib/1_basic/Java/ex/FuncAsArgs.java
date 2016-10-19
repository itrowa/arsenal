public class FuncAsArgs{
    public static int apply( term, int a){
        // apply a func term to arg a.
        return term(a);
    }
    
    public static int inc1(int num){
        // return num + 1
        return num + 1;
        }

    public static void main(String[] args){
        int result = apply(inc1, 3);
        StdOut.printf("%d", result);
    }
}