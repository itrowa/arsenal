/* 把事物封装成一个个对象, 内部有属性和方法, 对象和对象之间相互独立. 在javascript中如何实现?

/* 第一次尝试:原始模式
 */

function Cat(name, color){
    return {
        name: name,
        color: color}
}

var cat1 = new Cat("Huang", "Yellow");
var cat2 = new Cat ("Cheng", "White");

/* 代码达到了一定的复用性，解决了对象的独立性, 但是?
*/

/* 利用构造函数创建object
 */
function Cat(name,color){
    this.name = name;
    this.color = color;
    this.eat = function(){ return "Eat@_@~";}
} 

var cat1 = new Cat("Huang", "Yellow");
var cat2 = new Cat ("Cheng", "White");

cat1.constructor; // Cat
cat2.constructor; // Cat

cat instanceof Cat; //true
cat instanceof Cat; //true

/* 缺点：每个变量之间太独立。每个方法和每个属性都要在每个实例上创建一遍，浪费资源。对于一些属性相同的项目，其实可以做成引用的
 *
 */


/* prototype模式
 */



function Cat(name,color){
    this.name = name;
    this.color = color;
}

Cat.prototype.type = "maoke";
Cat.prototype.eat = function(){alert("eat!!")}; 

var cat1 = new Cat("Huang", "Yellow");
var cat2 = new Cat ("Cheng", "White");

/* cat1和cat2的eat方法都是放在Cat.prototype中。为他们所共享。
 */


//prototype的isPrototypeof() method
Cat.prototype.isPrototypeOf(cat1); // true
Cat.prototype.isPrototypeOf(cat2); // true

// in 按照属性页查找规则来查找name。
name in cat1 //true


//实例的hasOwnProperty() method
cat1.hasOwnProperty("name"); // true
cat1.hasOwnProperty("type"); // false


/* 问题:
 * 因为原型实际上是一个指针，再加上js的属性搜索机制,修改原型中的值
 * 后，所有实例会同步收到影响。
 */

/* 组合使用构造函数和原型：
 * 构造函数用于存放实例之间相互独立使用的属性；(类似python的class attr)
 * 原型用于存放要被实例之间共享使用的属性.(类似python的instance attr)
 */


