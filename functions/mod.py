from highrise import User, BaseBot

async def kick_user(bot: BaseBot, user: User, target_user_id: str) -> None:
    target_username = await bot.get_username_by_id(target_user_id)
    if target_username:
        await bot.highrise.moderate_room(target_user_id, "kick")
        await bot.highrise.chat(f"{target_username} has been kicked from the room!")

async def ban_user(bot: BaseBot, user: User, target_user_id: str) -> None:
    target_username = await bot.get_username_by_id(target_user_id)
    if target_username:
        await bot.highrise.moderate_room(target_user_id, "ban")
        await bot.highrise.chat(f"{target_username} has been banned from the room!")

async def mute_user(bot: BaseBot, user: User, target_user_id: str) -> None:
    target_username = await bot.get_username_by_id(target_user_id)
    if target_username:
        await bot.highrise.chat(f"{target_username} has been muted!")

async def summon_user(bot: BaseBot, user: User, target_user_id: str) -> None:
    room_users = (await bot.highrise.get_room_users()).content
    for room_user, pos in room_users:
        if room_user.id == target_user_id:
            await bot.teleport(room_user, Position(3.0, 0.25, 1.5, "FrontRight"))
            await bot.highrise.chat(f"Summoned {room_user.username} to your position.")
            break
