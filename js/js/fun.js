
/*
----------------------------------------------------
function: 一种特殊的object.
----------------------------------------------------

*/ 

/* 
函数的声明
----------------------------------------------------
*/

// 使用function statement声明一个函数
function mysum(x, y) {return x + y;}

// 先声明一个匿名函数再绑定一个name. 注意这种方法缺点: 预读取时不会实际创建
// lambda函数在内存中. 必须运行时才能创建lambda函数.
// 创建lambda函数的statement: function(arg, [args]) {};
var mysum1 = function(x, y) {};

typeof(mysum); //function
mysum instanceof Function; // true


// 为mysum添加新的attr.
mysum.author = "Huang";
mysum.colour = "Yellow";
mysum.getcolor = function(){return this.colour};

/*
函数的特殊方法.
*/

// 特殊属性:
mysum.__proto__;
mysum.constructor;  // 指向Function 因为mysum的的构造函数就是Function()


// 函数作为对象的特殊属性: 1. 自动得到prototpye属性. 内容如下~
mysum.prototype; // 一个object.
mysum.prototype.__proto__;      // 指向Object()的prototype. 因为是Object作为构造函数创建了mysum.
mysum.prototype.constructor;    // 指向mysum函数的指针.

// call方法和apply方法
function test(x, y){
    mysum.apply(this, arguments);
    mysum.call(this. arguments);
}



// inside a function: 

/*

1. 类就是函数. 可以当作普通函数用
2. 函数被new statement执行时, 就称作构造函数.
*/
// function createObject(name){
//     var o = new Object();
//     o.name = "Huang";
//     o.age = "26";
// }



// function Account(name) {
//     this.name = name;
//     this.balance = 100;
//     this.deposit = function(s){
//         this.balance += s
//     };
//     this.withdraw = function(s){
//         this.balance -= s
//     }
// }


// tom = new Account("Tom");