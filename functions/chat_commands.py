from highrise import BaseBot, User

class ChatCommands:
    @staticmethod
    async def handle_whisper(bot: BaseBot, user: User, message: str) -> None:
        # Extract the message part after the "/whisper" command
        broadcast_message = message[len("/whisper "):].strip()
        # Send the broadcast message as if the bot itself is speaking
        await bot.highrise.chat(f"{bot.bot_name} says: {broadcast_message}")
