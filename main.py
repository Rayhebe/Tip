import random
from highrise import BaseBot, User, Position
from highrise.models import SessionMetadata
from functions.chat_commands import whisper_to_room

class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("Bot is working")
        await self.highrise.walk_to(Position(4.0, 0.26, 3.5, "FrontRight"))

    async def on_user_join(self, user: User, position: Position) -> None:
        print(f"{user.username} joined the room.")

    async def on_chat(self, user: User, message: str) -> None:
        print(f"{user.username}: {message}")

        # Check if the message is a whisper command to the bot
        if message.startswith(f"@{self.username}") or message.startswith("/whisper"):
            # Extract the message after the bot's name or command
            secret_message = message.split(" ", 1)[1] if " " in message else ""
            await whisper_to_room(self, secret_message)
