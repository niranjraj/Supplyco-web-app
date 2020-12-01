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

    $('.update-cart').click(function (e) { 
        e.preventDefault();
        var productId=this.dataset.product
        var action=this.dataset.action
        
        updateUserOrder(productId,action)

        
    });

    function updateUserOrder(productId,action){
            var url='update_item/'

            $.ajax({
                type: "POST",
                headers: { "X-CSRFToken": csrftoken },
                url: "update_item",
                data: JSON.stringify({'productId':productId,'action':action}),
                dataType: "json",
                success: function (response) {
                   var cartNumber=response.cartItems;
                   var cartTotal=response.cartTotal;
                   var cartQuantity=response.itemQuantity;
                    $('.cart-number').html(cartNumber);
                    $('.cart-total').html(cartTotal);
                    if(cartQuantity>0){
                        $(`.item-quantity-value[data-product=${productId}]`).html(cartQuantity);
                    }else{
                       
                        $(`.cart-item[data-product=${productId}]`).remove();
                    }
                    
                    
                }
            });
    }
});



   