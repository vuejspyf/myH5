function starMove(obj,attr,iTarget){
    clearInterval(obj.timer);
    obj.timer=setInterval(function(){
        var cur=parseInt(getStyle(obj,attr));
        var speed=(iTarget-cur)/6;
        speed=speed>0?Math.ceil(speed):
        Math.floor(speed);
        if(cur==iTarget){
            clearInterval(obj.timer);
        }
        else{
            obj.style[attr]=cur+speed+'px';
        }
    },30);
}