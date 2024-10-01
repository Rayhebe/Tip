from functions.mod import mods, vips, grant_mod, grant_vip, remove_vip
from highrise import User, Position

class MGBot:
    def __init__(self, highrise):
        self.highrise = highrise

    async def command_handler(self, user: User, message: str):
        parts = message.split(" ")
        command = parts[0][1:].lower()  # Get the command after the prefix (!)

        # Heart reaction handling
        if command.startswith("heart"):
            await self.handle_reaction(user, parts, "heart")

        # Clap reaction handling
        elif command.startswith("clap"):
            await self.handle_reaction(user, parts, "clap")

        # Moderation commands for mods
        if user.username in mods:
            if command == "mod" and len(parts) == 2:
                target_user_id = parts[1]
                target_username = await self.get_username_by_id(target_user_id)
                response = await grant_mod(target_user_id, target_username)
                await self.highrise.chat(response)

            elif command == "kick" and len(parts) == 2:
                target_user_id = parts[1]
                await self.kick_user(user, target_user_id)

            elif command == "ban" and len(parts) == 2:
                target_user_id = parts[1]
                await self.ban_user(user, target_user_id)

            elif command == "mute" and len(parts) == 2:
                target_user_id = parts[1]
                await self.mute_user(user, target_user_id)

            elif command == "summon" and len(parts) == 2:
                target_user_id = parts[1]
                await self.summon_user(user, target_user_id)

            elif command == "vip" and len(parts) == 2:
                target_user_id = parts[1]
                target_username = await self.get_username_by_id(target_user_id)
                response = await grant_vip(target_user_id, target_username)
                await self.highrise.chat(response)

            elif command == "vipremove" and len(parts) == 2:
                target_user_id = parts[1]
                target_username = await self.get_username_by_id(target_user_id)
                response = await remove_vip(target_user_id, target_username)
                await self.highrise.chat(response)

        # If the user is a VIP, allow only the summon command
        elif user.username in vips:
            if command == "summon" and len(parts) == 2:
                target_user_id = parts[1]
                await self.summon_user(user, target_user_id)
            else:
                await self.highrise.chat(f"Sorry, {user.username}, you do not have permission to use this command.")

        else:
            await self.highrise.chat(f"Sorry, {user.username}, you do not have permission to use this command.")

    async def handle_reaction(self, user: User, parts: list, reaction_type: str):
        if len(parts) == 2 and "@" in parts[1]:
            target_username = parts[1][1:]  # Remove '@'
            target_user_id = await self.get_user_id(target_username)
            if target_user_id:
                await self.highrise.react(reaction_type, target_user_id)
                await self.highrise.chat(f"Sent a {reaction_type} to {target_username}")
            else:
                await self.highrise.chat("User not found.")
        elif len(parts) == 3 and user.username in mods + ["RayMG", "sh1n1gam1699"]:
            target_username = parts[1][1:]
            target_user_id = await self.get_user_id(target_username)
            amount = int(parts[2])

            if target_user_id and amount <= 30:
                for _ in range(amount):
                    await self.highrise.react(reaction_type, target_user_id)
                await self.highrise.chat(f"Sent {amount} {reaction_type}s to {target_username}")
            else:
                await self.highrise.chat("Invalid amount or user not found.")
        else:
            await self.highrise.chat(f"Usage: !{reaction_type}@user.id or !{reaction_type}@user.id [1-30]")

    async def kick_user(self, user: User, target_user_id: str):
        try:
            await self.highrise.moderate_room(target_user_id, "kick")
            target_username = await self.get_username_by_id(target_user_id)
            await self.highrise.chat(f"{target_username} has been kicked from the room!")
        except Exception as e:
            await self.highrise.chat(f"Error while kicking: {e}")

    async def ban_user(self, user: User, target_user_id: str):
        try:
            await self.highrise.moderate_room(target_user_id, "ban")
            target_username = await self.get_username_by_id(target_user_id)
            await self.highrise.chat(f"{target_username} has been banned from the room!")
        except Exception as e:
            await self.highrise.chat(f"Error while banning: {e}")

    async def mute_user(self, user: User, target_user_id: str):
        target_username = await self.get_username_by_id(target_user_id)
        await self.highrise.chat(f"{target_username} has been muted!")

    async def summon_user(self, user: User, target_user_id: str):
        """Summon a user to the position of the current user"""
        try:
            room_users = (await self.highrise.get_room_users()).content
            requester_position = None
            for room_user, position in room_users:
                if room_user.id == user.id:
                    requester_position = position
                    break

            for room_user, position in room_users:
                if room_user.id == target_user_id:
                    await self.teleport(room_user, Position(requester_position.x, requester_position.y, requester_position.z + 1, requester_position.facing))
                    await self.highrise.chat(f"Summoned {room_user.username} to your position.")
                    break
        except Exception as e:
            await self.highrise.chat(f"Error while summoning: {e}")

    async def teleport(self, user: User, position: Position):
        try:
            await self.highrise.teleport(user.id, position)
        except Exception as e:
            await self.highrise.chat(f"Teleport Error: {e}")

    async def get_username_by_id(self, user_id: str) -> str:
        """Retrieve the username based on the user ID"""
        room_users = (await self.highrise.get_room_users()).content
        for room_user, pos in room_users:
            if room_user.id == user_id:
                return room_user.username
        return None

    async def get_user_id(self, username: str) -> str:
        """Retrieve the user ID based on the username"""
        room_users = (await self.highrise.get_room_users()).content
        for room_user, _ in room_users:
            if room_user.username.lower() == username.lower():
                return room_user.id
        return None
