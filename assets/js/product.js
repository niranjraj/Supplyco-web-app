$(document).ready(function () {

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


  $('.cart-icon').click(function (e) { 
    $('.cart-modal').addClass("open-cart");
  });

  $('.close-cart').click(function (e) { 
    $('.cart-modal').removeClass("open-cart");
  });


  $("#search-input").on("keyup", function () {
    var value=$(this).val().toLowerCase();
    $('.product-card').filter(function(){
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    })
    
  });


  $('.search-icon').click(function (e) { 
    $(this).toggleClass("active-mode");
    $('#search-input').toggleClass("active-width");
  });

});