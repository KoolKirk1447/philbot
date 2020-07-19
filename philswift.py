#when someone says "oof" or "f" or "oooofff" or anything like that, make it say 'Now THAT'S a lotta damage!'
#NzM0NDQyMDAyODM3NTM2ODU5.XxR0zw.WuGrTDcsjaglWpZ1BR5xeydFzc4
import discord 
from discord.ext import commands
import random
TOKEN = 'NzM0NDQyMDAyODM3NTM2ODU5.XxR0zw.WuGrTDcsjaglWpZ1BR5xeydFzc4'

client = discord.Client()

description = '''This is the help menu for Kool Kirk's Private bot'''
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
        await message.channel.send('''```This is the help section of Kool Kirk's Phil Swift Bot

Ping    Pings me

Info    show information about this bot

Oof     THAT'S ALOT OF DAMAGE (don't need prefix)

Tape    Flex tape

Paste    Flex Paste

Space   Phil in Space

Glue    Flex Glue

Fix     Fixes your server```''')
        
    if message.content.startswith('phelp'):
        await message.channel.send('''```This is the help section of Kool Kirk's Phil Swift Bot

Ping    Pings me

Info    show information about this bot

Oof     THAT'S ALOT OF DAMAGE (don't need prefix)

Tape    Flex tape

Paste    Flex Paste

Space   Phil in Space

Glue    Flex Glue

Fix     Fixes your server```''')
###########################################################      
    if message.content.startswith('pcontact'):
        await message.channel.send('''```Kool Kirk's discord is: Kool Kirk#1447```
or you can goto his server https://discord.gg/fjRbXEZ
`To see Kool Kirk's connections type PConnnect`''')
        
    if message.content.startswith('Pcontact'):
        await message.channel.send('''```Kool Kirk's discord is: Kool Kirk#1447```
or you can goto his server https://discord.gg/fjRbXEZ
`To see Kool Kirk's connections type PConnnect`''')
        
    if message.content.startswith('pconnect'):
        await message.channel.send('''Youtube- https://www.youtube.com/channel/UCJMNCysMg4EvaeiQ_vSoxuw
Soundcloud- https://soundcloud.com/aaron-kirk-minecraftyman1''')
        
    if message.content.startswith('Pconnect'):
        await message.channel.send('''Youtube- https://www.youtube.com/channel/UCJMNCysMg4EvaeiQ_vSoxuw
Soundcloud- https://soundcloud.com/aaron-kirk-minecraftyman1''')
##########################################################
    if message.content.startswith('plog'):
        await message.channel.send('''```Phil Swift was created```''')

    if message.content.startswith('Plog'):
        await message.channel.send('''```Phil Swift was created```''')

    if message.content.startswith('Pversion'):
        await message.channel.send('''```I am running Version 1.0```
Type plog or Plog to see what was updated''')
        
    if message.content.startswith('pversion'):
        await message.channel.send('''```I am running Version 1.0```
Type plog or Plog to see what was updated''')
        
    if message.content.startswith('Pping'):
        await message.channel.send('''```Pong!```''')
        
    if message.content.startswith('pping'):
        await message.channel.send('''```Pong!```''')

    if message.content.startswith('pinfo'):
        await message.channel.send('''```here are the commands for information about the bot

Version    Show what version that I am running on

Log     Shows what was updated last

Contact    Show how you can contact Kool Kirk for problems or recommendations```''')
        
        
    if message.content.startswith('Pinfo'):
        await message.channel.send('''```here are the commands for information about the bot

Version    Show what version that I am running on

Log     Shows what was updated last

Contact    Show how you can contact Kool Kirk for problems or recommendations```''')
        
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