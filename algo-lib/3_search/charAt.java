import edu.princeton.cs.algs4.*;

public class charAt {
	public static void main(String[] args) {
		String s = "hello";
		for (int i = 0; i < s.length(); i++) {
			StdOut.print(s.charAt(i));
			StdOut.print((int)s.charAt(i));
		}
	}
}