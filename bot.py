import discord
from discord.ext import commands
import aiohttp
import os

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix=commands.when_mentioned_or("g-"), intents=intents)
bot.help_command = False

@bot.event
async def on_ready():
  print("Ready!")

@bot.command()
async def help(ctx):
  await ctx.send("`ggl`")
  
@bot.command()
async def ggl(ctx, *, search):
  async with aiohttp.ClientSession() as session:
    async with session.get(f"https://www.googleapis.com/customsearch/v1?key={os.environ['API_KEY']}&cx=e367fa34ef717987e&q={search}") as resp:
      js = await resp.json()
    
      embed = discord.Embed(
        title = f"Search Results:",
        color = 0xFFFFF1
      )
      embed.add_field(
        name = js['items'][0]['title'],
        value = f"[{js['items'][0]['snippet'][:50]}...]({js['items'][0]['link']})"
      )
      embed.add_field(
        name = js['items'][1]['title'],
        value = f"[{js['items'][1]['snippet'][:50]}...]({js['items'][0]['link']})"
      )
      embed.add_field(
        name = js['items'][2]['title'],
        value = f"[{js['items'][2]['snippet'][:50]}...]({js['items'][0]['link']})"
      )
      embed.add_field(
        name = js['items'][3]['title'],
        value = f"[{js['items'][3]['snippet'][:50]}...]({js['items'][0]['link']})"
      )
      embed.add_field(
        name = js['items'][4]['title'],
        value = f"[{js['items'][5]['snippet'][:50]}...]({js['items'][0]['link']})"
      )
    
      await ctx.send(embed=embed)
    
bot.run(os.environ['DISCORD_TOKEN'])
