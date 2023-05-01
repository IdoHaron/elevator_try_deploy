import { NetworkUtils } from "./NetworkUtils"
import {RecurringEvent} from "./TimedEvents"
timeout_fetch = 10000
class ManageImages{
    static #images_route = "/img/"
    static #image_field_id = "shown_image"
    static #request_image(current_client_id){
        return NetworkUtils.request_from_route(ManageImages.#images_route +"/"+current_client_id)
    }
    static #apply_image(encoded_image){
        image_box = document.getElementById(ManageImages.#image_field_id);
        image_box.src = "data:image/png;base64," + encoded_image
    }
    static update_image(current_client_id){
        ManageImages.#apply_image(ManageImages.#request_image(current_client_id))
    }
}
function always_false(){
    return false;
}
RecurringEvent(ManageImages.update_image, timeout_fetch, always_false, -1);
