function loadAll(){  
    var list = document.getElementById("list");  
    if(localStorage.length>0){  
        var result = "";  
        //result += "<tr><td>name</td><td>age</td><td>phone</td></tr><td>gender</td>";  
        for(var i=0;i<localStorage.length;i++){ 
            var name = localStorage.key(i);  
            var str = localStorage.getItem(name);  
            //var person = JSON.parse(str);  
            //result += "<tr><td>"+person.name+"</td><td>"+person.age+"</td><td>"+person.phone+"</td><td>"+person.gender+"</td></tr>"; 
            result += str;
        }  
        //result += "</table>";  
        list.innerHTML = result;  
    }else{  
        list.innerHTML = "none";  
    }  
} 

function del(){
	localStorage.clear();
	loadAll();
}