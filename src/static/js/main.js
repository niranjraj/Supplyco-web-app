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


ScrollOut({
    targets:'.hero-left,.hero-right,.details,.detail-info-1,.info-img-wrapper',
});

window.addEventListener("scroll",function(){
    var header=document.querySelector("header");
    header.classList.toggle("sticky",window.scrollY >0);
})

    
