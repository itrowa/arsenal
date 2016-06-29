// ajax without jquery
function loadXMLDoc() {
    var xmlhttp;

    if (window.XMLHttpRequest) {
        // code for IE7+, Firefox, Chrome, Opera, Safari
        xmlhttp = new XMLHttpRequest();
    } else {
        // code for IE6, IE5
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }

    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4 ) {
           if(xmlhttp.status == 200){
               alert("success");
           }
           else if(xmlhttp.status == 400) {
              alert("error 400")
           }
           else {
               alert("something broke")
           }
        }
    }

    xmlhttp.open("GET", "test.html", true);
    xmlhttp.send();
}