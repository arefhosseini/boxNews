/*document.getElementById("firstName").onblur = function(){
 var req ;
 req = new XMLHttpRequest();
 req.onreadystatechange=function(){
 if (req.readyState == 4 && req.status == 200){
 var data = JSON.parse(req.responseText);
 alert(data.ali);
 alert(req.response.toString());
 // alert(req.json);
 }
 }
 req.open("GET", "/signup", true);
 req.send();
 //delete req;
 }*/

document.getElementsByName("firstname").focus(function() {
    alert("in");
}).blur(function() {
    alert("out");
});
