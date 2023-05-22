const canvas_manager = new CanvasUtils(document.getElementById("present_image"));
function on_load(){ ; };

function on_change_image(select_elemet){
    const current_image_id = select_elemet.value;
    const image_info = NetworkUtils.request_from_route("/image/"+current_image_id);
    // add to canvas based on enccoding
    // present other image data.
    canvas_manager.upload_image(image_info["encoding"]);
}

on_load();