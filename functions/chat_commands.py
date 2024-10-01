from highrise import User

async def whisper_to_room(bot, message: str) -> None:
    # Send the message to the room as a public message
    await bot.highrise.chat(message)
