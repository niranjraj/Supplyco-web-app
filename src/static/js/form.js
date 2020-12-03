const log_in_btn=document.querySelector('#panel-btn1');
const sign_up_btn=document.querySelector('#panel-btn2');
const container=document.querySelector('.container');



sign_up_btn.addEventListener('click', ()=>{
    console.log("pressed");
    container.classList.remove("click-mode");  
 
})

log_in_btn.addEventListener('click', ()=>{
    console.log("pressed");
    container.classList.add("click-mode");  

})


