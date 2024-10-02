import os
import logging
from highrise import *
from highrise import BaseBot, Position
from highrise.models import SessionMetadata, User

# Set up logging to capture errors
logging.basicConfig(level=logging.INFO)

class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        try:
            logging.info("mgbot is online")
            # You can remove the walk_to command if it causes issues
            await self.highrise.walk_to(Position(3.0, 0.25, 1.5, "FrontRight"))
        except Exception as e:
            logging.error(f"Error on start: {e}")

    async def on_user_whisper(self, user: User, message: str) -> None:
        try:
            logging.info(f"Received whisper from {user.username}: {message}")
            allowed_users = ["RayMG", "sh1n1gam1699"]
            if user.username in allowed_users:
                if message.startswith("!"):
                    command = message[1:].strip()
                    logging.info(f"Command to execute: {command}")
                    await self.highrise.send_message(command)
                    logging.info("Message sent to room.")
        except Exception as e:
            logging.error(f"Error in whisper handling: {e}")

if __name__ == "__main__":
    bot = Bot()
    try:
        bot.run()
    except Exception as e:
        logging.error(f"Error running the bot: {e}")
