// stack的动态数组实现。每一个数组元素都是String类型.

// java ResizingArrayStackOfStrings.java < tobe.txt

import edu.princeton.cs.algs4.*;

public class ResizingArrayStackOfStrings {
	private String s[];
	private int N;				// stack length, not s[] length!

	public ResizingArrayStackOfStrings() {
		s = new String[1];	//  初始化时, 动态数组的大小只有1
		N = 0; // 其实可以省略.
	}

	public boolean isEmpty() { return N == 0;}
	public int size() { return N; }

	public void push(String item) {
		StdOut.println("Stack: " + s.length);
		if (N == s.length) 
			resize(2 * s.length);
		s[N++] = item;
		// note: 在push之前先检查数组是否满了.
	}

	public String pop() {
		String item = s[--N];
		s[N] = null;		// avoid loitering
		if (N < s.length / 4)
			resize(s.length / 2);
		// note: pop之后再检查是否需要resize.
		return item;
	}

	private void resize(int capacity) {
		String[] copy = new String[capacity];
		for (int i = 0; i < N; i++)
			copy[i] = s[i];
		s = copy;
		// note：新数组的大小是capacity， 它必须大于要被复制的栈的大小。
	}

	// 循环不变式: 数组总是在25% ~ 100% full 间.
	// 				栈顶下标是a[N-1], 但数组为空时除外!

	public static void main(String[] args) {
		ResizingArrayStackOfStrings s = new ResizingArrayStackOfStrings(); // @?
		while (!StdIn.isEmpty()) {
			String item = StdIn.readString();

			// 根据读取到的内容判断是出栈还是入栈.
			if (!item.equals("-"))
				s.push(item);
			else if (!s.isEmpty()) StdOut.print(s.pop() + " ");
		}
		StdOut.println("(" + s.size() + " left on stack)");
	}
}