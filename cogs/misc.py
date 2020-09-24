import discord
from discord.ext import commands

class Misc(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        e = discord.Embed(title = '__**AMONG US COMMANDS**__', description = 'List of commands', colour = discord.Colour.from_rgb(198, 17, 17))
        e.add_field(name = "Game Commands", value = "`!code <server code> <server region(optional)(defaault is **ASIA**)>` : Displays the code in embedded text\n`!start` or `!s` : Mutes everyone **alive** in **Lobby**\n`!meet` or `!m` : Unmutes **alive** members\n`!dead @member` or `!d @member` : Declare **@member** dead\n`!over` or `!o` : Umnutes **everyone** in the game")
        await ctx.send(embed = e)


def setup(client):
    client.add_cog(Misc(client))
