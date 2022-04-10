import discord
from discord.ext import commands
import aiohttp
import os

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
ntents.message_content = True

client = commands.Bot(command_prefix=commands.when_mentioned_or("g-"), intents=intents)
client.help_command = None

@client.event
async def on_ready():
  print("Ready!")

@client.command()
async def help(ctx):
  await ctx.send("`ggl`")
  
@client.command()
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
        value = f"[{js['items'][0]['snippet'][:50]}...]({js['items'][0]['link']})",
        inline = False
      )
      embed.add_field(
        name = js['items'][1]['title'],
        value = f"[{js['items'][1]['snippet'][:50]}...]({js['items'][0]['link']})",
        inline = False
      )
      embed.add_field(
        name = js['items'][2]['title'],
        value = f"[{js['items'][2]['snippet'][:50]}...]({js['items'][0]['link']})",
        inline = False
      )
      embed.add_field(
        name = js['items'][3]['title'],
        value = f"[{js['items'][3]['snippet'][:50]}...]({js['items'][0]['link']})",
        inline = False
      )
      embed.add_field(
        name = js['items'][4]['title'],
        value = f"[{js['items'][5]['snippet'][:50]}...]({js['items'][0]['link']})",
        inline = False
      )
    
      await ctx.send(embed=embed)
  
      
client.run(os.environ['DISCORD_TOKEN'])
