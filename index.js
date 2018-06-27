$(document).ready(function(){
 var collums=5;
 var rows=5;
 var wrap=$("#wrap")
 var w=wrap.width()/collums;
 var h=wrap.height()/rows;
 
 for(var r=0;r<rows;r++){
     for(var c=0;c<collums;c++){
    $('<li><div class="box"></div></li>').width(w);height(h)
    .css({
        "left":w*c+"px",
        "top":h*r+"px"
        "transform":"translateX("+(30*c+60)+"px)"
    })
    .appendTo(wrap);
     }
    

     
 }


});