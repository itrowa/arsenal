function myadd(x, y) {
    var total = x + y;
    return total;
}
// functions have access to an additional variable inside their 
// body called arguments, which is an array-like object holding 
// all of the values passed to the function.

// take multiple operands
function myadd_1() {
    var sum = 0;
    for (var i = 0, j = arguments.length; i<j; i++) {
        sum += arguments[i];
    }
    return sum;
}


// call()

window.color = "red";
var o = {color: "blue"};

function sayColor() {
  return this.color;
}

sayColor(); //red 进入函数body求值this, this就是window
sayColor.call(this);  //red,   把函数body的this设置为此处的this, 即windows
sayColor.call(window);  //red,  把函数body的this设置为window
sayColor.call(o);      //blue   把函数body的this设置为o.


// 返回Json格式,其中还包括了函数!!函数!!
// return {...};
function makePerson(first, last) {
    return {
        first: first,
        last: last,
        fullName: function() {
            return this.first + " " + this.last;
        },
        fullNameReversed: function() {
            return this.last + ", " + this.first;
        }
    };
}

// note: 'this' referes to current object, like 'self' in python

s = makePerson("Simon", "Willison")
s.fullName();   // "simon willison"
s.fullNameReversed();   // "willison, simon"

// improvement: using this 
function Person(first, last) {
    this.first = first;
    this.last = last;
    this.fullName = function() {
        return this.first + " " + this.last;
    };
    this.fullNameReversed = function() {
        return this.last + ", " + this.first;
    };
}

// create an instance?!
var ps = new Person("Simon", "Willison");


// improvement
function personFullName() {
  return this.first + ' ' + this.last;
}
function personFullNameReversed() {
  return this.last + ', ' + this.first;
}
function Person(first, last) {
  this.first = first;
  this.last = last;
  this.fullName = personFullName;
  this.fullNameReversed = personFullNameReversed;
}


// improvement, 注意Person.prototype.
function Person(first, last) {
  this.first = first;
  this.last = last;
}
Person.prototype.fullName = function fullName() {
  return this.first + ' ' + this.last;
};
Person.prototype.fullNameReversed = function fullNameReversed() {
  return this.last + ', ' + this.first;
};


// Object.prototype是极其有用的, you can add extra methods to existing objects at runtime:
s = new Person("Simon", "Willison");
s.firstNameCaps();

Person.prototype.firstNameCaps = function firstNameCaps() {
    return this.first.toUpperCase()
};
s.firstNameCaps(); // "SIMON"