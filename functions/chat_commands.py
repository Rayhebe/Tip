async def handle_direct_message(bot, message: str) -> None:
    # Send the message to the public chat without revealing the command
    await bot.highrise.chat(message)
