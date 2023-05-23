const screen_id = "screen_id"
const board_form = "message_construct"
const image_presentation = "timeslots"
const time_range_selector = document.getElementById("is_image_time_limited");
const canvas = new fabric.Canvas("edit_image_canvas");
const time_choosing_element = document.getElementById("image_time_limitation");


async function onload_body(){
    await sleep(10);
    const image_input_selector = document.getElementById(ImgSrcManagement.image_source_select_id);
    ImgSrcManagement.update_input_option(image_input_selector);
    change_visability_of_time_element(time_range_selector);
}
function string_to_dict_datetime(string_to_conv){
    console.log(string_to_conv);
    const [date, time, year] = string_to_conv.split(" ")
    const [day, month] = date.split("/")
    const [hour, minute] = time.split(":");
    const dict_t = {
        "day": day,
        "month": month,
        "year": year,
        "hour": hour,
        "minute": minute
    }
    console.log(dict_t);
    return dict_t;
}
async function sumbit_editied_image(event){
    event.preventDefault();
    console.log("submited!!");
    const canvas_to_hex = our_canvas.convert_to_hex();

    const chosen_board = document.getElementById(screen_id).innerText;
    const form_path =document.getElementById(board_form).action;
    const amount_of_time = document.getElementById(image_presentation).value;
    let image_date_range = time_choosing_element.value.split(" - ");
    image_date_range[0] = string_to_dict_datetime(image_date_range[0]);
    image_date_range[1] = string_to_dict_datetime(image_date_range[1]);
    let image;
    if (time_range_selector == "no"){
        image = JSON.stringify({
            "image_encoding": canvas_to_hex,
            "image_time": amount_of_time
       });
    }
    else{
        image = JSON.stringify({
            "image_encoding": canvas_to_hex,
            "image_time": amount_of_time,
            "datetime_range": image_date_range
       });
    }
    // add support to form upload.
    NetworkUtils.send_request(form_path, "POST", JSON.stringify({"image": image, "destination":chosen_board}))
    alert("Image added to screen")


};


function change_visability_of_time_element(element_pointer){
    if (element_pointer.value == "yes"){
        show_element(time_choosing_element)
    }
    else{
        hide_element(time_choosing_element);
    }
}



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