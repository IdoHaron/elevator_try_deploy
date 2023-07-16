// const canvas_manager = new CanvasUtils(document.getElementById("present_image"));
const select_elemet_id = "image";
const object_show_div_id = "show_obj";
let PROPERTIES = "";
function on_load(){ ; };

function selected_id() { return document.getElementById(select_elemet_id).value; }

function change_presented_object(obj_as_html) {document.getElementById(object_show_div_id).innerHTML = obj_as_html; }

function on_change_object(){
    const current_obj_id =  selected_id();
    const obbj_info = NetworkUtils.request_from_route("obj_as_html/"+current_obj_id);
    change_presented_object(obbj_info);
    // add to canvas based on enccoding
    // present other image data.
    /*
    canvas_manager.upload_image(image_info["image_encoding"]);

    const past_prop_table = document.getElementById("image_properties");
    if (past_prop_table!=null){
        past_prop_table.remove();
    }
    PROPERTIES= image_info["image_properties"];
    const property_table = show_image_properties(image_info["image_properties"], "image_properties");
    const selector_to_add_after = document.getElementById("present_image");
    selector_to_add_after.insertAdjacentHTML("afterend", property_table);
    // add here the append
    let container = document.getElementById("container");
    */

}

function clear_screen(){
    
}

function remove_obj(){
    const current_image_id = selected_id();
    console.log("current_image_id: "+current_image_id);
    const board_id = document.getElementById("board").innerText;
    change_presented_object("");
    NetworkUtils.request_from_route("remove_obj", "POST", {
        "destination": board_id,
        "image_id":current_image_id
    });
    page_reload();

    //select_manager.remove_option(current_image_id);
}

function show_image_properties(jsonData, table_id){
    
    // Get the keys of the first object as the table headers
    let keys = Object.keys(jsonData);

    if (keys.length === 0) {
        return "Invalid input";
    }

    // Start the table tag and add the header row
    let table = `<table id=${table_id} class="styled-tleab">`;
    table += "<tr class=\"active-row\">";
    for (let key of keys) {
        table += `<th>${key}</th>`;
    }
    table += "</tr>";

    // Loop through the JSON array and add each object as a table row
    for (let key of keys) {
        table += `<td>${jsonData[key]}</td>`;
    }

    // End the table tag and return the result
    table += "</table>";
    return table;
}

on_load();