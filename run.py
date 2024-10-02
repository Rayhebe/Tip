from main import Bot
from functions.webserver import keep_alive  # Ensure the path is correct
from asyncio import run as arun

if __name__ == "__main__":
    keep_alive()  # Start the web server to keep the bot alive
    room_id = "66d2726b2e80dd1f614c4dbb"  # Room ID here
    token = "432f23df3fc5076fe6c95ade994a533c9d473ecdb56acc31346899a94d6aaa6d"  # Bot token here

    try:
        arun(Bot().run(room_id, token))  # Start the bot
    except Exception as e:
        print(f"An error occurred while running the bot: {e}")
