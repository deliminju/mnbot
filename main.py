
import discord
import asyncio

client = discord.Client()

token = "ODA1MDU3NzQzODg2NjE0NTQ5.YBVWcw.aZOoHkUhCaZNhrPauNNtDWvQ1Z0"

@client.event
async def on_ready():

    print(client.user.name)
    print('하이이잇')
    game = discord.Game('헤헤헷헤헤헷')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content == "안녕":
        await message.channel.send("구래 안녕")
    if message.content == "찐세":
        await message.channel.send("핵쟁이")
    if message.content == "민준":
        await message.channel.send("며루치")
    if message.content == "찐세가 핵쟁이야?":
        await message.channel.send("웅 핵쟁이야")
    if message.content == "찐따는?":
        await message.channel.send("장세훈")
    if message.content == "비번":
        await message.channel.send("내놔")
    if message.content == "학춘아":
        await message.channel.send("뒤지고싶냐")
    if message.content == "뒤지고싶냐":
        await message.channel.send("아니용")

    if message.content =="민준앙탈":
        embed = discord.Embed(colour=discord.Colour.red(), title="ㅋㅋ", description="ㅎㅎ")
        embed.set_image(url="https://media.discordapp.net/attachments/802664221099556896/805082802856656916/Screenshot_2021-01-30_at_23.29.49.jpg")
        embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)








client.run(token)

