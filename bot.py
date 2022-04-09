import discord
from discord.ext import commands
import aiohttp
import os

bot = commands.Bot(command_prefix="g-")

@bot.event
async def on_ready():
  print("Ready!")
  
@bot.command()
async def ggl(ctx, *, search):
  async with aiohttp.ClientSession() as session:
    async with session.get(f"https://www.googleapis.com/customsearch/v1?key={os.envrion["API_KEY"]}&cx=e367fa34ef717987e&q={search}") as resp:
      js = resp.json()
    
      embed = discord.Embed(
        title = f"Search For {search.capitalize()}:",
        color = 0xFFFFF1
      )
      embed.add_field(
        name = js.items[0].title,
        value = f"[{js.items[0].snippet}]({js.items[0].link})"
      )
    
      await ctx.send(embed=embed)
    
bot.run(os.envrion["DISCORD_TOKEN"])
