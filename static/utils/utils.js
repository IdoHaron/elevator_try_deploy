function hide_element(element){
    element.style.display = "none";
}

function show_element(element){
    element.style.display = "";
}

function page_reload(){
    // check if internet connection works.
    if (NetworkUtils.ping_server())
        location.reload();
    console.log("tried to page reload");
}

const sleep = ms => new Promise(r => setTimeout(r, ms));
