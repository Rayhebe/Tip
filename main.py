
from highrise import BaseBot, User, Position
from highrise.models import SessionMetadata
from functions.chat_commands import handle_whisper_command

class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("Bot is working.")

    async def on_chat(self, user: User, message: str) -> None:
        print(f"{user.username}: {message}")

        # Check if the message is a whisper command
        if message.startswith("/whisper "):
            await handle_whisper_command(self, user, message)

        # Check if the bot is mentioned directly
        elif message.startswith("@MGBot"):
            # Handle command after the bot's name
            command_message = message[len("@MGBot "):].strip()
            await handle_whisper_command(self, user, command_message)
