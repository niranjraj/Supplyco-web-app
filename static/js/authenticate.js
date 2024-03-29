$(document).ready(function () {

    if($('.error-msg-1').children().length>0){
        $('.error-msg-1').addClass('slide-in');
    }

    // csrftoken
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
        
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');
    



    $('#sign-form').submit(function (e) { 
        e.preventDefault();
        var form=document.getElementById('sign-form')
        var userInfo={
            'email':form.email.value,
            'aadhaar':form.aadhaar.value,
            'password':form.password.value,
            'confirmpassword':form.confirmpassword.value,
        }

        $.ajax({
            type: "POST",
            headers: { "X-CSRFToken": csrftoken },
            url: 'createUser',
            data: JSON.stringify({'userData':userInfo,}),
            dataType: "json",
            success: function (response) {
                
                // dynamic error msg

                var data=JSON.parse(response)
                var errorvalue=data["errormsg"]
                var success=data["success"]
          
                if (success){
                 
                    document.location.href="/sign/otp";
                }      
                    
                $('#aadhaar-error').remove(); 
                $('#email-error').remove();
                $('#password-error').remove();  
                

                for (var msg in errorvalue){
            
                    if (msg=="aadhaar"){
                        $("<div id='aadhaar-error' class='alert alert-danger '>Invalid Aadhaar or Aadhaar already in use</div>").appendTo('.error-msg');
                    }
                    if (msg=="email"){
                        $("<div id='email-error' class='alert alert-danger '>Invalid Email or User already exist</div>").appendTo('.error-msg');
                    }
                     if (msg=="password2"){           
                        $("<div id='password-error' class='alert alert-danger '>Passwords don't match</div>").appendTo('.error-msg');
                    }  
                }
                $('.error-msg').addClass('slide-in');
               
            
            

                
                
            }
        });
        
    });
});