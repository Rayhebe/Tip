from highrise import BaseBot, User, SessionMetadata
from highrise.models import Position
from asyncio import run as arun

class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        try:
            await self.highrise.walk_to(Position(18., 0., .19, "FrontLeft"))
            await self.highrise.chat("Bot is now active!")
        except Exception as e:
            print(f"Error in on_start: {e}")

    async def on_user_join(self, user: User) -> None:
        print(f"{user.username} joined the room.")
        await self.highrise.send_whisper(user.id, f"Welcome {user.username}! Use '@mgbot command' for bot commands.")

    async def on_chat(self, user: User, message: str) -> None:
        try:
            _bid = "66be9396fdcc1589bbf8f297"  # Your bot user ID here
            _rid = "66d2726b2e80dd1f614c4dbb"  # Your room ID here
            
            # Check if the message is a whisper
            if user.id != _bid and message.startswith("/whisper"):
                target_user_id, *whisper_message = message.split()[1:]
                whisper_message = ' '.join(whisper_message)
                
                # Send the whispered message to the target user
                await self.highrise.send_whisper(target_user_id, whisper_message)
                await self.highrise.chat(f"Whispered to {target_user_id}: {whisper_message}")
                return

            # If the message starts with the bot's name, treat it as a command
            if message.lower().startswith(f"@mgbot"):
                user_message = message[len(f"@mgbot "):].strip()
                
                # Handle commands only from specific users
                if user.username in ["RayMG", "sh1n1gam1699"]:
                    await self.highrise.chat(f"{user.username}: {user_message}")
                else:
                    await self.highrise.send_whisper(user.id, "You do not have permission to use this command.")
                    
        except Exception as e:
            print(f"Error in on_chat: {e}")

if __name__ == "__main__":
    room_id = "66d2726b2e80dd1f614c4dbb"  # Your room ID here
    token = "432f23df3fc5076fe6c95ade994a533c9d473ecdb56acc31346899a94d6aaa6d"  # Your bot token here
    arun(Bot().start(room_id, token))  # Start the bot
