const canvas_manager = new CanvasUtils(document.getElementById("present_image"));
const select_elemet = document.getElementById("image");
const select_manager = new SelectUtils(select_elemet);
function on_load(){ ; };

function on_change_image(){
    const current_image_id = select_elemet.value;
    const image_info = JSON.parse(NetworkUtils.request_from_route("image/"+current_image_id));
    console.log(image_info);
    // add to canvas based on enccoding
    // present other image data.
    canvas_manager.upload_image(image_info["image_encoding"]);
}

function remove_image(){
    const current_image_id = select_elemet.value;
    console.log("current_image_id: "+current_image_id);
    const board_id = document.getElementById("board").innerText;
    canvas_manager.clearCanvas();
    NetworkUtils.request_from_route("remove_image", "POST", {
        "destination": board_id,
        "image_id":current_image_id
    });
    select_manager.remove_option(current_image_id);
}

on_load();