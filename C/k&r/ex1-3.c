#include <stdio.h>
/*
fahr to celsius conversation table.

*/
main()
{
    float fahr, celsius;
    int lower, upper, step;
    lower = 0;
    upper = 300;
    step = 20;

    fahr = lower;
    printf("CONVERSATION\n");
    while(fahr <= upper)
    {
    celsius = (fahr - 32.0)*(5.0/9.0);
    printf("%3.0f %6.1f\n", fahr, celsius);
    fahr = fahr + step;
    }
}
