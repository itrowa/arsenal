// 栈, 使用链表来实现

import edu.princeton.cs.algs4.*;
import java.util.Iterator;

public class LinkedStack<Item> implements Iterable<Item> {
	private Node first = null;			// dummy node?
	private int N;						// stack size

	// Node representation
	private class Node {
		Item item;
		Node next;
	}


	// 省略构造函数..

	public boolean isEmpty() { return first == null; }

	public int size() { return N; }

	public void push(Item item) {
		Node oldfirst = first;
		first = new Node();
		first.item = item;
		first.next = oldfirst;
		N++;
	}

	public Item pop() {
		Item item = first.item;
		first = first.next;
		N--;
		return item;
	}

	// 返回Iterator的方法
	public Iterator<Item> iterator() {
		return new ListIterator();
	}

	// 实现Iterator的class
	private class ListIterator implements Iterator<Item> {
		private Node current = first;

		public boolean hasNext() {
			return current != null;
		}

		public Item next() {
			Item item = current.item;
			current = current.next;
			return item;
		}

		public void remove() {};	// 不支持remove功能
	}

	// 测试用例
	public static void main(String[] args) {
		LinkedStack<String> s;
		s = new LinkedStack<String>();
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