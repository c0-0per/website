
function checkSingleInput(inputElement) {
    if(inputElement.value === "" || inputElement.value.length > 64)
        return false;

    return true;
}

// function checkEmail(inputElement) {
//     let mail = inputElement.value;
    
//     let res = /^([a-zA-Z0-9\._]+)@([a-zA-Z0-9])+.([a-z]+)?$/;

//     if (res.text(mail)){
//         return true;
//     }
//     return false;
// }

   

function EmailValidation(enteredEmail) {

    var mail_format = /^w+([.-]?w+)*@w+([.-]?w+)*(.w{2,3})+$/;

    if(mail_format.value.match(enteredEmail)) {

        alert("Yeah! a valid email!");

        document.form1.text1.focus();

        return true;

    }
    else {

        alert("Sorry! an invalid email!");

        document.form1.text1.focus();

        return false;
    }


}
 


function checkForm(event) {
    let nameCheckResult = checkSingleInput(document.getElementById("name-input"));
    // let surnameCheckResult = checkSingleInput(document.getElementById("surname-input"));
    let emailCheckResult = checkEmail(document.getElementById("email-input"));
    
    
    
    if(!nameCheckResult){
        let chybovaHlaska = document.getElementById("name-input-error");
        chybovaHlaska.classList.replace("error-hidden", "error-visible");
        event.preventDefault();
        return false;
    }

    // if(!surnameCheckResult){
    //     let chybovaHlaska = document.getElementById("surname-input-error");
    //     chybovaHlaska.classList.replace("error-hidden", "error-visible");
    //     event.preventDefault();
    //     return false;
    // }
    
    if(!emailCheckResult){
        let chybovaHlaska = document.getElementById("email-input-error");
        chybovaHlaska.classList.replace("error-hidden", "error-visible");
        event.preventDefault();
        return false;
    }

    return true;
}




function registerEventHandlers() {
    let tlacitko = document.getElementById("register-form");
    tlacitko.addEventListener("submit", checkForm);
    
}

window.addEventListener("load", registerEventHandlers);
