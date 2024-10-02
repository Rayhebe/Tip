from highrise import *
from highrise import BaseBot, Position
from highrise.models import SessionMetadata

class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("Bot is online")
        # Move the bot to a specific position in the room if desired
        await self.highrise.walk_to(Position(3.0, 0.25, 1.5, "FrontRight"))

    async def on_user_whisper(self, user: User, message: str) -> None:
        # Check if the whisper message contains "mgbot"
        if "mgbot" in message.lower():
            # Remove the bot's name from the message and repeat the rest in the public room
            actual_message = message.lower().replace("mgbot", "").strip()

            # Bot repeats the message in the public room if there's something to say
            if actual_message:
                await self.highrise.send_message(actual_message)

    async def on_user_message(self, user: User, message: str) -> None:
        # Optional: you can keep this if you want to handle public messages separately
        pass
