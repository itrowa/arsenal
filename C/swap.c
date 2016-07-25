#include <stdio.h>

int *swap(int *px, int *py)
// swap 2 int num.
{
	int temp;
	temp = *px;
	*px = *py;
	*py = temp;
	return px; 
}

int main(void)
{
	int i = 10, j = 20;
	int *p = swap(&i, &j);
	printf("now i=%d j=%d *p=%d\n", i, j, *p);
}