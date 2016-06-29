#include <stdio.h>

main()
{
    int nspaces, ntabs, nl, c;
    nspaces = 0;
    ntabs = 0;
    nl = 0;

    while((c = getchar()) != EOF)
    {
        if (c == '\n')
            ++nl;
        if (c == ' ')
            ++nspaces;
        if (c == '\t')
            ++ntabs;
    }
     printf("the number of line is %3d, \nthe number of spaces is %3d, \nthe number of tab is %3d", nl, nspaces, ntabs);
}
