# In routing.py
# from channels.routing import route
# channel_routing = [
#     route("http.request", "chat_app.consumers.http_consumer"),
# ]

from channels.routing import route
from chat_app.consumers import ws_add, ws_message, ws_disconnect

channel_routing = [
    route("websocket.connect", ws_add),
    route("websocket.receive", ws_message),
    route("websocket.disconnect", ws_disconnect),
]
