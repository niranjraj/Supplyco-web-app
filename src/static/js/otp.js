$(document).ready(function () {

    function getToken(name) {
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
    const csrftoken = getToken('csrftoken');

    
    $('.otp-submit').click(function (e) { 
        e.preventDefault();
       keyvalue= $('.otp-field').val();
       $.ajax({
           type: "POST",
           headers: { "X-CSRFToken": csrftoken },
           url: "otp",
           data: keyvalue,
           dataType: "text",
           success: function (response) {
            var data=JSON.parse(response)
            if( data=='true'){
           
                window.location.href="/"
            }
            

               
           }
       });
        
    });
});