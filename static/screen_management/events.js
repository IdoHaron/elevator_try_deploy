const canvas_manager = new CanvasUtils(document.getElementById("present_image"));
const select_elemet = document.getElementById("image");
let PROPERTIES = "";
const select_manager = new SelectUtils(select_elemet);
function on_load(){ ; };

function on_change_image(){
    const current_image_id = select_elemet.value;
    const image_info = JSON.parse(NetworkUtils.request_from_route("image/"+current_image_id));
    console.log(image_info);
    // add to canvas based on enccoding
    // present other image data.
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

}

function clear_screen(){
    
}

function remove_image(){
    const current_image_id = select_elemet.value;
    console.log("current_image_id: "+current_image_id);
    const board_id = document.getElementById("board").innerText;
    canvas_manager.clearCanvas();
    NetworkUtils.request_from_route("remove_obj", "POST", {
        "destination": board_id,
        "image_id":current_image_id
    });
    select_manager.remove_option(current_image_id);
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