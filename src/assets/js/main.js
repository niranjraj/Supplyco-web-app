const navBtn=document.querySelector('.nav-btn');
const drawer=document.querySelector('.drawer');

let navOpen=false;

navBtn.addEventListener('click',()=>{
    if(!navOpen){
        navBtn.classList.add('open');
        drawer.classList.add('open');
     
        navOpen=true;
    } else{
        navBtn.classList.remove('open');
        drawer.classList.remove('open');
    
        navOpen=false;
    }
})


let counter=1;
setInterval(function (){
    document.getElementById('radio'+counter).checked=true;
    counter++;
    if(counter>4){
        counter=1;
    }
},5000);

window.addEventListener("scroll",function(){
    var header=document.querySelector("header");
    header.classList.toggle("sticky",window.scrollY >0);
})

    
