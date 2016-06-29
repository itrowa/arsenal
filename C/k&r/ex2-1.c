#include <stdio.h>
#include <limits.h>

main(){
    printf("signed char is from %d to %d\n",SCHAR_MIN, SCHAR_MAX);
// 其余几个也可以用类似的方法打印出来。
    char cnt;
    int max;
    int min;
    max = min = cnt = 0;
    while(1){
       cnt++;
      if (cnt > max)
          max = cnt;
      if (cnt < min)
          min = cnt;
      if (cnt == 0)
          break;
    }
    printf("%d %d",max, min);
    //其他几个照样算就行了
}
