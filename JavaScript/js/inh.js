/*
 * 如何让Cat继承Animal的属性.
 */

/* 1. 直接调用Animal函数，设置那几个想要的属性
 *  经典继承; 借用构造函数.
 */
function Animal(）{
    this.species = "Animal";
}

function Cat(name,color){
    Animal.apply(this, arguments);
    this.name = name;
    this.color = color;
} 

var cat1 = new Cat("Huang","Yellow");

cat1.species; // animal
// 有时候我们希望object只是用指针去继承其他对象的属性，这时
// 这种方法不太好用.

/* 原型链
 * 通过把构造函数的prototype重新绑定到想要继承的构造函数的实例上.
 * 这样,Cat.prototype实际上指向了Animal的一个实例，因此获得了Animal的
 * 所有属性, 还通过属性搜索机制获得Animal.prototype中的属性.
 */

function Animal(）{
    this.species = "Animal";
}

function Cat(name,color){
    this.name = name;
    this.color = color;
}
Cat.prototype = new Animal(); 

var cat1 = new Cat("Huang","Yellow");
//q
cat1.constructor // 是谁?
Cat.constructor //是谁?
Animal.constructor //是谁?
 

// still have problem.
/* 2. 尝试：希望Cat只是引用Animal的属性。怎么做？ 
 *
 * 改写Cat的Prototype 让其指向Animal的实例，属性搜索机制就能访问
 * Animal中的设置的属性了。
 * 特点：Cat.prototype和Animal.prototype实际上是同一个对象. 独立性问题！?
 */

function Animal(）{
    this.species = "Animal";
}

function Cat(name,color){
    this.name = name;
    this.color = color;
}

// 直接更改prototype的绑定. 新指向的实例就是一个设置了species属性的Animal对象.
Cat.prototype = new Animal(); 

// 如果没有这一步, 它指向的是Animal. 这违背了Cat的constructor应该
// 是Cat自己的事实。所以必须纠正
Cat.prototype.constructor = Cat; 
// 但还是有问题: 现在Animal.prototype.constructor也变成了Cat!

var cat1 = new Cat("Huang","Yellow");

/* 3. 对2的改进。
 * 因为2有问题，所以现在这个待定不看.
 */


/* 实际： 同时使用继承链和构造函数.
 * 构造函数继承那些想要被各个实例独立使用的属性；
 * 用原型来继承那些想要被各个实例共享使用的属性.
 */
