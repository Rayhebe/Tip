from highrise import *
from highrise import BaseBot, Position
from highrise.models import SessionMetadata

class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("Bot is online")
        # Move the bot to a specific position if needed
        await self.highrise.walk_to(Position(3.0, 0.25, 1.5, "FrontRight"))

    async def on_user_whisper(self, user: User, message: str) -> None:
        # When the bot receives a direct (private) message, repeat it in the public room
        await self.highrise.send_message(message)

