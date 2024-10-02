from highrise import User

async def handle_whisper(user: User, message: str, bot) -> None:
    """
    Handle whispers sent to the bot and broadcast them to the room.
    """
    allowed_users = ["RayMG", "sh1n1gam1699"]  # Allowed users who can send messages
    if user.username in allowed_users:
        # Send the message to the room
        await bot.highrise.send_message(message)  # Broadcast the message to the room
