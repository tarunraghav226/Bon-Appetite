const login = document.getElementById("login");
const signup = document.getElementById("signup");

const loginForm = document.querySelector(".form--login");
const modalOverlay = document.querySelector(".overlay--modal");
const closeModalBtn =  document.querySelector(".close--modal--btn");
const signUpForm = document.querySelector(".form--signup");

const messageCloseBtn = document.getElementById("message--close--icon");

loginForm.style.display = "none";
modalOverlay.style.display = "none";
closeModalBtn.style.display = "none";
signUpForm.style.display = "none";

closeModalBtn?.addEventListener('click', ()=>{
    loginForm.style.display = "none";
    modalOverlay.style.display = "none";
    closeModalBtn.style.display = "none";
    signUpForm.style.display = "none";
});

login?.addEventListener('click', ()=>{
    if(modalOverlay.style.display == "block" && 
        signUpForm.style.display !== "block"){
        closeModalBtn.style.display = "none";
        modalOverlay.style.display = "none";
    }
    else{
        modalOverlay.style.display = "block";
        closeModalBtn.style.display = "block";
    }

    signUpForm.style.display = "none";

    if(loginForm.style.display == "block")
        loginForm.style.display = "none";
    else 
        loginForm.style.display = "block";

});

signup?.addEventListener('click', ()=>{
    if(modalOverlay.style.display == "block" && 
        loginForm.style.display !== "block"){
        closeModalBtn.style.display = "none";
        modalOverlay.style.display = "none";
    }
    else{
        modalOverlay.style.display = "block";
        closeModalBtn.style.display = "block";
    }

    loginForm.style.display = "none";

    if(signUpForm.style.display == "block")
        signUpForm.style.display = "none";
    else 
        signUpForm.style.display = "block";
});

messageCloseBtn?.addEventListener("click", ()=>{
    document.querySelector(".messages").style.display = "none";
});