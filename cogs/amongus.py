import discord
from discord.ext import commands

class AmongUs(commands.Cog):
    needed_role = 757685585073930240
    voice_channel = 756415045981831193

    def __init__(self, client):
        self.client = client
        PLAYERS = []
        alive = []

    @commands.command(aliases = ['s'])
    @commands.has_role(needed_role)
    async def start(self, ctx):
        await ctx.message.delete()
        channel = self.client.get_channel(self.voice_channel)
        self.PLAYERS = channel.members
        self.alive = self.PLAYERS[:]
        if not self.alive:
            await ctx.send("The **Lobby** is Empty")
        else:
            for i in self.alive:
                try:
                    await i.edit(mute = True)
                except:
                    continue
            await ctx.send(f"**Game Started** *(by {ctx.author.name})*")

    @commands.command(aliases = ['d'])
    @commands.has_role(needed_role)
    async def dead(self, ctx, member : discord.Member):
        await ctx.message.delete()
        if member not in self.alive and member in self.PLAYERS:
            await ctx.send("**Member is already dead**")
        elif member.id in [mem.id for mem in self.alive]:
            await member.edit(mute = True)
            self.alive.remove(member)
            await ctx.send(f"**{member.mention} added to dead[]** (*by {ctx.author.name}*)")
        else:
            await ctx.send("**Member is not in the game**")

    @commands.command(aliases = ['m'])
    @commands.has_role(needed_role)
    async def meet(self, ctx):
        await ctx.message.delete()
        for i in self.alive:
            await i.edit(mute = False)
        await ctx.send(f"**Meeting Started** (*by {ctx.author.name}*)")

    @commands.command(aliases = ['o'])
    @commands.has_role(needed_role)
    async def over(self, ctx, msg = None):
        await ctx.message.delete()
        for i in self.PLAYERS:
            try:
                await i.edit(mute = False)
            except:
                continue
        self.alive = []
        PLAYERS = []
        await ctx.send(f"*Game Ended* (*by {ctx.author.name}*)")

    @commands.command()
    @commands.has_role(needed_role)
    async def reset(self, ctx):
        await ctx.message.delete()
        mem = ctx.guild.members
        for i in mem:
            try:
                await i.edit(mute = False)
                await ctx.send(i.mention + f"'s voice activity has bees resetted by **{ctx.author.name}**" )
            except:
                continue

    @commands.command()
    @commands.has_role(needed_role)
    async def code(self, ctx, c, *, server = 'ASIA'):
        await ctx.message.delete()
        embed = discord.Embed(title = "CODE", description = c.upper(), colour = discord.Colour.from_rgb(198, 17, 17))
        embed.add_field(name = "SERVER", value = server.upper())
        await ctx.send(embed = embed)


def setup(client):
    client.add_cog(AmongUs(client))
