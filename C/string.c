// 字符串字面量
char *p;
p = "abc";				// 使p指向字符串的第一个字符

char ch;
ch = "abc"[1];			// 得到字符b

// 将0~15的数字转换为等价的16进制形式.
char digit_to_hex_char(int digit) {
	return "0123456789ABCDEF"[digit];
}

// 编译器自动合并多条字符串
printf("When you come to a fork in the road, take it."
	"--Yogi Berra.");


/// 字符串变量

// 字符串可存储的字符数量是80，但实际上用数组存储字符串时，一般都要多分配一个单元.
#define STR_LEN 80

char str[STR_LEN+1];

// 以下两个声明&初始语句效果都是一样的:
char date1[8] = "June 14";
char date2[8] = {'J', 'u', 'n', 'e', ' ', '1', '4', '\0'};


// note: 如果声明字符数组时同时初始化,编译器可自动计算数组长度


// 打印和输入
char str[] = "Are we having fun yet?";
printf("%3.6s\n", str);
puts(str); // 自动换行

// scanf函数

// gets
char sentence[SENT_LEN+1];

printf("Enter a sentence: \n");
gets(sentence);