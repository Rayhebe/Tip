import random
from highrise import BaseBot, User, Position
from highrise.models import SessionMetadata

class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("Bot is running")
        await self.highrise.walk_to(Position(4.0, 0.26, 3.5, "FrontRight"))

    async def on_user_join(self, user: User, position: Position) -> None:
        print(f"{user.username} joined the room")
        await self.highrise.send_emote("dance-hipshake")

    async def on_chat(self, user: User, message: str) -> None:
        print(f"{user.username}: {message}")

        # Check for direct message command
        if message.lower().startswith("@mgbot"):
            command_message = message[7:].strip()  # Remove the command prefix
            if command_message:  # Ensure there's something to respond with
                await self.highrise.chat(command_message)  # Broadcast the message to the room
            else:
                await self.highrise.chat("Please provide a message after @MGBot.")
