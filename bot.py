import discord
import numpy as np
import sounddevice as sd
from dotenv import load_dotenv
import os
import asyncio
import sys

# Load environment variables
load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# Audio settings
samplerate = 44100  # Sample rate
channels = 2  # Adjust based on your needs
dtype = 'int16'  # Data type for the audio stream

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.content.startswith('!join'):
        channel = message.author.voice.channel
        if channel:
            voice_client = await channel.connect()
            await message.channel.send("Connected and now playing.")
            stream_audio(voice_client)

def callback(indata, frames, time, status):
    # This function will be called for each audio block captured
    if status:
        print(status, file=sys.stderr)
    # Convert the NumPy array to bytes and then stream it to Discord
    # Note: You might need to adjust this part based on Discord's requirements
    # This is a placeholder to illustrate the process
    audio_data = indata.tobytes()

def stream_audio(voice_client):
    with sd.InputStream(samplerate=samplerate, channels=channels, dtype=dtype, callback=callback):
        print("Streaming started...")
        # Keep the stream alive or perform other tasks here
        # You might need to adjust this logic to fit your application
        while True:
            asyncio.sleep(1)  # Prevent blocking

client.run(TOKEN)
