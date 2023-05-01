class NetworkUtils{
    static xmlHttp = new XMLHttpRequest();
    static current_server_loc = window.location.origin;
    static current_server_route = window.location.href
    static send_request(server_and_route, request_type, request_content){
        NetworkUtils.xmlHttp.open(request_type, server_and_route, false);
        NetworkUtils.xmlHttp.send(request_content)
        return NetworkUtils.xmlHttp.responseText
    }
    
    static request_from_route(route){
        const wanted_route = NetworkUtils.current_server_loc + "/" + route
        return NetworkUtils.send_request(wanted_route, "GET", null);
    }
}

