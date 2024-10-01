# List of mod users and vip users
mods = {"RayMG", "sh1n1gam1699"}  # Starting with RayMG and your friend
vips = set()  # VIP users

async def grant_mod(user_id: str, username: str):
    """Grant moderator rights to a user"""
    mods.add(username)
    return f"{username} has been granted moderator permissions."

async def grant_vip(user_id: str, username: str):
    """Grant VIP rights to a user"""
    vips.add(username)
    return f"{username} has been granted VIP permissions."

async def remove_vip(user_id: str, username: str):
    """Remove VIP rights from a user"""
    if username in vips:
        vips.remove(username)
        return f"{username} has been removed from VIP permissions."
    return f"{username} is not a VIP."
