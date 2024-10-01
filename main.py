import random
from highrise import *
from highrise import BaseBot, Position
from highrise.models import SessionMetadata

casa = ["I Marry You 💍", "Of course I do 💍❤️", "I don't want to 💍💔", "Of course I don't 💍💔", "I Love You Of course I marry you 💍"]
mods = ["RayMG", "sh1n1gam1699"]  # Add moderator usernames here
vips = []  # Add VIP usernames here

class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("Bot is working")
        await self.highrise.walk_to(Position(3.0, 0.25, 1.5, "FrontRight"))

    async def on_user_join(self, user: User, position: Position | AnchorPosition) -> None:
        print(f"{user.username} entered the room")
        await self.highrise.send_whisper(user.id, f"❤️Welcome [{user.username}] Use: [!emote list] or [1-97] For Dances & Emotes")
        await self.highrise.send_whisper(user.id, f"❤️Use: [/help] For More Information.")
        await self.highrise.send_whisper(user.id, f"❤️.🤍.")
        await self.highrise.send_emote("dance-hipshake")
        await self.highrise.send_emote("emote-lust", user.id)

    async def on_chat(self, user: User, message: str) -> None:
        print(f"{user.username}: {message}")

        # Clap reaction logic with specified number of claps
        if message.lower().startswith("clap"):
            parts = message.split("@")

            if len(parts) == 1:  # No @username, just "clap" command (self clap)
                await self.clap(user, user, 1)  # Default 1 clap for self

            elif parts[1].strip().lower().startswith("all"):  # "clap@all <number>"
                await self.clap_for_all(user, parts)

            else:  # "clap@<username> <number>"
                await self.clap_for_user(user, parts)

        # Heart reaction logic
        elif message.lower().startswith("heart"):
            parts = message.split("@")

            if len(parts) == 1:  # No @username, just "heart" command (self heart)
                await self.heart(user, user, 1)  # Default 1 heart for self

            elif parts[1].strip().lower().startswith("all"):  # "heart@all <number>"
                await self.heart_for_all(user, parts)

            else:  # "heart@<username> <number>"
                await self.heart_for_user(user, parts)

        # Moderation commands for mods
        if user.username in mods:
            if message.startswith("!mod "):
                await self.handle_mod_commands(user, message)

            elif message.startswith("!kick "):
                await self.kick_user(user, message)

            elif message.startswith("!ban "):
                await self.ban_user(user, message)

            elif message.startswith("!mute "):
                await self.mute_user(user, message)

            elif message.startswith("!summon "):
                await self.summon_user(user, message)

    async def handle_mod_commands(self, user: User, message: str):
        parts = message.split(" ")
        if len(parts) == 2:
            target_user_id = parts[1]
            target_username = await self.get_username_by_id(target_user_id)
            if target_username:
                # Grant mod logic can be placed here
                await self.highrise.chat(f"{target_username} has been granted mod status.")

    async def kick_user(self, user: User, message: str) -> None:
        parts = message.split(" ")
        if len(parts) == 2:
            target_user_id = parts[1]
            target_username = await self.get_username_by_id(target_user_id)
            if target_username:
                await self.highrise.moderate_room(target_user_id, "kick")
                await self.highrise.chat(f"{target_username} has been kicked from the room!")

    async def ban_user(self, user: User, message: str) -> None:
        parts = message.split(" ")
        if len(parts) == 2:
            target_user_id = parts[1]
            target_username = await self.get_username_by_id(target_user_id)
            if target_username:
                await self.highrise.moderate_room(target_user_id, "ban")
                await self.highrise.chat(f"{target_username} has been banned from the room!")

    async def mute_user(self, user: User, message: str) -> None:
        parts = message.split(" ")
        if len(parts) == 2:
            target_user_id = parts[1]
            target_username = await self.get_username_by_id(target_user_id)
            await self.highrise.chat(f"{target_username} has been muted!")

    async def summon_user(self, user: User, message: str) -> None:
        parts = message.split(" ")
        if len(parts) == 2:
            target_user_id = parts[1]
            room_users = (await self.highrise.get_room_users()).content
            for room_user, pos in room_users:
                if room_user.id == target_user_id:
                    await self.teleport(room_user, Position(3.0, 0.25, 1.5, "FrontRight"))
                    await self.highrise.chat(f"Summoned {room_user.username} to your position.")
                    break

    async def clap_for_all(self, user: User, parts: list) -> None:
        room_users = await self.highrise.get_room_users()
        room_user = next((ru for ru, _ in room_users.content if ru.id == user.id), None)

        if room_user and (room_user.is_host or room_user.is_moderator):
            num_claps = 1
            if len(parts) > 1 and parts[1].strip().lower().split(" ")[-1].isdigit():
                num_claps = int(parts[1].strip().lower().split(" ")[-1])

            for room_user, _ in room_users.content:
                await self.clap(user, room_user, num_claps)

            await self.highrise.chat(f"{user.username} clapped for everyone {num_claps} times!")
        else:
            await self.highrise.chat("Only the host or a moderator can clap for everyone.")

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

    async def heart_for_all(self, user: User, parts: list) -> None:
        room_users = await self.highrise.get_room_users()
        room_user = next((ru for ru, _ in room_users.content if ru.id == user.id), None)

        if room_user and (room_user.is_host or room_user.is_moderator):
            num_hearts = 1
            if len(parts) > 1 and parts[1].strip().lower().split(" ")[-1].isdigit():
                num_hearts = int(parts[1].strip().lower().split(" ")[-1])

            for room_user, _ in room_users.content:
                await self.heart(user, room_user, num_hearts)

            await self.highrise.chat(f"{user.username} sent hearts to everyone {num_hearts} times!")
        else:
            await self.highrise.chat("Only the host or a moderator can send hearts for everyone.")

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
            if room_user.username.lower() == target_username.lower
