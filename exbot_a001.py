# This example requires the 'message_content' intent.

import discord
from discord import app_commands
from discord.app_commands import *
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="/", intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@client.tree.command(name='hello', description='testing')  # 명령어 이름, 설명
@app_commands.describe(text1='쓸 내용', text2 = '번호') # 같이 쓸 내용들
async def hello(interaction: discord.Interaction, text1:str, text2:int):    # 출력
    await interaction.response.send_message(f'{interaction.user.mention} : {text1} : {text2}', ephemeral=True)

client.run('MTIyMTA2MDQ2ODg4MjUzODU4Nw.G1scZX.iNikqjR8bI5H8sW1GqHoDIcI6Gd0NMGltKro2g')
