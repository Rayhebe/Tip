import streamlit as st
from main import Bot
from functions.webserver import keep_alive
from asyncio import run as arun

# Set up the Streamlit interface
st.title("Highrise Game Bot")
st.write("Starting the bot...")

if __name__ == "__main__":
    keep_alive()  # Start the web server to keep the bot alive
    room_id = "66d2726b2e80dd1f614c4dbb"  # Your room ID here
    token = "432f23df3fc5076fe6c95ade994a533c9d473ecdb56acc31346899a94d6aaa6d"  # Your bot token here

    try:
        st.write("Running bot...")
        arun(Bot().run(room_id, token))  # Start the bot
    except Exception as e:
        st.error(f"An error occurred while running the bot: {e}")
