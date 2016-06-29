#include <stdio.h>

// 验证表达式getchar() != EOF 的值是0还是1
// 答案是1
// 因为只要不是EOF，那么不等式成立（为真），在C中真值用1表示
main()
{
    printf("the value of that exp. is %3d", (getchar() != EOF));    //!=的优先级更高
}
