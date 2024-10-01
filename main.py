import random
from highrise import BaseBot, User, Position
from highrise.models import SessionMetadata

class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("Bot started.")
        await self.highrise.walk_to(Position(4.0, 0.26, 3.5, "FrontRight"))

    async def on_user_join(self, user: User, position: Position) -> None:
        print(f"{user.username} joined the room.")
        await self.highrise.send_emote("dance-hipshake")

    async def on_chat(self, user: User, message: str) -> None:
        print(f"{user.username}: {message}")

        # Check if the message is a command directed to the bot
        if message.startswith("@MGBot"):
            # Remove the @MGBot part and handle the command
            command_message = message[len("@MGBot"):].strip()
            await self.handle_command(user, command_message)

        # Check for /whisper command
        elif message.startswith("/whisper"):
            whisper_message = message[len("/whisper"):].strip()
            await self.handle_command(user, whisper_message)

    async def handle_command(self, user: User, command_message: str) -> None:
        # Display the command message publicly in the room
        if command_message:
            await self.highrise.chat(command_message)

# Assuming you have other necessary bot initialization here
