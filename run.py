import sys
import os
import time
import traceback
from importlib import import_module
from highrise.__main__ import *

# BOT SETTINGS
bot_file_name = "main"
bot_class_name = "bot"
room_id = "66bad059afeca0c24b497205"
bot_token = "e6afc2ed8cbe059baa1c4420661e6b385e0d37c09a7697d2a6360e688fc636f7"

my_bot = BotDefinition(getattr(import_module(bot_file_name), bot_class_name)(), room_id, bot_token)

while True:
    try:
        definitions = [my_bot]
        arun(main(definitions))
    except Exception as e:
        print(f"An exception occurred: {e}")
        traceback.print_exc()
    time.sleep(5)
