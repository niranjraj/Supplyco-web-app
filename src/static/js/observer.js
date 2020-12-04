const header=document.querySelector("header");
const  headerNav= document.querySelector(".primary-divider");
const sliders =document.querySelectorAll('.card');
const headerOptions={
   
};

const headerObserver= new IntersectionObserver(function(entries,headerObserver) {

    entries.forEach(entry =>{
        if(!entry.isIntersecting){
            header.classList.add('nav-scroll');
        }else{
            header.classList.remove('nav-scroll');
        }
    })
},headerOptions);

headerObserver.observe(headerNav);


const appearOptions={
   threshold:0.3,
  
};

const appearOnScroll= new IntersectionObserver(function(entries,appearOnScroll){
    entries.forEach(entry=>{
        if(!entry.isIntersecting){
            return;
        } else {
            entry.target.classList.add('appear');
            appearOnScroll.unobserve(entry.target);
        }
    })
},appearOptions);


sliders.forEach(slider =>{
    appearOnScroll.observe(slider);
})


