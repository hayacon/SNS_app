import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self): #connect user to websocket
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        #connect to the redis server
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code): #dis-connect from websocket
        #dis connect from the redis server
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )


    async def receive(self, text_data): #recieve data from user
        username = self.scope["user"].username
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        message = (username + ': ' + message)

        #send message to the chat room
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = self.scope["user"].username

        await self.send(text_data=json.dumps({
            'message':message,
            'username':username
        }))
