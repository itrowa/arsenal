#include <stdio.h>

int mian(void)
{
	int a = 10, b;

	// 内联汇编代码，其实是是执行一个特殊的函数__asm__().
	__asm__("movl %1, %%eax\n\t"
			"movl %%eax, %0\n\t"
			:"=r"(b)				// output
			:"r"(a)					// input
			:"%eax"					// clobbered register
		);
}