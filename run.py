from highrise import BaseBot, User, SessionMetadata
from highrise.models import Position
from asyncio import run as arun
import importlib.util
import time

class RunBot():
    room_id = "66d2726b2e80dd1f614c4dbb"  # Room ID
    bot_token = "432f23df3fc5076fe6c95ade994a533c9d473ecdb56acc31346899a94d6aaa6d"  # Bot token
    bot_file = "main"
    bot_class = "Bot"

    def __init__(self) -> None:
        self.definitions = [
            BotDefinition(
                getattr(import_module(self.bot_file), self.bot_class)(),
                self.room_id, self.bot_token)
        ]

    def run_loop(self) -> None:
        while True:
            try:
                arun(main(self.definitions))

            except Exception as e:
                print("Error: ", e)
                time.sleep(5)

if __name__ == "__main__":
    RunBot().run_loop()
