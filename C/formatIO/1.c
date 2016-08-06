#include <stdio.h>

int main(void) {
	int i = 40;
	float x = 839.21f;

	// 测试d的各种控制输出.
	printf("|%d|%5d|%-5d|%5.3d|\n", i, i, i, i);

	// 测试f的各种控制输出.
	printf("|%10.3f|%10.3e|%-10g|\n", x, x, x);

	return 0;
}