import discord
import asyncio
import pyaudio
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

TOKEN = 'your_bot_token_here'
client = discord.Client()

# PyAudio setup
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

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
            play_audio(voice_client)

def play_audio(voice_client):
    while True:  # You'll need to implement proper stopping conditions
        data = stream.read(CHUNK)
        voice_client.send_audio_packet(data)

client.run(TOKEN)
