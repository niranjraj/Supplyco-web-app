$(document).ready(function () {

    if($('.error-msg-1').children().length>0){
        $('.error-msg-1').addClass('slide-in');
    }

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
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
                
                var data=JSON.parse(response)
                var errorvalue=data["errormsg"]
                var success=data["success"]
                console.log(typeof success);
                if (success){
                    console.log("success")
                    document.location.href="/sign/otp";
                }
                var errormsg=$(".error-msg").html();

                if( $('#aadhaar-error').length )         // use this if you are using id to check
                {     
                     $('#aadhaar-error').remove();
                }
                if( $('#email-error').length )         // use this if you are using id to check
                {
                    $('#email-error').remove();
                }
                if( $('#password-error').length )         // use this if you are using id to check
                    {
                        $('#password-error').remove();  
                    }

                for (var msg in errorvalue){
            
                    if (msg=="aadhaar"){
                        $("<div id='aadhaar-error' class='alert alert-danger '>Invalid Aadhaar or Aadhaar already in use</div>").appendTo('.error-msg');
                        $('.error-msg').addClass('slide-in');
                    }
                    if (msg=="email"){
                        $("<div id='email-error' class='alert alert-danger '>Invalid Email or User already exist</div>").appendTo('.error-msg');
                        $('.error-msg').addClass('slide-in');
                    }
                     if (msg=="password2"){
                        
                        $("<div id='password-error' class='alert alert-danger '>Passwords don't match</div>").appendTo('.error-msg');
                        $('.error-msg').addClass('slide-in');
                    }
                    
                }
            
            

                
                
            }
        });
        
    });
});