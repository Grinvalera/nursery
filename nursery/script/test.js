   $( function(){
          var Large = $(".prev_full a"), Thumbs = $(".prev_min a");
          Thumbs.hover(function(){
          Large.find("img").attr("src",$(this).attr("data-img"));
         Large.attr("href",$(this).attr("href"));
        });
    });