from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import snsApp.routing

application = ProtocolTypeRouter({
    'websocket' : AuthMiddlewareStack(URLRouter(snsApp.routing.websocket_urlpatterns))
})
