from functions.webserver import keep_alive  # Adjust this if necessary
from main import Bot  # Ensure you're importing the Bot class from your main.py
from asyncio import run as arun

if __name__ == "__main__":
    keep_alive()  # Start the web server to keep the bot alive
    room_id = "66d2726b2e80dd1f614c4dbb"  # Your room ID
    token = "432f23df3fc5076fe6c95ade994a533c9d473ecdb56acc31346899a94d6aaa6d"  # Your token
    arun(Bot().run(room_id, token))  # Run the bot
