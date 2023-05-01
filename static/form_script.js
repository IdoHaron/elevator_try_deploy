//implement constructors.

class ImageUploadManagement{
    static file_upload_id = "user_image";
    static async on_file_upload(pointer_to_file){
        const file = pointer_to_file.files[0];
        console.log(file);
        const file_reader_instance = new FileReader();
        file_reader_instance.readAsDataURL(file);
        file_reader_instance.onload = function() {
            const image_to_present = file_reader_instance.result;
            const image_canvas = document.getElementById(ImageCanvasManagement.pointer_to_canvas)
            ImageCanvasManagement.clear_canvas(image_canvas);
            const ctx = image_canvas.getContext("2d");
            var background = new Image();
            background.src = image_to_present;
            background.onload  = ()=>{
                ImageCanvasManagement.resize_canvas(image_canvas, background.naturalWidth, background.naturalHeight);
                ctx.drawImage(background, 0, 0);
            }
        };
    }
}

class ImgSrcManagement{
    static image_source_select_id = "template_or_user_image"

    static update_input_option(image_input_obj){
        console.log(image_input_obj);
        const image_input_type = image_input_obj.value;
        let current_value;
        console.log(image_input_obj.options);
        console.log(image_input_obj.options.length);
        let option;
        let element_to_hide;
        for (let i=0; i<image_input_obj.options.length; i++){
            option = image_input_obj.options[i]
            console.log(option);
            current_value = option.value
            if (option == undefined || current_value === image_input_type)
                continue;
            element_to_hide = document.getElementById(current_value);
            hide_element(element_to_hide);
        }
        show_element(document.getElementById(image_input_type));
        document.getElementById(image_input_type).value ="";
        const canvas_element = document.getElementById(ImageCanvasManagement.pointer_to_canvas)
        ImageCanvasManagement.clear_canvas(canvas_element);
} 
}

class ImageCanvasManagement{
    static pointer_to_canvas = "edit_image_canvas";
    static clear_canvas(canvas_pointer){
        const context = canvas_pointer.getContext('2d');
        console.log("CLEAR!!!");
        context.clearRect(0, 0, canvas_pointer.width, canvas_pointer.height);

    }
    static resize_canvas(canvas_pointer, wanted_width, wanted_height) {
        canvas_pointer.width= wanted_width;
        canvas_pointer.height = wanted_height;
    }
}


const sleep = ms => new Promise(r => setTimeout(r, ms));


async function onload(){
    await sleep(10);
    const image_input_obj = document.getElementById(ImgSrcManagement.image_source_select_id);
    ImgSrcManagement.update_input_option(image_input_obj);
}

async function sumbit_editied_image(){};