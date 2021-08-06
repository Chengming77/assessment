function save(){  
    var person = new Object;
    person.timestamp = new Date().getTime();
    person.name = document.getElementById("name").value;
    person.age = document.getElementById("age").value;  
    person.phone = document.getElementById("phone").value;
    person.gender = document.getElementById("gender").value;
    person.comments = document.getElementById("comments").value;
    var str = JSON.stringify(person);
    localStorage.setItem(person.timestamp,str);  
    alert("add successfully");
}