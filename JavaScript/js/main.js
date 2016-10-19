var myHeading = document.querySelector('h1');
myHeading.innerHTML = 'Hello world!';


"Hello".length; //5
"Hello".charAt(0)
"hello".charAt(0); // "h"
"hello, world".replace("hello", "goodbye"); // "goodbye, world"
"hello".toUpperCase(); // "HELLO"




/*
    Boolean:
 Any value can be converted to a boolean according to the following rules:

false, 0, empty strings (""), NaN, null, and undefined all become false.
All other values become true.
大多数情况下转换是自动进行的.
*/

// convert other type to boolean type:
Boolean(""); //false
Boolean(234); //true

/*
variables

var keyword.
*/

var a;  // undefined
var name = "simon";

/*
operators:
+, -, +=, -=, ++, --, ...
*/

/* 
comparasions

注意js的类型强制转换(coercion)
*/

123 = "123"; //true
1 == True; //true


/*
object: 一种引用类型
*/

var obj = new Object();
var obj1 = {}; // literal syntax

var obj = {
    name: "Carrot",
    "for": "Max",
    details: {
        color: "orange",
        size: 12
    }
}

// 用literial syntax创建object类型的引用类型对象
var person = {
    name: "Nicholas",
    age: 29
}

obj.details.color; // orange
obj["details"]["size"]; //12

// create an object `prototype`
function Person(name, age) {
    this.name = name;
    this.age = age;
}

//////////////////////////////////////////////////////
// create an instance of the prototype
var You = new Person("You", 24);

// access object properties: @???
obj.name="simon";
var name = obj.name;

// access object properties: another way
obj["name"]="simon";
var name = obj["name"];


/* 
array
*/
var a = new Array();
a[0] = "dog";
a[1] = "cat";
a[2] = "hen";
a.length; // 3

// using array literal:
var a = ["dog", "cat", "hen"];
a[100] = "fox";
a.length;   // 101

// 看看一些数组越界的情况:
typeof a[90];   // undefined

// iteration:
for (var i=0; i < a.length; i++) {
    // do sth..
}

// iteration, better way:
for (var i=0, len=a.length; i<len; i++) {
    // do sth..
}

// iteration, better better way:
for (var i = 0, item; item = a[i++];) {
    // do sth..
}

// iteration since EMACS5:
["dog", "cat", "hen"].forEach(function(currentValue, index, array) {
    // do sth with currentValue or array[index]
});


/*
a.push(item);
a.join()
a.pop()
..
