#include <stdio.h>



#define CHECK_ZERO(divisor)				\
	if (divisor == 0)					\
		printf("*** Attempt to divide by zero on line %d "			\
			   "of file %s ***\n", __LINE__, __FILE__)

int main(void){
	// 使用预定义的宏： 
	printf("Wacky Windows (c) 2010 Wacky Software, Inc.\n");
	printf("Compiled on %s at %s\n", __DATE__, __TIME__);
	float i=30, j=0, k;
	CHECK_ZERO(j);
	k = i / j;
}