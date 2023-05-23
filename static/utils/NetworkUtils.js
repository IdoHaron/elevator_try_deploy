class NetworkUtils{
    static xmlHttp = new XMLHttpRequest();
    static current_server_loc = window.location.origin;
    static current_server_route = window.location.href
    static send_request(server_and_route, request_type, request_content){
        NetworkUtils.xmlHttp.open(request_type, server_and_route, false);
        NetworkUtils.xmlHttp.send(request_content)
        return NetworkUtils.xmlHttp.responseText
    }
    
    static request_from_route(route, request_type, content){
        if (request_type === undefined){
            request_type = "GET"
        }
        if (content === undefined){
            content = null;
        }
        content = JSON.stringify(content);
        console.log(content);
        const wanted_route = NetworkUtils.current_server_loc + "/" + route
        return NetworkUtils.send_request(wanted_route, request_type, content);
    }

    static ping_server(){
        return NetworkUtils.request_from_route("route_to_ping")
    }
    static redirect_page(sub_path){
        window.location.replace(NetworkUtils.current_server_loc+"/"+sub_path)
    }
}

