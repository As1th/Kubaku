import os
from keep_alive import keep_alive
import discord
from discord.ext import commands, tasks

from discord.utils import get
from discord import Intents
TOKEN = os.environ['TOKEN']
intents = Intents.all()
client = discord.Client(intents=intents)

# This sends or updates an embed message with a description of the roles.

   
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

#@client.event
#async def on_member_join(member):
#    await member.create_dm()
#    await member.dm_channel.send(
#        f'Hi {member.name}, welcome to my Discord server!'
#    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.id == 844899391793659954:
        if message.content.startswith('!roles'):
            embedvar = discord.Embed(title="React to this message to get your roles!",
                                     description="Click the corresponding emoji to receive your role.\n<:WarThunder:"
                                                 "745425772944162907> - War Thunder\n<:Apex:745425965764575312> - "
                                                 "Apex\n<:ModernWarfare:757104623738814554> - "
                                                 "Modern Warfare\n<:Minecraft:757029546632413346> - "
                                                 "Minecraft\n<:R6Siege:757030019909550122> - R6 Siege", color=0x00ff00)
            await message.channel.send(embed=embedvar)
            print("Changed message embed color.")
        elif message.content.startswith('update'):
            embedvar2 = discord.Embed(title="React to this message to get your roles!",
                                      description="Click the corresponding emoji to receive your role.\n<:WarThunder:"
                                                  "745425772944162907> - War Thunder\n<:Apex:745425965764575312> - "
                                                  "Apex\n<:ModernWarfare:757104623738814554> - "
                                                  "Modern Warfare\n<:Minecraft:757029546632413346> - "
                                                  "Minecraft\n<:R6Siege:757030019909550122> - R6 Siege\n"
                                                  "<:AmongUs:760192601625591859> - Among Us", color=0x00ff00)
            channel = client.get_channel(844899391793659954)
            msg = await channel.fetch_message(757114312413151272)
            await msg.edit(embed=embedvar2)
            print("Updated role reaction message.")
    else:
        return

    if message.content.startswith('!Kubaku') or message.content.startswith('!kubaku') or message.content.startswith('!KUBAKU'):
        await message.channel.send("Hi!\nWant me to do something for you? I can:\n"
        "``!greenlist`` - Display a list of common feature requests are confirmed and planned to be added.\n"
        "``!redlist`` - Display a list of common feature requests that will NOT be in the game due to various restrictions.\n")
        return

    exc = ":octagonal_sign:  *Excavation System* - Unfortunately far too much work to implement a custom system for this, especially since a GBA excavation system would lack the touch screen that made the original so immersive. A system like in Pokemon D/P/Pt's 'Underground' would honestly get very tedious to have to do at every dig, and is more trouble than it's worth."
    awk = ":octagonal_sign:  *Awakening System* - Similar to excavation, would be a lot of custom work with no way to make a 'fun' system inside these limitations. Would also mean creating and storing an item for every fossil, which is more trouble and memory consuming than it's worth."
    cp = ":octagonal_sign:  *Custom Parts* - I chose Custom Colours over Custom Parts. As cool as Parts are, the small and low-quality sprites in the game work much better with simple colour changes. Some Custom Parts are so small that you wouldn't even know what you were looking at in the mess of pixels. Palette changes are much nicer to look at without real sprite artists. Also avoiding adding both Parts and Colours together (for similar reasons as adding a second Custom Colour)."
    cc2 = ":octagonal_sign:  *Custom Color 2* - Adding another form for each Spectrobe would be an exponential amount of work and would slow down developement considerably. With over 100 species planned, 300 forms is a bit too pressing both in time and memory. It would also require different Chroma minerals being mapped to different CCs, whereas the current solution is simple and unintrusive internally."
    origins = ":octagonal_sign:  *Spectrobes from Origins* - Mainly due to sprites. The 3D quality of the DS models translate 'acceptably' into sprites due to their low polys and colours, but the Wii models would look worse. I would also prefer to limit scope here anyway. This a demake of Spec1, so I think the handful of BtP Spectrobes are enough of a bonus."

    if message.content.startswith('!greenlist'):
        embedvar = discord.Embed(title="**The Green Feature List**",
                                     description="This is a list of common feature requests that are already confirmed and planned to be added eventually!\n\n"
":white_check_mark:  *Every Spec1 Spectrobe and Krawl*\n"
":white_check_mark:  *Full Story + Postgame Geo Vortexes*\n"
":white_check_mark:  *A more notable use of Minerals (EV training via Minerals, with altered data values and a way to actually see EVs)*\n"
":white_check_mark:  *Incubation System (Based on Daycare System)*", color=0x00ff00)
        await message.channel.send(embed=embedvar)
        return
      
    if message.content.startswith('!redlist'):
        if message.content.startswith('!redlist EXC') or message.content.startswith('!redlist exc') :
           await message.channel.send(exc)
           return
        elif message.content.startswith('!redlist AWK') or message.content.startswith('!redlist awk') :
           await message.channel.send(awk)
           return
        elif message.content.startswith('!redlist CP') or message.content.startswith('!redlist cp') :
           await message.channel.send(cp)
           return
        elif message.content.startswith('!redlist CC2') or message.content.startswith('!redlist cc2') :
           await message.channel.send(cc2)
           return
        elif message.content.startswith('!redlist ORIGINS') or message.content.startswith('!redlist origins') :
           await message.channel.send(origins)
           return
        elif message.content.startswith('!redlist ALL') or message.content.startswith('!redlist all'):
          embedvar = discord.Embed(title="**The Red Feature List**",
                                     description="This is a list of features that are NOT planned to be implemented. Discussion of these is still welcome, but most are barred due to scope and other unavoidable restrictions.\n\n"+exc+"\n"+awk+"\n"+cp+"\n"
          +cc2+"\n"
          +origins, color=0xfe0000)
          await message.channel.send(embed=embedvar)
          return
          
        else:
          embedvar = discord.Embed(title="**The Red Feature List**",
                                     description="This is a list of features that are NOT planned to be implemented. Discussion of these is still welcome, but most are barred due to scope and other unavoidable restrictions.\n"
                                     "**(See pinned messages for all explanations).**\n\n"
":octagonal_sign:  *Excavation System* - ``!redlist EXC`` for why.\n"                                    
":octagonal_sign:  *Awakening System* - ``!redlist AWK`` for why.\n"
":octagonal_sign:  *Custom Parts* - ``!redlist CP`` for why.\n"
":octagonal_sign:  *Custom Color 2* - ``!redlist CC2`` for why.\n"
":octagonal_sign:  *Spectrobes from Origins* - ``!redlist ORIGINS`` for why.", color=0xfe0000)
          await message.channel.send(embed=embedvar)
          return 
