from main import Bot
from functions.webserver import keep_alive
from asyncio import run as arun

if __name__ == "__main__":
    room_id = "66d2726b2e80dd1f614c4dbb"
    token = "432f23df3fc5076fe6c95ade994a533c9d473ecdb56acc31346899a94d6aaa6d"

    # Start the web server in a separate thread or process
    import threading

    # Define a function to run the web server
    def start_web_server():
        keep_alive()

    # Create and start a new thread for the web server
    web_server_thread = threading.Thread(target=start_web_server)
    web_server_thread.start()

    # Run the bot
    arun(Bot().run(room_id, token))
