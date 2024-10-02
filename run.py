from asyncio import run as arun
import time
from highrise import main  # Ensure this is the right import for running the bot
from highrise import BotDefinition
from main import Bot

class RunBot:
    room_id = "66d2726b2e80dd1f614c4dbb"  # Room ID
    bot_token = "432f23df3fc5076fe6c95ade994a533c9d473ecdb56acc31346899a94d6aaa6d"  # Bot token

    def run_loop(self) -> None:
        while True:
            try:
                # Create an instance of the BotDefinition and pass it to the main method
                bot_definitions = [
                    BotDefinition(Bot(), self.room_id, self.bot_token)
                ]
                arun(main(bot_definitions))  # This should run the bot with the given definitions
            except Exception as e:
                print("Error: ", e)
                time.sleep(5)

if __name__ == "__main__":
    RunBot().run_loop()
