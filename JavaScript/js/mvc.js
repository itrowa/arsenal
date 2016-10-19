var M = {}, V = {}, C = {};

/* Model View Controller Pattern with Form Example */


/* Controller Handles the Events */

M = {
    data: {
        userName : "Dummy Guy",
        userNumber : "000000000"
    }, 
    setData : function(d){
        this.data.userName = d.userName;
        this.data.userNumber = d.userNumber;
    },
    getData : function(){
        return data;
    }
}

V = {
    userName : document.querySelector("#inputUserName"),
    userNumber : document.querySelector("#inputUserNumber"),
    update: function(M){
        this.userName.value = M.data.userName;
        this.userNumber.value = M.data.userNumber;
    }
}

C = {
    model: M,
    view: V,
    handler: function(){
        this.view.update(this.model);
    }
}

document.querySelector(".submitBtn").addEventListener("click", function(){
    C.handler.call(C);
}); 

/* Model Handles the Data */

/* View Handles the Display */