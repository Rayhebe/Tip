async def handle_whisper_command(bot, user, message):
    # Check if the message starts with the whisper command
    if message.startswith("/whisper "):
        secret_message = message[len("/whisper "):]
        await bot.highrise.chat(secret_message)  # Sends the message to the room

    # No need for any additional checks for the bot mention, since it calls this function
