// String类型的队列. 内部数据结构为链表. 链表每一个元素item是String.

// 使用:
// java LinkedQueueOfStrings.java

import edu.princeton.cs.algs4.*;

public class LinkedQueue<Item> {
	private Node first, last;		// 链表头尾的指针
	private int N;					// 队列长度.

	// 构造函数省略了. first, last均会被初始化为默认值null.

	// Node representation
	private class Node {
		Item item;
		Node next;
	}

	public boolean isEmpty() {
		return first == null;
	}

	public int size() { return N; }

	public void enqueue(Item item) {
		Node oldlast = last;
		last = new Node();
		last.item = item;
		last.next = null;

		// 1. 原来链表就是空的.
		// 2. 其它情况
		if (isEmpty()) first = last;
		else oldlast.next = last;
		N++;
	}

	public Item dequeue() {
		Item item = first.item;
		first = first.next;
		if (isEmpty()) last = null;
		N--;
		return item;
		// note: 需要小心对空的queue进行出列操作. -> 这会直接抛出异常 所以还好吧.
		//       小心对只有一个node的queue进行出列操作.
	}

	// 需要考虑两个特殊状态: 
	// 1是刚刚建立好链表的状态 这个时候first, last都是null
	// 2是只有一个node的状态 此时first last都指向这个唯一的node.

	// 测试用例: 读取整数
	public static void main(String[] args) {
		LinkedQueue<String> q = new LinkedQueue<String>();

		while(!StdIn.isEmpty()) {
			String item = StdIn.readString();
			// 根据读取到的内容判断是出列还是入列.
			if (!item.equals("-"))
				q.enqueue(item);
			else if (!q.isEmpty()) StdOut.print(q.dequeue() + " ");
		}
		StdOut.println("(" + q.size() + " left on queue)");
	}
}