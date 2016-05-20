from channels.routing import route


http_routing = [
    route("http.request", poll_consumer, path=r"^/poll/$", method=r"^POST$"),
]

chat_routing = [
    route("websocket.connect", chat_connect, path=r"^/(?P<room>[a-zA-Z0-9_]+)/$"),
    route("websocket.disconnect", chat_disconnect),
]

routing = [
    # You can use a string import path as the first argument as well.
    include(chat_routing, path=r"^/chat"),
    include(http_routing),
]
