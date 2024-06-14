$(".menu-toggle").click(function(){
    var $menu = $(".menu");
    if($menu.hasClass("open")) {
      $menu.removeClass("open");
      $menu.addClass("close");
    } else {
      $menu.addClass("open");
      $menu.removeClass("close");
    }
  });
  
  // demo it, yo!
  $('body')
    .queue(function(next) {
      $(".menu-toggle").click();
      next();
    }).delay(2200)
    .queue(function(next) {
      $(".menu-toggle").click();
      next();
    });