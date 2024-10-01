# functions/chat_commands.py

async def whisper(bot, user, message: str) -> None:
    # This function could be extended for different whisper handling
    await bot.highrise.chat(message)

async def direct_message(bot, user, message: str) -> None:
    # This function could handle direct messages differently if needed
    await bot.highrise.chat(message)
