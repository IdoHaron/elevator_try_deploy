
class UserFileUpload{
    static file_upload_id = "user_image";
    static async on_file_upload(pointer_to_file){
        const file = pointer_to_file.files[0];
        console.log(file);
        const file_reader_instance = new FileReader();
        file_reader_instance.readAsDataURL(file);
        file_reader_instance.onload = function() {
            const image_to_present = file_reader_instance.result;
            our_canvas.upload_image_to_canvas(image_to_present);
        };
    }
}

