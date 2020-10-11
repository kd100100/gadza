function open_login(){
    document.getElementById("login_bg").style.zIndex=150;
    document.getElementById("login_box").style.zIndex=200;
}

function close_login(){
    document.getElementById("login_bg").style.zIndex=-150;
    document.getElementById("login_box").style.zIndex=-200;
}