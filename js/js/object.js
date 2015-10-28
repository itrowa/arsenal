/*
----------------------------------------------------
object: 一种引用类型
----------------------------------------------------
js的对象其实数据结构是一个dict, 一系列的key-value pair.

*/
var person = {
    name: "Nicholas",
    age: 29,
    details: {
        address: "No.5 of Nanshan Street",
        post_code: 518000
    },
    getAge: function() {
        return this.age;
    }
}

// access value: dot exp

// 注意会把value按照原样输出!!
person.name; //"Nicholas"
person.getAge; // 打印对应的value
person.getAge(); // call expression.

// 动态地进行修改:
person.name="Huang He";
person.date="1989.05.12";

// subscription expression:
person["name"];
person["details"]["address"];
person["getAge"]();

// 可以遍历:
for(var s in person)
    alert(s + " is a " + typeof(person[s]));

// person是Object的实例吗? instanceof statement.
person instanceof Object;    //true

// person的构造函数是?.
person.constructor; //Object()

// person属于什么类的实例?
typeof(person);


// 可以使用new statement, 再动态更新这个obj的内容
// 注意, Object是作为构造函数使用的.
var obj = new Object();
obj.name = "Huang";

var aa = new person(); // 出错! 因为person不能作为构造函数使用. 本质就不是函数.



// 问题:  Function是 Object. 并且, Object也是Function.
Function instanceof Object
// true
Object instanceof Function
// true