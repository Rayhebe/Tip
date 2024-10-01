# mod.py

from highrise import User, Position

# Existing mod and vip lists
mods = ["RayMG", "sh1n1gam1699"]
vips = []

async def grant_mod(user_id: str, username: str) -> str:
    mods.append(username)
    return f"{username} has been granted mod privileges."

async def remove_vip(user_id: str, username: str) -> str:
    if username in vips:
        vips.remove(username)
        return f"{username} has been removed from VIP status."
    return f"{username} is not a VIP."

async def grant_vip(user_id: str, username: str) -> str:
    if username not in vips:
        vips.append(username)
        return f"{username} has been granted VIP status."
    return f"{username} is already a VIP."

async def get_user_id(highrise, username: str) -> str:
    """Retrieve the user ID based on the username."""
    room_users = (await highrise.get_room_users()).content
    for room_user, position in room_users:
        if room_user.username.lower() == username.lower():
            return room_user.id
    return None
