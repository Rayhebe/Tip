from flask import Flask
from threading import Thread
from asyncio import run as arun
import time
from importlib import import_module
from highrise.__main__ import BotDefinition, main  # Ensure this import is correct

class WebServer:
    def __init__(self):
        self.app = Flask(__name__)

        @self.app.route('/')
        def index() -> str:
            return "Bot is running!"

    def run(self) -> None:
        self.app.run(host='0.0.0.0', port=8084)

    def keep_alive(self):
        t = Thread(target=self.run)
        t.start()

class RunBot:
    room_id = "66d2726b2e80dd1f614c4dbb"
    bot_token = "202d7b11c3d00fe44e472d4c1b8ad9f4e3277e5fd03927d5cfab15532e9d8af8"
    bot_file = "main"
    bot_class = "Bot"

    def __init__(self) -> None:
        try:
            # Dynamically import the Bot class from main.py
            bot_class = getattr(import_module(self.bot_file), self.bot_class)
            self.definitions = [
                BotDefinition(bot_class(), self.room_id, self.bot_token)
            ]
        except ImportError as e:
            print(f"ImportError: {e}")
            self.definitions = None  # Ensure this is handled gracefully
        except AttributeError as e:
            print(f"AttributeError: {e}")
            self.definitions = None
        except Exception as e:
            print(f"Unexpected error during bot definition setup: {e}")
            self.definitions = None

    def run_loop(self) -> None:
        if not self.definitions:
            print("No bot definitions were initialized. Exiting.")
            return  # Exit if there was an error during setup

        while True:
            try:
                arun(main(self.definitions))
            except Exception as e:
                print("Error running the bot: ", e)
                time.sleep(5)

if __name__ == "__main__":
    WebServer().keep_alive()
    RunBot().run_loop()
