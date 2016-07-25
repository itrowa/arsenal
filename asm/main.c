int bar(int c, int d) {
	int e = e + d;
	return e;
}

int foo(int a, int b) {
	return bar(a, b);
}

int main(void) {
	foo(2, 3);
	return 0;
}