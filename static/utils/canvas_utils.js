class CanvasUtils{
    
    constructor(canvas_pointer){
        this.canvas_pointer = canvas_pointer;
        this.context = this.canvas_pointer.getContext ('2d');
    }

    upload_image(image_encoding){
        // create a new image object
        var image = new Image ();
        // set the image source
        image.src = image_encoding;
        // wait for the image to load
        image.onload = () => {
        // draw the image on the canvas at the given coordinates
            this.context.drawImage (image, 0, 0, this.canvas_pointer.width, this.canvas_pointer.height);
        };
    }
    clearCanvas () {
        this.context.clearRect (0, 0, this.canvas_pointer.width, this.canvas_pointer.height);
      }      
}