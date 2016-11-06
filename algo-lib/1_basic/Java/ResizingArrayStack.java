// 使用参数化类型实现的stack. 内部数据结构为动态数组.

// java ResizingArrayStack < tobe.txt

import edu.princeton.cs.algs4.*;

public class ResizingArrayStack<Item> {
	private Item a[];
	private int N;

	// 构造函数
	public ResizingArrayStack() {
		a = (Item[]) new Object[1];
		// 实例变量N 将被自动初始化为0
	}

	public boolean isEmpty() { return N == 0;}
	public int size() { return N; }

	public void push(Item item) { 
		if ( N > a.length)	resize(2 * a.length);
		a[N++] = item;
	}

	public Item pop() {
		Item item = a[--N] ;
		a[N] = null;

		if (N < a.length / 4) 
			resize(a.length / 2);
		return item;
	}

	public void resize(int capacity) {
		Item[] copy = (Item[])  new Object[capacity];
		for (int i = 0; i < N; i++)
			copy[i] = a[i];
		// note：新数组的大小是capacity， 它必须大于要被复制的栈的大小。
		a = copy;
	}

	public static void main(String[] args) {
		ResizingArrayStack<String> s = new ResizingArrayStack<String>(); // @?
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