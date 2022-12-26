import translators as ts
import discord
from discord.ext import commands
import nest_asyncio
nest_asyncio.apply()
ts.[translator] #select the translator

intents = discord.Intents.all() 
client = discord.Client()

@client.event
async def on_ready():
    # Prints a message when the bot is online and functioning
    await client.change_presence(status=discord.Status.online, activity = discord.Game(name=f"Let's join Community-GameFi NFT HolyShxxt! 🥳 🎉 Currently in {len(client.guilds)} servers! 🎉"))
    print('Ready to translate!')

@client.event
async def on_reaction_add(reaction, user): 
    emojiid = reaction.emoji.encode('unicode-escape') #encode the emoji
    print(emojiid)
    if reaction.count == 1: #if there is new emoji after starting the bot
      
#Japanese 
        if emojiid == b'\\U0001f1ef\\U0001f1f5': #if reacted emoji is Japan 
            phrase = reaction.message.content
            trans_ja = ts.[translator](phrase, to_language='ja')
            await reaction.message.channel.send(trans_ja)

#English
        if emojiid == b'\\U0001f1fa\\U0001f1f8': #if reacted emoji is US
            phrase = reaction.message.content
            trans_en = ts.[translator](phrase, to_language='en')
            await reaction.message.channel.send(trans_en)


#Chinese
        if emojiid == b'\\U0001f1ed\\U0001f1f0': #if reacted emoji is HK 
            phrase = reaction.message.content
            trans_hk = ts.[translator](phrase, to_language='zh-TW')
            await reaction.message.channel.send(trans_hk)

#Korean
        if emojiid == b'\\U0001f1f0\\U0001f1f7': #if reacted emoji is Korea 
            phrase = reaction.message.content
            trans_ko = ts.[translator](phrase, to_language='ko')
            await reaction.message.channel.send(trans_ko)

#Spanish
        if emojiid == b'\\U0001f1ea\\U0001f1f8': #if reacted emoji is Spain 
            phrase = reaction.message.content
            trans_es = ts.[translator](phrase, to_language='es')
            await reaction.message.channel.send(trans_es)
            
#Portuguese 
        if emojiid == b'\\U0001f1f5\\U0001f1f9': #if reacted emoji is Portugual  
            phrase = reaction.message.content
            trans_pt = ts.[translator](phrase, to_language='pt')
            await reaction.message.channel.send(trans_pt)

client.run([Token])

