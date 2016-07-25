struct unit {
    char c;
    int num;
}
struct unit u;

// 定义此结构体类型的指针
struct unit *p = &u;

// 间接寻址运算
(*p).c
(*p).num