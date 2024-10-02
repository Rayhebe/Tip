from asyncio import run as arun
import time
from main import Bot  # Import the Bot class from main.py

class RunBot:
    room_id = "66d2726b2e80dd1f614c4dbb"  # Room ID
    bot_token = "202d7b11c3d00fe44e472d4c1b8ad9f4e3277e5fd03927d5cfab15532e9d8af8"  # Bot token

    def run_loop(self) -> None:
        while True:
            try:
                # Create an instance of the Bot and start it
                arun(Bot().start(self.room_id, self.bot_token))
            except Exception as e:
                print(f"Error: {e}")
                time.sleep(5)

if __name__ == "__main__":
    RunBot().run_loop()
