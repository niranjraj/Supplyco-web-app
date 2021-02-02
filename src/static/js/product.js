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



  $('html').click(function () { 
     $('.menu').removeClass("active");
      
  });
  $('.menu-icon').click(function (e) { 
         e.stopPropagation();  
     $('.menu').toggleClass("active");
  });

  var prevScrollpos = $(window).scrollTop();
  $(window).scroll(function () { 
   var currentScrollPos = $(window).scrollTop();
   if (prevScrollpos > currentScrollPos) {
     $('nav').css("top","0px" );
   } else {
     $('nav').css("top","-80px" );
     $('.menu').removeClass("active");
   }
   prevScrollpos = currentScrollPos;
  });

  $('.product-img-wrapper').click(function (e) { 
    e.preventDefault();
    $('.modal-wrapper').addClass("open");
    var productId=this.dataset.product;
    var action =this.dataset.action;
    console.log(action);
    $.ajax({
      type: "POST",
      headers: { "X-CSRFToken": csrftoken },
      url: "productModal",
      data: JSON.stringify({'productId':productId}),
      dataType: "json",
      success: function (response) {
        var productTitle=response['productTitle'];
        var productPrice=response['productPrice'];
        var productDescription=response['productDescription'];
        var productImage=response['productImage'];
          $('.modal-item-price').html(`₹${productPrice}`);
          $('.modal-item-description').html(productDescription);
          $('.modal-item-name').html(productTitle);
          $('.modal-item-img').attr('src', `/media/${productImage}`);

          $('.modal-add-btn').attr('data-product', productId);
          $('.modal-add-btn').attr('data-action', "add");
          console.log(productTitle);
          
          
      }
  });
    
  });




  $("#search-input").on("keyup", function () {
    var value=$(this).val().toLowerCase();
    $('.product-card').filter(function(){
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    })
    
  });

  $('.fa-times').click(function (e) { 
    e.preventDefault();
    $('.modal-wrapper').removeClass("open");
});


});