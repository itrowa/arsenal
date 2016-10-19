/*

悟透javascript: 主要研究数据和过程的关系.


JavaScript中的数据很简洁的。简单数据只有 undefined, null, boolean, number和string这五种，而复杂数据只有一种，即object。
*/

var life = new Object();
// 从Object() 创建了一个instance? 不过不知道分不分这两个东西.

typeof(life);   //"object"

function foo() {
    1+1
};

typeof(foo); //"function"

//函数只是变量而已, 可以看到建立一个函数和建立一个变量语法是一样的.

var foo1 = function() {
    1+1
};
typeof(foo1); //"function"

//函数的名字会被覆盖! 就像变量会被覆盖一样. 因此js允许函数名重复, 后面的新内容会替代掉老内容.(函数名只是一个指针)

// 函数是对象.可以有各种属性.
// 动态为一个function类型的name添加属性
foo1.author = "Huang He";
foo1.date = "2015.10.17";
foo1.doCalc = function() {return 1+2; };

// 访问这个name的各种属性

// dot exp访问
foo1.author;
// subscription访问
foo1["author"];
// exec 函数body
foo1();
// exec 下标为doCalc的属性, 注意最后有(),表明这是call expression.
foo1["doCalc"]();
foo1["doCalc"];

//foo1的各个attr列出来,就像数组或者列表一样(实际上是个symbol table,或者字典). 因此可以遍历.
for(var s in foo1)
    print(s+" is a " + typeof(foo1[s]));


////////////////////////////////////////////
// about this

function whoAmI() {
    alert(this.name);
};

whoAmI(); // "" 全局对象的name是"",即window对象

var bill = {name: "Bill Gates"};
bill.whoAmI = whoAmI;
bill.whoAmI();    // Bill Gates

var steve = {name:"Steve Jobs"};
steve.whoAmI = whoAmI;
steve.whoAmI(); // Steve Jobs

whoAmI.call(bill);  // Bill Gates
whoAmI.call(steve); // Steve Jobs

bill.whoAmI.call(steve) // Steve Jobs
steve.whoAmI.call(bill) // Bill Gates

// 对象: 实质就是dict

var company =
{
    name: "Microsoft",
    product: "softwares",
    chairman: { name: "Bill Gates", 
                age: 53, 
                Married: true},
    employees: [{name: "Angel", age: 26, Married: false}, {name: "Hanson", age: 32, Marred: true}],
    readme: function() {document.write(this.name + " product " + this.product);}
};



// JSON字符串变成一个JavaScript对象时，只需要使用eval函数这个强大的数码转换引擎，就立即能得到一个JavaScript内存对象。
// var jstring = ...;
// eval(jstring);