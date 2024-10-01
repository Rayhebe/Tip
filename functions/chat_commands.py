from highrise import BaseBot, User

async def handle_whisper(bot: BaseBot, user: User, message: str) -> None:
    """
    Handle the /whisper command by sending the message to the room publicly.
    The original whisper command message will not be displayed in the chat log.
    """
    if message.lower().startswith("/whisper"):
        # Extract the message after the command
        secret_message = message[len("/whisper "):].strip()
        
        # Send the message to the room
        await bot.highrise.chat(secret_message)
