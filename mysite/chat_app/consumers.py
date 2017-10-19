# In consumers.py
from channels import Group

# Connected to websocket.connect
def ws_add(message):
    #import pdb;pdb.set_trace()
    print ("asd")
    # Accept the connection
    message.reply_channel.send({"accept": True})
    # Add to the chat group
    group_name = message.content['path'].split('/')[-1]
    Group(group_name).add(message.reply_channel)

# Connected to websocket.receive
def ws_message(message):
    # import pdb;pdb.set_trace()
    group_name = message.content['path'].split('/')[-1]
    Group(group_name).send({
        "text": message.content['text'],
    })

# Connected to websocket.disconnect
def ws_disconnect(message):
    Group("chat").discard(message.reply_channel)
