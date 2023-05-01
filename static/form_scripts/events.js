const to_board_select = "board"
const board_form = "message_construct"
const canvas = new fabric.Canvas("edit_image_canvas");


async function onload_body(){
    await sleep(10);
    const image_input_obj = document.getElementById(ImgSrcManagement.image_source_select_id);
    ImgSrcManagement.update_input_option(image_input_obj);
}

async function sumbit_editied_image(event){
    event.preventDefault();
    console.log("submited!!");
    const canvas_to_hex = our_canvas.convert_to_hex();
    const chosen_board = document.getElementById(to_board_select).value;
    const form_path =document.getElementById(board_form).action;
    // add support to form upload.
    NetworkUtils.send_request(form_path, "POST", JSON.stringify({"image": canvas_to_hex, "destination":chosen_board}))

};


async function on_change_template(element_pointer){
    const current_template =element_pointer.value;
    if(current_template == 0){
        return;
    }
    const image_encoding = NetworkUtils.request_from_route("template/"+current_template);
    our_canvas.upload_image_to_canvas(image_encoding);
}


function add_text_to_canvas(event){
    event.preventDefault();
    const text = document.getElementById("text_on_image").value;
    our_canvas.add_text_to_canvas(text, {
        fill: 'black',
        moveCursor: 'pointer'
    });
}
generate_canvas();