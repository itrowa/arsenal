/*
 工厂模式
 ---------------------------------------------------------------

 先把Object当成构造函数创建一个实例, 然后再往这个实例里面添加东西, 把这个过程封装在一个函数中.

 缺点: 

*/
function createPerson_1(name, age, job) {
    var o = new Object();
    o.name = name;
    o.job = job;
    o.sayName = function() {
        return (this.name)
    };
    return o
}

var person1 = createPerson_1("Nicholas", 29, "Software Engineer");
var person2 = createPerson_1("Greg", 27, "Doctor");

person1.sayName(); // "Nicholas"
person2.sayName(); // "Greg"


/*
构造函数模式
---------------------------------------------------------------

*/
function Person(name, age, job){
    this.name = name;
    this.age = age;
    this.job = job;
    this.sayName = function(){
        return this.name;
    };
}

var person1 = new Person("Nicholas", 29, "Software Engineer")
person1.age; // 29
person1.sayName // "Nicholas"

// 其它的使用Person函数的方法:
Person("Greg", 27, "Doctor");   // Person函数body中的this会被求值为window,实际上是给window对象设置了这些属性
window.age; // 27

var o = new Object();
Person.call(o, "Kristen", 25, "Nurse"); // Person函数的body中的this会被求值成为o. 所以是给对象o设置了这些属性..
o.age; //25

/*
特点: 创建一个函数 来当作"构造函数" , body中, 所有的属性都设置给this对象.

缺点:  不同的Person实例的sayName绑定到的是不同的Function的实例.

*/


// Prototype模式
function Person(name, age, job){
    Person.protype.name = name;
    Person.protype.age = age;
    Person.protype.job = job;
    Person.protype.sayName = function() {
        alert(this.name);
    }
}