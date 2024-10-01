from highrise import BaseBot, User, Position
from highrise.models import SessionMetadata

class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("Bot is online.")
        await self.highrise.walk_to(Position(4.0, 0.26, 3.5, "FrontRight"))

    async def on_chat(self, user: User, message: str) -> None:
        # Ignore messages from the bot itself
        if user.username == "MGBot":
            return

        # Check for direct message to the bot
        if message.startswith("@MGBot "):
            # Extract the message after @MGBot
            direct_message = message[len("@MGBot "):].strip()
            if direct_message:  # Ensure there is a message to send
                await self.highrise.chat(direct_message)  # Display the message in public
            return  # Exit the function to avoid further processing

# Create an instance of the bot class and run it
