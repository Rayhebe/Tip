import random
from highrise import BaseBot, User, Position
from highrise.models import SessionMetadata
from functions.chat_commands import handle_direct_message

class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("Bot is online.")
        await self.highrise.walk_to(Position(4.0, 0.26, 3.5, "FrontRight"))

    async def on_user_join(self, user: User, position: Position) -> None:
        print(f"{user.username} has joined the room.")
        await self.highrise.send_emote("dance-hipshake")

    async def on_chat(self, user: User, message: str) -> None:
        print(f"{user.username}: {message}")

        # Check for direct message commands
        if message.lower().startswith("@mgbot"):
            # Remove the @mgbot prefix and handle the message
            command = message[7:].strip()  # Get command after @mgbot
            await handle_direct_message(self, user, command)

# Create an instance of your bot
bot = Bot()
