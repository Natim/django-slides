from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from channels.routing import ProtocolTypeRouter, URLRouter, ChannelNameRouter

import chat.routing
import thumbnails.consumers as thumbnails_consumers


application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                chat.routing.websocket_urlpatterns
            )
        ),
    ),
    "channel": ChannelNameRouter({
        "thumbnails-generate": thumbnails_consumers.GenerateConsumer,
    }),
})
