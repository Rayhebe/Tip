from highrise import User

async def handle_whisper_command(bot, user: User, message: str) -> None:
    if message.startswith("/whisper "):
        secret_message = message[len("/whisper "):]
        await bot.highrise.chat(secret_message)  # Sends the message to the room
