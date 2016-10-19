// 最简单的定容栈实现.

// 使用： 
// % more tobe.txt
// java FixedCapacityStackOfStrings < tobe.txt

import edu.princeton.cs.algs4.*;

public class FixedCapacityStackOfStrings {
	private String[] a;
	private int N;            // stack size, not a size!

	// 构造函数
	public FixedCapacityStackOfStrings(int cap) {
		a = new String[cap];
	}

	public boolean isEmpty() { return N == 0; }
	public int size() { return N; }
	public void push (String item) {a[N++] = item;}			// 更新元素，N再++.
	public String pop() { return a[--N]; }					// N先--，再返回它.

	// 分析：栈顶下标位于N-1, 这在每次push或者pop之后都成立.

	// 测试用例
	public static void main(String[] args) {
		FixedCapacityStackOfStrings s;
		s = new FixedCapacityStackOfStrings(100);
		while(!StdIn.isEmpty()) {
			String item = StdIn.readString();

			// 根据读取到的内容判断是出栈还是入栈.
			if (!item.equals("-"))
				s.push(item);
			else if (!s.isEmpty()) StdOut.print(s.pop() + " ");
		}
		StdOut.println("(" + s.size() + " left on stack)");
	}
}