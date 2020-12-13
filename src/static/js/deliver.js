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


    
    // <------page layout--------->
    $('nav').on('click', '> *', function(e) {
        e.preventDefault();
        $("nav").children().removeClass('active');
        $(this).addClass('active');
        console.log()
        if(this.className.includes("home")){
            
            $(".main-content").children().removeClass('first-view');
            $('.section-1').addClass('first-view');
        }
        else if(this.className.includes("deliver")){
          
            $(".main-content").children().removeClass('first-view');
            $('.section-2').addClass('first-view');
        }
        else if(this.className.includes("rules")){
            
            $(".main-content").children().removeClass('first-view');
            $('.section-3').addClass('first-view');
        }
    });


    $('.check-btn').click(function (e) { 


        e.preventDefault();

       
            $('.modal-wrapper').addClass("open");
         
            var firstTime=this.dataset.action;
            var deliveryId=this.dataset.deliver;
            var startOrComplete=$(`.status[data-open="${deliveryId}"]`).text();
            if(startOrComplete=="Delivering"){
                $('.start-btn').removeClass('btn-view');
                $('.complete-btn').addClass('btn-view');
            }
            else if(startOrComplete=="Delivered"){
                $('.start-btn').removeClass('btn-view');
                $('.complete-btn').removeClass('btn-view');
            }
        
            $.ajax({
                type: "POST",
                headers: { "X-CSRFToken": csrftoken },
                url: "",
                data: JSON.stringify({'deliveryId':deliveryId,'action':'check'}),
                dataType: "json",
                success: function (response) {
                    var city=response['shippingInfo']['city'];
                    var street=response['shippingInfo']['address'];
                    var zipcode=response['shippingInfo']['zipcode'];
                    var phoneNumber=response['shippingInfo']['phoneNumber'];  
                    var itemList=response['itemList'];
                    var userCheck=response['userCheck'];
                    $('.city').html(city);
                    $('.street').html(street);
                    $('.zipcode').html(zipcode);
                    $('.phoneNumber').html(phoneNumber);
                    $('.order-items').attr("data-deliverid",`${deliveryId}`);
                    $('.start-btn').attr("data-deliverid",`${deliveryId}`);
                    $('.complete-btn').attr("data-deliverid",`${deliveryId}`);
                    $('.order-items').html('');
                    
                    if(!userCheck){
                        $('.start-btn').removeClass('btn-view');
                        $('.complete-btn').removeClass('btn-view');
                    }
            
            
                    for (var i=0;i<itemList.length;i++){
                        console.log(itemList[i])
                    
                    $(`<div class='item-wrapper'><div class='item-name'>${itemList[i]["itemName"]}</div><div class='item-quantity'>x${itemList[i]["itemQuantity"]}</div></div>`).appendTo('.order-items')
                    
                        
                    
                    }
                    
                    
                    
            
                
                    
                }
        });
        


        
        
        
    });


    $('.start-btn').click(function (e) { 
        e.preventDefault();   
        $('.start-btn').removeClass('btn-view');
        $('.complete-btn').addClass('btn-view');
        var deliverId=this.dataset.deliverid
        console.log(typeof deliverId)

        $.ajax({
            type: "POST",
            headers: { "X-CSRFToken": csrftoken },
            url: "",
            data: JSON.stringify({'startId':deliverId,'action':'start'}),
            dataType: "json",
            success: function (response) {
                
     
           
        
                   
         
             
                
            }
        });

        
        
    });

    $('.complete-btn').click(function (e) { 
        e.preventDefault();
        var deliverId=this.dataset.deliverid


        $.ajax({
            type: "POST",
            headers: { "X-CSRFToken": csrftoken },
            url: "",
            data: JSON.stringify({'completeId':deliverId,'action':'complete'}),
            dataType: "json",
            success: function (response) {
                
              
                console.log("success")
        
                   
         
             
                
            }
        });

        
    });





    $('.fa-times').click(function (e) { 
        e.preventDefault();
        $('.modal-wrapper').removeClass("open");
    });

  
});