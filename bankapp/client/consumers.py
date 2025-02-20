import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("✅ WebSocket connection requested")  # Debugging
        await self.accept()
        print("✅ WebSocket connection established")  # Debugging
        await self.send(text_data=json.dumps({"message": "Welcome to WebSocket!"}))

    async def disconnect(self, close_code):
        print(f"❌ WebSocket disconnected with code: {close_code}")  # Debugging

    async def receive(self, text_data):
        print(f"📩 Raw data received: {text_data}")  # Debugging raw WebSocket data
        
        data = json.loads(text_data)
        message = data.get("message", "")
        
        print(f"📨 Processed message from user: {message}")  # Debugging message
        
        # Echo the message back
        await self.send(text_data=json.dumps({"message": message}))

