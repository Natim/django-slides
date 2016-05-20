from channels.routing import route

channel_routing = [
    route("http.request", "demo.consumers.http_consumer"),
    # route("websocket.receive", "demo.consumers.ws_echo"),
    route("websocket.receive", "demo.consumers.ws_message"),
    route("websocket.connect", "demo.consumers.ws_add"),
    route("websocket.disconnect", "demo.consumers.ws_disconnect"),
]
