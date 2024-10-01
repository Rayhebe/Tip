import random
from highrise import BaseBot, User, Position
from highrise.models import SessionMetadata
from functions.chat_commands import handle_direct_message

class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("Bot is starting.")
        await self.highrise.walk_to(Position(4.0, 0.26, 3.5, "FrontRight"))

    async def on_user_join(self, user: User, position: Position) -> None:
        print(f"{user.username} has joined the room.")

    async def on_chat(self, user: User, message: str) -> None:
        print(f"{user.username}: {message}")

        # Check if the message starts with the bot's name
        if message.lower().startswith("@mgbot"):
            # Remove the @MGBot part and handle the remaining message
            command_message = message[len("@mgbot"):].strip()
            await handle_direct_message(self, command_message)
