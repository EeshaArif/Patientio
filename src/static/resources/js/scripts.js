/*global document, location,window,current,next,prev*/
/*jslint browser: true*/
/*global $*/
$(document).ready(function () {
    
      
    
    var $navigation = $('nav');
  
    /*add/remove the sticky bar according to sreensize*/  
    $(window).ready(function() {
    if (window.innerWidth <= 992) {$navigation.addClass('sticky');}
    else {
        $navigation.removeClass('sticky');
    }
  
    });
    
    /*add/remove the sticky bar when you resize the screen*/   
    
    $(window).resize(function() {
    if (window.innerWidth <= 992)            {$navigation.addClass('sticky');
       
                                             }
        
    else {
        $navigation.removeClass('sticky');
        $('.main-nav').css("display","block");
        
    }
  
    });
   
    
    
    /* for the sticky navigation*/
    $('.js--section-declare').waypoint(function (direction) {
        if (direction === "down") {
            $('nav').addClass('sticky');
            
        } else if(window.innerWidth > 992){$('nav').removeClass('sticky');
                   }
    }, {
        offset: '60px;'
    
    });
    
    
    

    
    
    
    /* Scroll on buttons */
    $('.js--scroll-to-plans').click(function() {
        $('html, body').animate({scrollTop: $('.section-plans').offset().top},1000);
        
    });
        $('.js--scroll-to-start').click(function() {
        $('html, body').animate({scrollTop: $('.js--section-features').offset().top},1000);
        
    });
    
    /*NAVIGATION SCROLL */   /*NET SAY UTHAIYA HUA CODE*/
    

    // Select all links with hashes
$('a[href*="#"]')
  // Remove links that don't actually link to anything
  .not('[href="#"]')
  .not('[href="#0"]')
  .click(function(event) {
    // On-page links
    if (
      location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') 
      && 
      location.hostname == this.hostname
    ) {
      // Figure out element to scroll to
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      // Does a scroll target exist?
      if (target.length) {
        // Only prevent default if animation is actually gonna happen
        event.preventDefault();
        $('html, body').animate({
          scrollTop: target.offset().top
        }, 1000, function() {
          // Callback after animation
          // Must change focus!
          var $target = $(target);
          $target.focus();
          if ($target.is(":focus")) { // Checking if the target was focused
            return false;
          } else {
            $target.attr('tabindex','-1'); // Adding tabindex for elements not focusable
            $target.focus(); // Set focus again
          }
        });
      }
    }
  });
    

    /*Animations on scroll*/
    $('.js--wp-a1').waypoint(function(){
    $('.js--wp-a1').addClass('animated fadeIn');
        
    },{
        offset:'70%'
    })
        $('.js--wp-a2').waypoint(function(){
    $('.js--wp-a2').addClass('animated fadeIn');
        
    },{
        offset:'60%'
    })
        $('.js--wp-a3').waypoint(function(){
    $('.js--wp-a3').addClass('animated fadeIn');
        
    },{
        offset:'60%'
    })
        $('.js--wp-a4').waypoint(function(){
    $('.js--wp-a4').addClass('animated fadeIn');
        
    },{
        offset:'60%'
    })
        $('.js--wp-a5').waypoint(function(){
    $('.js--wp-a5').addClass('animated fadeIn');
        
    },{
        offset:'80%'
    })
    $('.js--wp-b1').waypoint(function(){
    $('.js--wp-b1').addClass('animated fadeIn');
        
    },{
        offset:'60%'
    })
        $('.js--wp-b2').waypoint(function(){
    $('.js--wp-b2').addClass('animated fadeIn');
        
    },{
        offset:'60%'
    })
        $('.js--wp-b3').waypoint(function(){
    $('.js--wp-b3').addClass('animated fadeIn');
        
    },{
        offset:'60%'
    })
        $('.js--wp-b4').waypoint(function(){
    $('.js--wp-b4').addClass('animated fadeIn');
        
    },{
        offset:'60%'
    })
        $('.js--wp-b5').waypoint(function(){
    $('.js--wp-b5').addClass('animated fadeIn');
        
    },{
        offset:'80%'
    })

    $('.contactbtn').waypoint(function(){
    $('.contactbtn').addClass('animated fadeInRightBig');
        
    },{
        offset:'100%'
    })      
    $('.resultbtn').waypoint(function(){
    $('.resultbtn').addClass('animated pulse');
        
    },{
        offset:'40%'
    })      
 /*   $('.letterbtn').waypoint(function(){
    $('.letterbtn').addClass('animated flash');
        
    },{
        offset:'50%'
    })     */ 
    $('.section-testimonials div h2').waypoint(function(){
    $('.section-testimonials div h2').addClass('animated pulse');
        
    },{
        offset:'50%'
    })    
    $('.section-condition div h2').waypoint(function(){
    $('.section-condition div h2').addClass('animated pulse');
        
    },{
        offset:'50%'
    })     
    $('.guidelines').waypoint(function(){
    $('.guidelines').addClass('animated pulse');
        
    },{
        offset:'50%'
    })   
    $('.section-cities div h2').waypoint(function(){
    $('.section-cities div h2').addClass('animated pulse');
        
    },{
        offset:'50%'
    })   
    $('.sidebar').waypoint(function(){
    $('.sidebar').addClass('animated pulse');
        
    },{
        offset:'50%'
    })  
    $('.feedback').waypoint(function(){
    $('.feedback').addClass('animated slideInLeft');
        
    },{
        offset:'50%'
    })    
    $('.centers').waypoint(function(){
    $('.centers').addClass('animated slideInRight');
        
    },{
        offset:'50%'
    })   
    $('.schedule').waypoint(function(){
    $('.schedule').addClass('animated slideInUp');
        
    },{
        offset:'50%'
    })
    $('.js--wp-1').waypoint(function(){
    $('.js--wp-1').addClass('animated fadeIn');
        
    },{
        offset:'50%'
    })  
    $('.js--wp-1-2').waypoint(function(){
    $('.js--wp-1-2').addClass('animated fadeIn');
        
    },{
        offset:'50%'
    })
    
        $('.js--wp-2').waypoint(function(){
        $('.js--wp-2').addClass('animated fadeInUp');
        
    },{
        offset:'50%'
    })
    
        $('.js--wp-3').waypoint(function(){
        $('.js--wp-3').addClass('animated fadeIn');
        
    },{
        offset:'50%'
    })
    
    
        $('.js--wp-4').waypoint(function(){
        $('.js--wp-4').addClass('animated pulse');
        
    },{
        offset:'50%'
    });
    
    /*Mobile nac*/
    $('.js--nav-icon').click(function() {
        var nav=$('.js--main-nav');
        nav.slideToggle(200);
        
        var icon=$('.js--nav-icon i');
        
        
        if( icon.hasClass('ion-navicon-round')){
            
            icon.addClass('ion-close-round');
            icon.removeClass('ion-navicon-round');
        } else {
            icon.addClass('ion-navicon-round');
            icon.removeClass('ion-close-round');
        }
        
        
        
    })
    
 $(document).ready(function(){

            $("#theTarget").skippr();

        });  
    
    
    
    
    
$('.slider span.next').click(function() {
  $current = $(this).siblings('img.active');
  $next = $current.next('img');
  if ($next.length === 0) {
      $next = $current.prev('img');
  }
  if ($next.length != 0) {
    $current.removeClass('active');
    $next.addClass('active');
  }
    


    
    
})
$('.slider span.prev').click(function() {
  $current = $(this).siblings('img.active');
  $prev = $current.prev('img');
  if ($prev.length === 0) {
      $prev = $current.next('img');
  }
    
  if ($prev.length != 0) {
    $current.removeClass('active');
    $prev.addClass('active');
  }
  
})
    
});