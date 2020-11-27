const textArea=document.querySelector('textarea');
const textInput=document.querySelector('.text-input');

textArea.onfocus=function(){
    textInput.classList.add("toggle-mode");

}

textArea.onblur=function(){
    textInput.classList.remove("toggle-mode");

}
