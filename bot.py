import discord
import os
from discord.ext import commands

token = os.getenv("TOKEN")

client = commands.Bot(command_prefix='!')
client.remove_command('help')

@client.event
async def on_ready():
    print("Bot is online")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("Role not found")
        await ctx.message.delete()

@client.command(aliases = ['rr'])
async def reload(ctx, extension = "None"):
    if extension == "None":
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                client.unload_extension(f'cogs.{filename[:-3]}')
                client.load_extension(f'cogs.{filename[:-3]}')
        await ctx.send("All cogs Reloaded")
    else:
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')
        await ctx.send(extension + " Reloaded")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)
