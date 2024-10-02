from highrise import BaseBot, User, SessionMetadata
from highrise.models import Position
from asyncio import run as arun

class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("Bot started!")
        await self.highrise.walk_to(Position(18., 0., .19, "FrontLeft"))
        await self.highrise.chat("LOADING...")

    async def on_chat(self, user: User, message: str):
        try:
            _bid = "66be9396fdcc1589bbf8f297"  # Bot user ID
            _rid = "66d2726b2e80dd1f614c4dbb"  # Room ID
            _id = f"1_on_1:{_bid}:{user.id}"
            _idx = f"1_on_1:{user.id}:{_bid}"

            # Check if the message is private and from RayMG or sh1n1gam1699
            if user.username.lower() in ["raymg", "sh1n1gam1699"]:
                if message.lower().startswith(f"@mghbot"):
                    user_message = message[len(f"@mghbot "):].strip()
                    # Broadcast the private message to the room
                    await self.highrise.chat(f"{user.username}: {user_message}")
        except Exception as e:
            print(f"Error in on_chat: {e}")

if __name__ == "__main__":
    room_id = "66d2726b2e80dd1f614c4dbb"
    token = "202d7b11c3d00fe44e472d4c1b8ad9f4e3277e5fd03927d5cfab15532e9d8af8"
    arun(Bot().start(room_id, token))
