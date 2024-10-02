from highrise import BaseBot, User, SessionMetadata
from highrise.models import Position
from asyncio import run as arun

class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        try:
            await self.highrise.walk_to(Position(18., 0., .19, "FrontLeft"))
            await self.highrise.chat("Bot is online and ready to receive messages!")
        except Exception as e:
            print(f"Error in on_start: {e}")

    async def on_chat(self, user: User, message: str):
        try:
            # Define your bot ID and room ID
            _bid = "66be9396fdcc1589bbf8f297"  # Your bot user ID here
            _rid = "66d2726b2e80dd1f614c4dbb"  # Your room ID here

            # Check if the message is a private message to the bot
            if message.lower().startswith(f"@mgbot"):
                user_message = message[len(f"@mgbot "):].strip()
                
                # Only allow the specified users to broadcast messages
                if user.username.lower() in ["raymg", "sh1n1gam1699"]:
                    await self.highrise.chat(f"Broadcast from {user.username}: {user_message}")
                else:
                    await self.highrise.send_whisper(user.id, "You do not have permission to use this command.")
                    
        except Exception as e:
            print(f"Error in on_chat: {e}")
