/*global document, location,window,current,next,prev*/
/*jslint browser: true*/
/*global $*/


$(document).ready(function () {
    $('.section-facts').waypoint(function(){
      $('.count').each(function () {
    $(this).prop('Counter',0).animate({
        Counter: $(this).text()
    }, {
        duration: 10000,
        easing: 'swing',
        step: function (now) {
            $(this).text(Math.ceil(now));
        }
    });
});
         },{
        offset:'50%'
    })
    
    var $navigation = $('nav');

  
    /*add/remove the sticky bar according to sreensize*/  
    $(window).ready(function() {
    if (window.innerWidth <= 992) {$navigation.addClass('sticky');

}
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
                $('.btnlogin1').removeClass('btn2');
            
        } else if(window.innerWidth > 992){$('nav').removeClass('sticky');
        $('.btnlogin1').addClass('btn2');
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
    
    /*NAVIGATION SCROLL */   
    

    // Select all links with hashes
$('a[href*="#"]')
  // Remove links that don't actually link to anything
  .not('[href="#"]')
  .not('[href="#0"]')
  .click(function(event) {
    if (
      location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') 
      && 
      location.hostname == this.hostname
    ) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      if (target.length) {
        event.preventDefault();
        $('html, body').animate({
          scrollTop: target.offset().top
        }, 1000, function() {
          var $target = $(target);
          $target.focus();
          if ($target.is(":focus")) { 
            return false;
          } else {
            $target.attr('tabindex','-1'); 
            $target.focus(); 
          }
        });
      }
    }
  });
    

    /*Animations on scroll*/
    $('.js--wp-a1').waypoint(function(){
    $('.js--wp-a1').addClass('animated fadeInUp');
        
    },{
        offset:'70%'
    })
        $('.js--wp-a2').waypoint(function(){
    $('.js--wp-a2').addClass('animated fadeInUp');
        
    },{
        offset:'60%'
    })
        $('.js--wp-a3').waypoint(function(){
    $('.js--wp-a3').addClass('animated fadeInUp');
        
    },{
        offset:'60%'
    })
        $('.js--wp-a4').waypoint(function(){
    $('.js--wp-a4').addClass('animated fadeInUp');
        
    },{
        offset:'60%'
    })
        $('.js--wp-a5').waypoint(function(){
    $('.js--wp-a5').addClass('animated fadeIn');
        
    },{
        offset:'80%'
    })
     $('.js--flip-1').waypoint(function(){
    $('.js--flip-1').addClass('animated flipInY');
        
    },{
        offset:'60%'
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

    $('.section-testimonials div h2').waypoint(function(){
    $('.section-testimonials div h2').addClass('animated pulse');
        
    },{
        offset:'50%'
    }) 
        $('.section-facts div h2').waypoint(function(){
    $('.section-facts div h2').addClass('animated pulse');
        
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
    $('.sidebar1').waypoint(function(){
    $('.sidebar1').addClass('animated zoomInRight');
        
    },{
        offset:'50%'
    })   
    $('.feedback0').waypoint(function(){
    $('.feedback0').addClass('animated slideInLeft');
        
    },{
        offset:'40%'
    })    
        $('.feedback1').waypoint(function(){
    $('.feedback1').addClass('animated slideInUp');
        
    },{
        offset:'60%'
    }) 
            $('.feedback2').waypoint(function(){
    $('.feedback2').addClass('animated slideInRight');
        
    },{
        offset:'80%'
    }) 
        $('.feedback3').waypoint(function(){
    $('.feedback3').addClass('animated slideInLeft');
        
    },{
        offset:'40%'
    })    
        $('.feedback4').waypoint(function(){
    $('.feedback4').addClass('animated slideInUp');
        
    },{
        offset:'60%'
    }) 
            $('.feedback5').waypoint(function(){
    $('.feedback5').addClass('animated slideInRight');
        
    },{
        offset:'80%'
    }) 
    $('.centers').waypoint(function(){
    $('.centers').addClass('animated slideInRight');
        
    },{
        offset:'50%'
    })   
    $('.js--wp-6-1').waypoint(function(){
    $('.js--wp-6-1').addClass('animated slideInRight');
        
    },{
        offset:'80%'
    }) 
        $('.js--wp-6-2').waypoint(function(){
    $('.js--wp-6-2').addClass('animated slideInRight');
        
    },{
        offset:'80%'
    })  
    $('.js--wp-6-3').waypoint(function(){
    $('.js--wp-6-3').addClass('animated slideInRight');
        
    },{
        offset:'80%'
    })  
        $('.js--wp-6-4').waypoint(function(){
    $('.js--wp-6-4').addClass('animated slideInRight');
        
    },{
        offset:'80%'
    })  
        $('.js--wp-6-5').waypoint(function(){
    $('.js--wp-6-5').addClass('animated slideInRight');
        
    },{
        offset:'80%'
    }) 
     $('.js--wp-6-6').waypoint(function(){
    $('.js--wp-6-6').addClass('animated slideInRight');
        
    },{
        offset:'80%'
    }) 
        $('.js--wp-6-7').waypoint(function(){
    $('.js--wp-6-7').addClass('animated slideInRight');
        
    },{
        offset:'80%'
    })  
    $('.js--wp-6-8').waypoint(function(){
    $('.js--wp-6-8').addClass('animated slideInRight');
        
    },{
        offset:'80%'
    })  
        $('.js--wp-6-9').waypoint(function(){
    $('.js--wp-6-9').addClass('animated slideInRight');
        
    },{
        offset:'80%'
    })  
        $('.js--wp-6-10').waypoint(function(){
    $('.js--wp-6-10').addClass('animated slideInRight');
        
    },{
        offset:'80%'
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
        $('.js--wp-1-2-0').waypoint(function(){
    $('.js--wp-1-2-0').addClass('animated fadeIn');
        
    },{
        offset:'50%'
    })
        $('.js--wp-1-2-1').waypoint(function(){
    $('.js--wp-1-2-1').addClass('animated fadeIn');
        
    },{
        offset:'60%'
    })
        $('.js--wp-1-2-2').waypoint(function(){
    $('.js--wp-1-2-2').addClass('animated fadeIn');
        
    },{
        offset:'70%'
    })
        $('.js--wp-2').waypoint(function(){
        $('.js--wp-2').addClass('animated fadeInUp');
        
    },{
        offset:'50%'
    })
        $('.js--wp-2-1').waypoint(function(){
        $('.js--wp-2-1').addClass('animated fadeInUp');
        
    },{
        offset:'50%'
    })    
    
        $('.js--wp-2-2').waypoint(function(){
        $('.js--wp-2-2').addClass('animated fadeInUp');
        
    },{
        offset:'50%'
    })  

        $('.js--wp-2-3').waypoint(function(){
        $('.js--wp-2-3').addClass('animated fadeInUp');
        
    },{
        offset:'50%'
    })  
            $('.js--wp-2-4').waypoint(function(){
        $('.js--wp-2-4').addClass('animated fadeInUp');
        
    },{
        offset:'50%'
    }) 
            $('.js--wp-2-5').waypoint(function(){
        $('.js--wp-2-5').addClass('animated fadeInUp');
        
    },{
        offset:'50%'
    })       

       $('.js--wp-2-6').waypoint(function(){
        $('.js--wp-2-6').addClass('animated fadeInUp');
        
    },{
        offset:'50%'
    })    
    
        $('.js--wp-2-7').waypoint(function(){
        $('.js--wp-2-7').addClass('animated fadeInUp');
        
    },{
        offset:'50%'
    })  

        $('.js--wp-2-8').waypoint(function(){
        $('.js--wp-2-8').addClass('animated fadeInUp');
        
    },{
        offset:'50%'
    })  
            $('.js--wp-2-9').waypoint(function(){
        $('.js--wp-2-9').addClass('animated fadeInUp');
        
    },{
        offset:'50%'
    }) 
            $('.js--wp-2-10').waypoint(function(){
        $('.js--wp-2-10').addClass('animated fadeInUp');
        
    },{
        offset:'50%'
    })       


        $('.js--wp-3').waypoint(function(){
        $('.js--wp-3').addClass('animated fadeIn');
        
    },{
        offset:'35%'
    })      
    $('.js--wp-3-2').waypoint(function(){
        $('.js--wp-3-2').addClass('animated fadeIn');
        
    },{
        offset:'60%'
    })
    
    
        $('.js--wp-4').waypoint(function(){
        $('.js--wp-4').addClass('animated pulse');
        
    },{
        offset:'50%'
    });
    
        $('.js--wp-5').waypoint(function(){
        $('.js--wp-5').addClass('animated pulse');
        
    },{
        offset:'40%'
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
    
    
});
