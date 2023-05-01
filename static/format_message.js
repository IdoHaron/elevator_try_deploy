/*
class NetworkUtils{
    static xmlHttp = new XMLHttpRequest();
    static current_server_route = window.location.href
    static send_request(server_and_route, request_type, request_content){
        NetworkUtils.xmlHttp.open(request_type, server_and_route, false);
        NetworkUtils.xmlHttp.send(request_content)
        return NetworkUtils.xmlHttp.responseText
    }
    
    static request_from_route(route){
        const wanted_route = NetworkUtils.current_server_route + "/" + route
        return NetworkUtils.send_request(wanted_route, "GET", null);
    }
}
*/

class TemplateMessage{
    constructor(message_template, message_content){
        this.message_content = message_content;
        this.message_template_name = message_template;
        this.template_encoding = this.#fetch_template(this.message_template_name )
    }

    #fetch_template(template_name){
        const route = "/template/"+template_name
        return NetworkUtils.request_from_route(route)
    }
    
}



function construct_TemplateMessage_obj() {
    const template = document.getElementsByName("template").value;
    const content = document.getElementsByName("content").value;
    return new TemplateMessage(template, content);
}

const tmp = construct_TemplateMessage_obj();

