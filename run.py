from main import Bot
from asyncio import run as arun

if __name__ == "__main__":
    room_id = "66d2726b2e80dd1f614c4dbb"  # Your room ID here
    token = "432f23df3fc5076fe6c95ade994a533c9d473ecdb56acc31346899a94d6aaa6d"  # Your token here
    arun(Bot().run(room_id, token))
