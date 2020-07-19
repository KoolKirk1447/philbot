import discord 
from discord.ext import commands
import random
#enter your token at <your token here>
TOKEN = '<your token here>'

client = discord.Client()

description = '''Phil Swift here'''
bot = commands.Bot(command_prefix='!', description=description)


@bot.event
async def on_ready():
    activity = discord.Game(name='''Busy fixing servers with Flex Tape. Btw type Phelp for help''', type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print('YOU HAVE LOGGED IN SUCCESFULLY!')

@bot.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('oof'):
        await message.channel.send('''THAT'S ALOT OF DAMAGE''')
        
    if message.content.startswith('OOF'):
        await message.channel.send('''THAT'S ALOT OF DAMAGE''')
        
    if message.content.startswith('Oof'):
        await message.channel.send('''THAT'S ALOT OF DAMAGE''')
        
    if message.content.startswith('Phelp'):
        await message.channel.send('''```This is the help section of Phil Swift Bot

Ping    Pings me

Oof     THAT'S ALOT OF DAMAGE (don't need prefix)

Tape    Flex tape

Paste    Flex Paste

Space   Phil in Space

Glue    Flex Glue

Fix     Fixes your server```''')
        
    if message.content.startswith('phelp'):
        await message.channel.send('''```This is the help section of Phil Swift Bot

Ping    Pings me

Oof     THAT'S ALOT OF DAMAGE (don't need prefix)

Tape    Flex tape

Paste    Flex Paste

Space   Phil in Space

Glue    Flex Glue

Fix     Fixes your server```''')
        
    if message.content.startswith('Pping'):
        await message.channel.send('''```Pong!```''')
        
    if message.content.startswith('pping'):
        await message.channel.send('''```Pong!```''')
        
    if message.content.startswith('Ptape'):    
        await message.channel.send(file=discord.File('flextape.mp4'))
        
    if message.content.startswith('ptape'):    
        await message.channel.send(file=discord.File('flextape.mp4'))
        
    if message.content.startswith('Ppaste'):    
        await message.channel.send(file=discord.File('flexpaste.mp4'))
        
    if message.content.startswith('ppaste'):    
        await message.channel.send(file=discord.File('flexpaste.mp4'))
        
    if message.content.startswith('Pspace'):    
        await message.channel.send(file=discord.File('philspace.mp4'))
        
    if message.content.startswith('pspace'):    
        await message.channel.send(file=discord.File('philspace.mp4'))
        
    if message.content.startswith('Pglue'):    
        await message.channel.send(file=discord.File('flexglue.mp4'))
        
    if message.content.startswith('pglue'):    
        await message.channel.send(file=discord.File('flexglue.mp4'))
        ########
    if message.content.startswith('Pfix'):    
        await message.channel.send(file=discord.File('philfix.png'))
        
    if message.content.startswith('pfix'):    
        await message.channel.send(file=discord.File('philfix.png'))
        
        
bot.run(TOKEN)
