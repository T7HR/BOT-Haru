import os
import discord
from discord.ext import commands
from discord import app_commands

from myserver import server_on

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())



# //////////////////// Bot Event /////////////////////////
# คำสั่ง bot พร้อมใช้งานแล้ว
@bot.event
async def on_ready():
    print("Bot Online!")
    synced = await bot.tree.sync()
    print(f"{len(synced)} command(s)")


# แจ้งคนเข้า -ออกเซิฟเวอร์


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1235863937938100247) # IDห้อง
    text = f"Welcome **{str(member)}** to Server **{member.guild.name}**"

    emmbed = discord.Embed(title = 'Welcome to the server!',
                           description = text,
                           color = 0x0015FF)

    await channel.send(text) # ส่งข้อความไปที่ห้องนี้
    await channel.send(embed = emmbed)  # ส่ง Embed ไปที่ห้องนี้
    await member.send(text) # ส่งข้อความไปที่แชทส่วนตัวของ member
    embed.set_author(name=str(member), icon_url=member.avatar_url)


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1235863937938100247)  # IDห้อง
    text = f"{member.name} has left the server!"
    await channel.send(text)  # ส่งข้อความไปที่ห้องนี้


# คำสั่ง chatbot
@bot.event
async def on_message(message):
    mes = message.content # ดึงข้อความที่ถูกส่งมา
    if mes == 'ฮาโหล':
        await message.channel.send("โหลควยไร") # ส่งกลับไปที่ห้องนั่น

    elif mes == '555':
        await message.channel.send("ยาอ่อน")

    await bot.process_commands(message)
    # ทำคำสั่ง event แล้วไปทำคำสั่ง bot command ต่อ


@bot.event
async def on_message(message):
    mes = message.content # ดึงข้อความที่ถูกส่งมา
    if mes == 'ฮารุ':
        await message.channel.send("201031") # ส่งกลับไปที่ห้องนั่น

    await bot.process_commands(message)


# ///////////////////// Commands /////////////////////
# กำหนดคำสั่งให้บอท

@bot.command()
async def hello(ctx):
    await ctx.send(f"hello {ctx.author.name}!")


@bot.command()
async def ขอมูล(ctx):
    await ctx.send(f"hello {ctx.author.name}!")


@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)


# Slash Commands
@bot.tree.command(name='hellobot', description='Replies with Hello')
async def hellocommand(interaction):
    await interaction.response.send_message("555")


@bot.tree.command(name='พิมพ์ตาม', description='พิมพ์ตามที่เราใส่')
@app_commands.describe(name = "ใส่ข้อความที่จะให้บอทพิมพ์ตาม")
async def namecommand(interaction, name : str):
    await interaction.response.send_message(f"{name}")


# Embeds


@bot.tree.command(name='กฏหมอ', description='กฏหมอทั้งหมด')
async def test1(interaction):
    emmbed = discord.Embed(title='Link', url="https://docs.google.com/spreadsheets/d/15Y3MvtGqrZkf9SzLRwJwOk5Z7xGs_ahyx_9Sq8V_CSQ/edit?usp=sharing", description='This is an embed that will show how to build an embed and the different components', color=0x66FFFF, timestamp= discord.utils.utcnow())

    
    await interaction.response.send_message(embed = emmbed)




@bot.tree.command(name='help', description='กฎหมอทั้งหมด')
async def helpcommand(interaction):
    emmbed = discord.Embed(title='Click Link', url='https://docs.google.com/spreadsheets/d/15Y3MvtGqrZkf9SzLRwJwOk5Z7xGs_ahyx_9Sq8V_CSQ/edit?gid=588131081#gid=588131081', 
                           description='Bot Commands',
                           color=0x66FFFF,
                           timestamp= discord.utils.utcnow())


    # ใส่ข้อมูล

    emmbed.set_author(name='Highest', url='https://discord.gg/highest', icon_url='https://media.discordapp.net/attachments/1226563343389556836/1226563460612231228/logo2.png?ex=66779efd&is=66764d7d&hm=9734c98d26eafc1a52ca8b668049ce7eee5bbf73f9391bbf94fc9b7c8b1ccf1b&=&format=webp&quality=lossless')

    # ใส่รูปเล็ก-ใหญ่
    emmbed.set_image(url='https://media.discordapp.net/attachments/1226563343389556836/1226979365854904482/500.gif?ex=6677d0d4&is=66767f54&hm=17ad2a5d72dd2a9f4a3a76bddaf7eed074c26037114f75fe310d07b354eacefe&=&width=350&height=350')

    # Footer เนื้อหาส่วนท้าย
    emmbed.set_footer(text='วันที่')

    await interaction.response.send_message(embed = emmbed)

server_on()

bot.run(os.getenv('TOKEN'))
