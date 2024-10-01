from highrise import BaseBot, User

async def handle_direct_message(bot: BaseBot, user: User, command: str) -> None:
    if command:
        # Display the user's command in the public chat
        await bot.highrise.chat(command)  # Send the command as a public message
