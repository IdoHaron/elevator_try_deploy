let try_text = null
class ImageCanvasManagement{
    static canvas_id = "edit_image_canvas"
    constructor(){
        this.pointer_to_canvas = new fabric.Canvas("edit_image_canvas");
    }

    clear_canvas(){
        this.pointer_to_canvas.clear();
        /*
        const context = canvas_pointer.getContext('2d');
        console.log("CLEAR!!!");
        context.clearRect(0, 0, canvas_pointer.width, canvas_pointer.height);
        */

    }
    resize_canvas(wanted_width, wanted_height) {
        this.pointer_to_canvas.setWidth(wanted_width);
        this.pointer_to_canvas.setHeight(wanted_height);
        /*
        canvas_pointer.width= wanted_width;
        canvas_pointer.height = wanted_height;
        */
    }
    convert_to_hex(){
        return document.getElementById(this.canvas_id).toDataURL();
    }

    upload_image_to_canvas(image_encoding){
        var img = new Image();
        const canvas = this.pointer_to_canvas
        canvas.uniformScaling = false;

        // When the image loads, set it as background image
        img.onload = function() {
            var f_img = new fabric.Image(img);
            // f_img.scaleToHeight(50);//canvas.height)
            //f_img.scaleToWidth(canvas.width)
            f_img.height = canvas.height;
            f_img.width = canvas.width;

            canvas.setBackgroundImage(f_img);

            canvas.renderAll();
        };
        img.src = image_encoding

        /*this.clear_canvas();
        this.pointer_to_canvas.setBackgroundImage(image_encoding, this.pointer_to_canvas.renderAll.bind(this.pointer_to_canvas), {
            height: this.pointer_to_canvas.height,
            width: this.pointer_to_canvas.width
         });*/ 
        /*
        const ctx = canvas_pointer.getContext("2d");
        var background = new Image();
        background.src = image_encoding;
        background.onload  = ()=>{
            ImageCanvasManagement.resize_canvas(canvas_pointer, background.naturalWidth, background.naturalHeight);
            ctx.drawImage(background, 0, 0);
        }*/
    }
    add_text_to_canvas(wanted_text, options){
        const text = new fabric.IText(wanted_text, options);
        try_text = text;
        this.pointer_to_canvas.add(text)
    }
}

let our_canvas = null;
async function generate_canvas(){
    our_canvas = new ImageCanvasManagement();
}

console.log("our canvas was created");