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