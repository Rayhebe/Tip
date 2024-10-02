from highrise import *
from highrise import BaseBot, Position
from highrise.models import SessionMetadata

class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("Bot is online")
        # Move the bot to a specific position in the room if needed
        await self.highrise.walk_to(Position(3.0, 0.25, 1.5, "FrontRight"))

    async def on_user_whisper(self, user: User, message: str) -> None:
        # Check if the message is a command you want the bot to handle
        # You can add command filtering here if necessary
        if message.startswith("!"):
            # This is where you can handle the commands
            command = message[1:].strip()  # Remove the '!' and any extra spaces
            
            # Example: Broadcast the command publicly
            await self.highrise.send_message(command)
