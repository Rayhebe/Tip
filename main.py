import random
from highrise import BaseBot, User, Position
from highrise.models import SessionMetadata
from functions.chat_commands import handle_whisper_command

class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("Bot is working.")
        await self.highrise.walk_to(Position(4.0, 0.26, 3.5, "FrontRight"))

    async def on_user_join(self, user: User, position: Position) -> None:
        print(f"{user.username} joined the room.")
        await self.highrise.send_emote("dance-hipshake")

    async def on_chat(self, user: User, message: str) -> None:
        print(f"{user.username}: {message}")

        # Check if the message is a whisper command
        if message.startswith("/whisper "):
            await handle_whisper_command(self, user, message)

        # Check if the bot is mentioned directly
        elif message.startswith("@MGBot"):
            command_message = message[len("@MGBot "):].strip()
            await handle_whisper_command(self, user, command_message)

# Entry point for the bot
if __name__ == "__main__":
    bot = Bot()
    bot.run()
