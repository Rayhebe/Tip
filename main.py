async def on_chat(self, user: User, message: str):
    try:
        _bid = "66be9396fdcc1589bbf8f297"  # Your bot user ID here
        _rid = "66d2726b2e80dd1f614c4dbb"  # Your room ID here
        _id = f"1_on_1:{_bid}:{user.id}"
        _idx = f"1_on_1:{user.id}:{_bid}"

        # Check if the message is from RayMG or sh1n1gam1699
        if user.username.lower() in ["raymg", "sh1n1gam1699"]:
            # If the message starts with @mghbot, treat it as a command
            if message.lower().startswith(f"@mghbot"):
                # Strip the bot name and get the user message
                user_message = message[len(f"@mghbot "):].strip()

                # Broadcast the message in the public room
                await self.highrise.chat(f"{user.username}: {user_message}")
                
                # Optionally, log the event
                print(f"Broadcasted message from {user.username}: {user_message}")

    except Exception as e:
        print(f"Error in on_chat: {e}")
