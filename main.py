from highrise import (
    BaseBot,
    User,
    SessionMetadata,
)
from highrise.models import Position
from asyncio import run as arun

class Bot(BaseBot):

    async def on_start(self, SessionMetadata: SessionMetadata) -> None:
        try:
            await self.highrise.walk_to(Position(18., 0., .19, "FrontLeft"))
            await self.highrise.chat("LOADING...")
            print("Bot has entered the room successfully.")  # Log when the bot enters the room
        except Exception as e:
            print(f"Error in on_start: {e}")

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
                print(f"Command from {user.username}: {user_message}")  # Log commands
        except Exception as e:
            print(f"Error in on_chat: {e}")

    async def on_user_join(self, user: User) -> None:
        print(f"{user.username} joined the room.")  # Log when a user joins

if __name__ == "__main__":
    from functions.webserver import keep_alive  # Adjust the path if necessary
    keep_alive()  # Start the web server to keep the bot alive
    room_id = "66d2726b2e80dd1f614c4dbb"  # Room ID here
    token = "432f23df3fc5076fe6c95ade994a533c9d473ecdb56acc31346899a94d6aaa6d"  # Bot token here
    arun(Bot().run(room_id, token))
