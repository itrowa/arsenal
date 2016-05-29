/*
    js的条件控制流用于模拟数字电路? 太装逼了
*/

var age = 20;
if (age >= 18) { // 如果age >= 18为true，则执行if语句块
    alert('adult');
} else { // 否则执行else语句块
    alert('teenager');
}

/*
    js的块级用花括号表达.{}. 花括号也可以省略, 这种情况下, 块级只算上第一行. 这个设计
    容易给不爱写花括号的人带来麻烦. 因此建议都写上花括号.

    条件控制流的一般形式是:
    if () {}
    else if () {}
    else {}

    else if部分可省略.

    if控制流具有短路特性;
    if控制流是多选1.
*/


var x = 0;
var i;
for (i=1; i<=10000; i++) {
    x = x + i;
}
x; // 50005000

// for(... in ...), 用于将key遍历出来(遍历的是对象的属性名称!).(而不是value)
var o = {
    name: 'Jack',
    age: 20,
    city: 'Beijing'
};
for (var key in o) {
    alert(key); // 'name', 'age', 'city'
}
// 类似python的for in语句, 直接迭代可迭代的对象中的元素.

// while; do.. while
var x = 0;
var n = 99;
while (n > 0) {
    x = x + n;
    n = n - 2;
}
x; // 2500