from channels.routing import route
from chat_app.consumers import ws_add, ws_message, ws_disconnect

channel_routing = [
    route("websocket.add", ws_add),
    route("websocket.receive", ws_message),
    route("websocket.disconnect", ws_disconnect),
    route("websocket.connect", ws_add, path=r"^/chat/"),

]
