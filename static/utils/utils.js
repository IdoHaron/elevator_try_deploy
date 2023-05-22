function hide_element(element){
    element.style.display = "none";
}

function show_element(element){
    element.style.display = "";
}

const sleep = ms => new Promise(r => setTimeout(r, ms));

console.log("utils imported");