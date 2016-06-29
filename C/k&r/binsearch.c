/*
 *
 * binsearch函数，在v[0]<=v[1]<=v[2]<=...<=v[n-1]中查找x
 * 注意v是已经排序了的数组，而且是升序排列的
 *
 * 算法：折半查找。将输入值x和数组v的中间元素进行比较。如果x小于中间元素的值则在数组的前半部分查找，否则在后半部分查找。 下一次也都是和所选部分的中间元素进行比较。这个过程一直持续，直到找到特定的值为止。
 */

int binsearch(int x, int v[], int n){
    int low, high, mid;

    low = 0;
    high = n - 1;
    while(low <= high) {
        mid = (low + high) / 2;
        if (x < v[mid])
            high = mid - 1;
        else if(x > v[mid])
            low = mid + 1;
        else
            return mid;

    }
    return -1;
}
/*
 * 改进版的函数，while循环语句内只执行一次测试。
 */
int binsearch(int x, int v[], int n){
    int low, high, mid;

    low = 0;
    high = n - 1;
    while(low <= high) {
        mid = (low + high) / 2;
        if (x < v[mid])
            high = mid - 1;
        else if(x > v[mid])
            low = mid + 1;
        else
            return mid;

    }
    return -1;
}



