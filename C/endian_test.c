// 测试大端小端

#include <stdio.h>
int main(void){
	int n = 1;
	// 小端的定义：如果地址位存储的是LSB，则称为小端.
	// 将变量n的地址取出并转换为char*型地址，然后打印这个地址的数据，如果是1，表示小端.
	printf(*(char *)&n ? "small endian!\n" : "big endian!\n");
}