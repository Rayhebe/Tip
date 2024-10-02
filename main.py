import os
import logging
from highrise import *
from highrise import BaseBot, Position
from highrise.models import SessionMetadata, User
from functions.whisper_handler import handle_whisper  # Import the whisper handler function

# Set up logging to capture errors
logging.basicConfig(level=logging.INFO)

# Create the bot class
class Bot(BaseBot):
    # This method is triggered when the bot starts
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        try:
            logging.info("mgbot is online")
            await self.highrise.walk_to(Position(3.0, 0.25, 1.5, "FrontRight"))  # Optional: Move to a position
        except Exception as e:
            logging.error(f"Error on start: {e}")

    # This method handles whispers (private messages) sent to the bot
    async def on_user_whisper(self, user: User, message: str) -> None:
        try:
            logging.info(f"Received whisper from {user.username}: {message}")
            # Call the function to handle the whisper
            await handle_whisper(user, message, self)  # Pass the bot instance to the handler
        except Exception as e:
            logging.error(f"Error in whisper handling: {e}")

# Run the bot when the script is executed
if __name__ == "__main__":
    bot = Bot()
    try:
        bot.run()
    except Exception as e:
        logging.error(f"Error running the bot: {e}")
