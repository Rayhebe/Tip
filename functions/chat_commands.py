# functions/chat_commands.py

async def handle_direct_message(bot, user, command):
    """
    This function handles direct messages sent to the bot.
    """
    # Example: Bot will say the command publicly in the room
    if command:
        await bot.highrise.send_room_message(command)
    else:
        await bot.highrise.send_whisper(user.id, "I didn't understand the command.")
