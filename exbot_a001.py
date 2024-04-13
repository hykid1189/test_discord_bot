import discord
import socket
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 9999)
print('Start up on {} port {}'.format(*server_address))

while True:
    print('accept wait')
    # 클라이언트 접속 대기
    client_socket, client_address = server_socket.accept()

    try:
        # 클라이언트가 보낸 데이터 수령(1024byte)
        data = client_socket.recv(1024)
        # 문자열 치환
        data = data.decode()
    except Exception as err:  # 예외 발생 시
        # 클라이언트 소켓 연결 끊기
        client_socket.close()
        break
    finally:  # 모든 작업이 종료
        client_socket.close()
        break

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

bot.run('')
