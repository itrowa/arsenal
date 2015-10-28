# 换零钱问题, 整数分割问题

import linked_list

def partitions(n, m):
    """
    用最大为m的数去分割n，以Linked list的形式返回每一种分割方案。
    """
    if n ==0:
        return link(empty, empty)
    elif n < 0 or m == 0:
        return empty
    else:
        using_m = partitions(n-m, m)
        with_m = apply_to_all_link(lambda s: link(m, s), using_m)
        without_m = partitions(n, m-1)
        return extend_link(with_m, without_m)

def print_partitions(n, m):
    """
    把n用最大为m的部分分割的结果输出给人类看。

    >>> print_partitions(6, 4)
    4 + 2
    4 + 1 + 1
    3 + 3
    3 + 2 + 1
    3 + 1 + 1 + 1
    2 + 2 + 2
    2 + 2 + 1 + 1
    2 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 1 + 1
    """
    lists = partitions(n, m) # 分割得到linked_list.
    strings = apply_to_all_link(lambda s: join_link(s, "+"), lists)
    print(join_link(strings, "\n"))
