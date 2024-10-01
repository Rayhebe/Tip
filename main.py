import random
from highrise import BaseBot, User, Position
from highrise.models import SessionMetadata
from functions.mod import kick_user, ban_user, mute_user, summon_user
from functions.chat_commands import ChatCommands  # Import the ChatCommands class

casa = [
    "I Marry You 💍", "Of course I do 💍❤️", "I don't want to 💍💔",
    "Of course I don't 💍💔", "I Love You Of course I marry you 💍"
]

class Bot(BaseBot):
    bot_name = "MGBot"  # Define the bot name

    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("working")
        await self.highrise.walk_to(Position(4.0, 0.26, 3.5, "FrontRight"))

    async def on_user_join(self, user: User, position: Position) -> None:
        print(f"{user.username} entrou na sala")
        await self.highrise.send_emote("dance-hipshake")
        await self.highrise.send_emote("emote-lust", user.id)

    async def on_chat(self, user: User, message: str) -> None:
        print(f"{user.username}: {message}")

        # Check if the message is a whisper from RayMG or sh1n1gam1699
        if user.username in ['RayMG', 'sh1n1gam1699'] and message.startswith("/whisper"):
            await ChatCommands.handle_whisper(self, user, message)  # Call the whisper handler
            return

        # Heart reaction logic
        if message.lower().startswith("heart"):
            parts = message.split("@")
            if len(parts) == 1:  # No @username, just "heart" command (self heart)
                await self.heart(user, user, 1)  # Default 1 heart for self
            else:  # "heart@<username> <number>"
                await self.heart_for_user(user, parts)

        # Clap reaction logic
        elif message.lower().startswith("clap"):
            parts = message.split("@")
            if len(parts) == 1:  # No @username, just "clap" command (self clap)
                await self.clap(user, user, 1)  # Default 1 clap for self
            else:  # "clap@<username> <number>"
                await self.clap_for_user(user, parts)

        # Moderation commands for mods
        if user.username in ['RayMG', 'sh1n1gam1699', 'mod']:  # Adjust the mod list as needed
            if message.startswith("!kick "):
                parts = message.split(" ")
                if len(parts) == 2:
                    target_user_id = parts[1]
                    await kick_user(self, user, target_user_id)

            elif message.startswith("!ban "):
                parts = message.split(" ")
                if len(parts) == 2:
                    target_user_id = parts[1]
                    await ban_user(self, user, target_user_id)

            elif message.startswith("!mute "):
                parts = message.split(" ")
                if len(parts) == 2:
                    target_user_id = parts[1]
                    await mute_user(self, user, target_user_id)

            elif message.startswith("!summon "):
                parts = message.split(" ")
                if len(parts) == 2:
                    target_user_id = parts[1]
                    await summon_user(self, user, target_user_id)

    async def heart(self, sender: User, target: User, num_hearts: int) -> None:
        for _ in range(num_hearts):
            await self.highrise.react("heart", target.id)

    async def heart_for_user(self, user: User, parts: list) -> None:
        target_username = parts[1].split(" ")[0].strip()  # Get the target username
        num_hearts = 1  # Default to 1 heart

        if len(parts[1].split(" ")) > 1:  # If a number of hearts is specified
            try:
                num_hearts = int(parts[1].split(" ")[1].strip())
            except ValueError:
                await self.highrise.chat("Invalid number of hearts.")
                return

        room_users = await self.highrise.get_room_users()
        target_user = None

        # Find the specified user in the room
        for room_user, _ in room_users.content:
            if room_user.username.lower() == target_username.lower():
                target_user = room_user
                break

        if target_user:
            await self.heart(user, target_user, num_hearts)
            await self.highrise.chat(f"{user.username} sent {num_hearts} hearts to {target_user.username}!")
        else:
            await self.highrise.chat(f"User '{target_username}' not found in the room.")

    async def clap(self, sender: User, target: User, num_claps: int) -> None:
        for _ in range(num_claps):
            await self.highrise.react("clap", target.id)

    async def clap_for_user(self, user: User, parts: list) -> None:
        target_username = parts[1].split(" ")[0].strip()  # Get the target username
        num_claps = 1  # Default to 1 clap

        if len(parts[1].split(" ")) > 1:  # If a number of claps is specified
            try:
                num_claps = int(parts[1].split(" ")[1].strip())
            except ValueError:
                await self.highrise.chat("Invalid number of claps.")
                return

        room_users = await self.highrise.get_room_users()
        target_user = None

        # Find the specified user in the room
        for room_user, _ in room_users.content:
            if room_user.username.lower() == target_username.lower():
                target_user = room_user
                break

        if target_user:
            await self.clap(user, target_user, num_claps)
            await self.highrise.chat(f"{user.username} clapped for {target_user.username} {num_claps} times!")
        else:
            await self.highrise.chat(f"User '{target_username}' not found in the room.")
