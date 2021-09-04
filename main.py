import os
from keep_alive import keep_alive
import discord
TOKEN = os.environ['TOKEN']
client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
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
        elif message.content.startswith('!redlist ALL') or message.content.startswith('!redlist all') :
           await message.channel.send("**The Red Feature List**\n"
"This is a list of all the features that are NOT planned to be implemented. Discussion of these is still welcome, but most are barred due to scope and other unavoidable restrictions.\n\n")
           await message.channel.send(exc+"\n"+awk+"\n"+cp+"\n"
          +cc2+"\n"
          +origins
)
           return
          
        else:
           await message.channel.send("**The Red Feature List**\n"
"This is a list of all the features that are NOT planned to be implemented. Discussion of these is still welcome, but most are barred due to scope and other unavoidable restrictions.\n"
":octagonal_sign:  *Excavation System* - ``!redlist EXC`` for why.\n"
":octagonal_sign:  *Awakening System* - ``!redlist AWK`` for why.\n"
":octagonal_sign:  *Custom Parts* - ``!redlist CP`` for why.\n"
":octagonal_sign:  *Custom Color 2* - ``!redlist CC2`` for why.\n"
":octagonal_sign:  *Spectrobes from Origins* - ``!redlist ORIGINS`` for why."
)

keep_alive()
client.run(os.getenv('TOKEN'))