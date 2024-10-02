from highrise import (
    BaseBot,
    User,
    SessionMetadata,
)
from highrise.models import Position
from asyncio import run as arun
from functions.webserver import keep_alive  # Updated import statement

class Bot(BaseBot):

    async def on_start(self, SessionMetadata: SessionMetadata) -> None:
        try:
            await self.highrise.walk_to(Position(18., 0., .19, "FrontLeft"))
            await self.highrise.chat("LOADING...")
        except Exception as e:
            print(f"error : {e}")

    async def on_chat(self, user: User, message: str):
        try:
            _bid = "66be9396fdcc1589bbf8f297"  # Your bot user ID here
            _id = f"1_on_1:{_bid}:{user.id}"
            _idx = f"1_on_1:{user.id}:{_bid}"
            _rid = "66d2726b2e80dd1f614c4dbb"  # Your room ID here

            # If the message starts with the bot's name, treat it as a command
            if message.lower().startswith(f"@mgbot"):
                user_message = message[len(f"@mgbot "):].strip()
                # Send the message to the public room as if the user said it
                await self.highrise.chat(f"{user.username}: {user_message}")
                
        except Exception as e:
            print(f"Error in on_chat: {e}")

if __name__ == "__main__":
    room_id = "66d2726b2e80dd1f614c4dbb"
    token = "432f23df3fc5076fe6c95ade994a533c9d473ecdb56acc31346899a94d6aaa6d"
    keep_alive()  # Start the web server
    arun(Bot().run(room_id, token))