# Assign the role when the role is added as a reaction to the message.
@client.event
async def on_raw_reaction_add(payload):
    guild = client.get_guild(payload.guild_id)
    member = get(guild.members, id=payload.user_id)
    # channel and message IDs should be integer:
    if payload.channel_id == 844899391793659954 and payload.message_id == 757114312413151272:
        if str(payload.emoji) == "<:Apex:745425965764575312>":
            role = get(payload.member.guild.roles, name='Apex')
        elif str(payload.emoji) == "<:WarThunder:745425772944162907>":
            role = get(payload.member.guild.roles, name='War Thunder')
        elif str(payload.emoji) == "<:ModernWarfare:757104623738814554>":
            role = get(payload.member.guild.roles, name='Modern Warfare')
        elif str(payload.emoji) == "<:R6Siege:757030019909550122>":
            role = get(payload.member.guild.roles, name='R6 Siege')
        elif str(payload.emoji) == "<:Minecraft:757029546632413346>":
            role = get(payload.member.guild.roles, name='Minecraft')
        elif str(payload.emoji) == "<:AmongUs:760192601625591859>":
            role = get(payload.member.guild.roles, name='Among Us')
        else:
            role = get(guild.roles, name=payload.emoji)

        if role is not None:
            await payload.member.add_roles(role)
            print(f"Assigned {member} to {role}.")


# Assign the role when the role is added as a reaction to the message.
@client.event
async def on_raw_reaction_remove(payload):
    guild = client.get_guild(payload.guild_id)
    member = get(guild.members, id=payload.user_id)
    if payload.channel_id == 844899391793659954 and payload.message_id == 757114312413151272:
        if str(payload.emoji) == "<:Apex:745425965764575312>":
            role = get(guild.roles, name='Apex')
        elif str(payload.emoji) == "<:WarThunder:745425772944162907>":
            role = get(guild.roles, name='War Thunder')
        elif str(payload.emoji) == "<:ModernWarfare:757104623738814554>":
            role = get(guild.roles, name='Modern Warfare')
        elif str(payload.emoji) == "<:R6Siege:757030019909550122>":
            role = get(guild.roles, name='R6 Siege')
        elif str(payload.emoji) == "<:Minecraft:757029546632413346>":
            role = get(guild.roles, name='Minecraft')
        elif str(payload.emoji) == "<:AmongUs:760192601625591859>":
            role = get(guild.roles, name='Among Us')
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji)

        if role is not None:
            await member.remove_roles(role)
            print(f"Removed {role} from {member}.")
    
    

keep_alive()
client.run(os.getenv('TOKEN'))