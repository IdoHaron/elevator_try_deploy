

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
        our_canvas.clear_canvas();
    } 
}

