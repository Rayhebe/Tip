from highrise import BaseBot, User, SessionMetadata
from highrise.models import Position
from asyncio import run as arun

class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        try:
            await self.highrise.walk_to(Position(18., 0., .19, "FrontLeft"))
            await self.highrise.chat("LOADING...")
        except Exception as e:
            print(f"Error in on_start: {e}")

    async def on_chat(self, user: User, message: str):
        try:
            _bid = "66be9396fdcc1589bbf8f297"  # Your bot user ID here
            _rid = "66d2726b2e80dd1f614c4dbb"  # Your room ID here
            _id = f"1_on_1:{_bid}:{user.id}"
            _idx = f"1_on_1:{user.id}:{_bid}"

            # Check if the message is from RayMG or sh1n1gam1699
            if user.username.lower() in ["raymg", "sh1n1gam1699"]:
                # If the message starts with the bot's name, treat it as a command
                if message.lower().startswith(f"@mghbot"):
                    user_message = message[len(f"@mghbot "):].strip()
                    # Send the message to the public room as if the user said it
                    await self.highrise.chat(f"{user.username}: {user_message}")
                
        except Exception as e:
            print(f"Error in on_chat: {e}")

# No need to run the bot here, it will be managed by run.py
