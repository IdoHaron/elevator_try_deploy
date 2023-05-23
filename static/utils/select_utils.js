class SelectUtils{
    constructor(select_pointer){
        this.select_pointer = select_pointer;
    }
    remove_option(value) {
        // Get the select element by its id
        for (var i = 0; i < this.select_pointer.options.length; i++) {
            // If the option has the same value as the one to remove
            if (this.select_pointer.options[i].value == value) {
              // Remove the option from the select element
              this.select_pointer.removeChild(this.select_pointer.options[i]);
              // Break out of the loop
              break;
            }
        }
      }
      
}