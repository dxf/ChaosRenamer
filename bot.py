import discord
from config import token
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True  # Ensure bot can see members' nicknames

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.slash_command(name="rename", description="Rename a member.")
async def rename(ctx, member: discord.Member, new_nick: str):
    try:
        await member.edit(nick=new_nick)
        await ctx.respond(f"{member.mention}'s nickname has been changed to {new_nick}.")
    except:
        await ctx.respond(f"Failed to rename {member.mention}. @daf and tell him to do something about it")

bot.run(token)