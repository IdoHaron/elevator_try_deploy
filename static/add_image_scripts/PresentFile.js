
class UserFileUpload{
    static file_upload_id = "user_image";
    static async on_file_upload(pointer_to_file, type){
        switch(type){
            case "image":
                console.log("present image");
                // ImageUploadManagement.on_file_upload(pointer_to_file);
                const file = pointer_to_file.files[0];
                console.log(file);
                const file_reader_instance = new FileReader();
                file_reader_instance.readAsDataURL(file);
                file_reader_instance.onload = function() {
                    const image_to_present = file_reader_instance.result;
                    our_canvas.upload_image_to_canvas(image_to_present);
                };
                break;
            case "video":
                console.log("present video");
                VideoUploadManagement.on_file_upload(pointer_to_file);
                break;
                
        }
    }

    static async submit(event, type, file_element_pointer, file_data, destination_board){
        const file_pointer = document.getElementById(file_element_pointer);
        switch(type){
            case "image":
                break;
        
            case "video":
                const file = file_pointer.files[0];
                const reader = new FileReader();
                const file_content = reader.readAsDataURL(file);
                reader.onload = ()=>{
                    const full_req =Object.assign({}, file_data, {
                        "destination":destination_board,
                        "encoding": reader.result
                    });
                    console.log(full_req);
                    NetworkUtils.request_from_route("add_video", "POST", JSON.stringify(full_req));
                }
                break;
        }
    }
}

