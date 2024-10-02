import os
from highrise import *
from highrise import BaseBot, Position
from highrise.models import SessionMetadata, User

# Create the bot class
class Bot(BaseBot):
    # This method is triggered when the bot starts
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("mgbot is online")
        # Optional: Move the bot to a specific position in the room
        await self.highrise.walk_to(Position(3.0, 0.25, 1.5, "FrontRight"))

    # This method handles whispers (private messages) sent to the bot
    async def on_user_whisper(self, user: User, message: str) -> None:
        # List of allowed users who can issue commands (RayMG and sh1n1gam1699)
        allowed_users = ["RayMG", "sh1n1gam1699"]

        # Check if the user is allowed to send commands
        if user.username in allowed_users:
            # Check if the message starts with '!', indicating it's a command
            if message.startswith("!"):
                command = message[1:].strip()  # Remove the '!' and any extra spaces

                # Bot will broadcast the command in the public room
                await self.highrise.send_message(command)

# Run the bot when the script is executed
if __name__ == "__main__":
    bot = Bot()
    bot.run()
