import discord
from discord.ext import commands
from datetime import datetime
from colorama import Fore
from discord.voice_client import VoiceClient
from asyncio import coroutine, run
import time

def get_time():
    return ('\033[1m' + Fore.LIGHTMAGENTA_EX + datetime.now().strftime("%H:%M:%S") + Fore.WHITE)

bot = commands.Bot(command_prefix=">")
bot.remove_command("help")

@bot.event
async def on_ready():
    print(f"{get_time()}{Fore.LIGHTGREEN_EX} [+] Bot started")

@bot.command(pass_context=True)
async def scare(ctx):
    print(f"{get_time()}{Fore.WHITE} [+] Jumpscare executing...")
    channel = ctx.message.author.voice.channel
    print(f"{get_time()}{Fore.WHITE} [+] Getting the channel...")
    vc = await channel.connect()
    print(f"{get_time()} [+] Connected to the channel")
    print(f"{get_time()} [+] Playing the sound...")
    vc.play(discord.FFmpegPCMAudio('sound.mp3'))
    while vc.is_playing():
        time.sleep(1)
    await vc.disconnect()
    print(f"{get_time()} [+] Left the channel")
    print(f"{get_time()} {Fore.LIGHTGREEN_EX} [+] Sucessfuly pranked")


bot.run('YOUR-TOKEN')