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
        moveCursor: 'pointer',
        fontSize:40
    });
}
const canvas_height = window.innerHeight / 2;
const canvas_width = window.innerWidth / 2;
const canvas_element= document.getElementById("edit_image_canvas");
canvas_element.height = canvas_height;
canvas_element.width = canvas_width;
pointer_to_canvas_outside_ref = new fabric.Canvas("edit_image_canvas", {
    height: canvas_height,
    width: canvas_width
});
canvas.renderAll();

generate_canvas();

function add_image_to_canvas(image_encoding, fabric_canvas, wanted_width, wanted_height){
    var img = new Image();
    img.src = image_encoding;
    //img.sizes = (wanted_width,wanted_height)
    img.width = wanted_width;
    img.height = wanted_height;
    img.sizes = (wanted_width,wanted_height);
    img.onload = function() {
        var f_img = new fabric.Image(img);
        //f_img.scaleToWidth(wanted_width);
        let scale_width = wanted_width / f_img.width;
        let scale_height = wanted_height / f_img.height;
        f_img.set({
            scaleX: scale_width,
            scaleY: scale_height
        });
        
        fabric_canvas.setBackgroundImage(f_img);
        fabric_canvas.renderAll();
    };
}