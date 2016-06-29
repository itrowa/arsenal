#include <stdio.h>

// 打印EOF的值
// 因为EOF实际是个宏替换，所以会被替换为一个整数。所以可以通过%3d的方式打印出来。
main()
{
    printf("the value of EOF is %3d", EOF);
}
