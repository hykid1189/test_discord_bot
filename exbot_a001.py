import discord
from discord.ext import commands
import random as rd
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def AK47(ctx):
    await ctx.send('AK47! AK47!')

@bot.command()
async def random(ctx):
    await ctx.send(rd.randint(1,100))

bot.run('')
