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

    $('#payment-info').hide();
    $(form).submit(function (e) { 
        e.preventDefault()
        $('.btn-success ').hide();
        $('#payment-info').show(800);
        
    });

    
    paypal.Buttons({

        // Set up the transaction
        createOrder: function(data, actions) {
            return actions.order.create({
                purchase_units: [{
                    amount: {
                        value: parseFloat(total).toFixed(2)
                       
                    }
                }]
            });
        },

        // Finalize the transaction
        onApprove: function(data, actions) {
            return actions.order.capture().then(function(details) {
                // Show a success message to the buyer
                submitFormData()
            });
        }


    }).render('#paypal-button-container'); 
    
  


    function submitFormData(){
      
        var form=document.getElementById('form')
        var shippingInfo={
            'address':form.address.value,
            'city':form.city.value,
            'zipcode':form.zipcode.value,
            'phoneNumber':form.phoneNumber.value,
        }

        $.ajax({
            type: "POST",
            headers: { "X-CSRFToken": csrftoken },
            url: 'process_order',
            data: JSON.stringify({'total':total,'shipping':shippingInfo,}),
            dataType: "json",
            success: function (response) {
                alert('Transaction completed')
                window.location='/products';
                
            }
        });
    }
});