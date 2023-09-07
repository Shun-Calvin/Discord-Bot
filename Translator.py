#Thanks to @1ntegrale9

import translators as ts
import translators.server as tss
import discord
from discord.ext import commands
import nest_asyncio
nest_asyncio.apply()

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    # Prints a message when the bot is online and functioning
    await client.change_presence(status=discord.Status.online, activity = discord.Game(name=f"Let's join Community-GameFi NFT HolyShxxt! 🥳 🎉 Currently in {len(client.guilds)} servers! 🎉"))
    print('Ready to translate!')

@client.event
async def on_reaction_add(reaction, user):
    print("emoji-id")
    emojiid = reaction.emoji.encode('unicode-escape')
    print(emojiid)
    if reaction.count == 1:
#Japanese 
        if emojiid == b'\\U0001f1ef\\U0001f1f5':
            tss.google
            phrase = reaction.message.content
            trans_ja = tss.google(phrase, to_language='ja')
            tran = discord.Embed(color = 0x2ecc71)
            print(reaction.message.author.name)
            tran.set_author(name = f'Translation Result ')
            tran.add_field(name= f'Raw text from {reaction.message.author.name}', value = phrase, inline = False)
            tran.add_field(name= f'Result  🇯🇵', value = trans_ja, inline = False)
            tran.set_footer(text = f'Translator Bot From HolyShxxt Community')
            await reaction.message.channel.send(embed = tran)
            tran.remove_field(index=1)
            tran.remove_field(index=0)

#English
        if emojiid == b'\\U0001f1fa\\U0001f1f8':
            tss.google
            phrase = reaction.message.content
            trans_en = tss.google(phrase, to_language='en')
            tran = discord.Embed(color = 0x2ecc71)
            tran.set_author(name = f'Translation Result')
            tran.add_field(name= f'Raw text from {reaction.message.author.name}', value = phrase, inline = False)
            tran.add_field(name= f'Result  🇺🇸', value = trans_en, inline = False)
            tran.set_footer(text = f'Translator Bot From HolyShxxt Community')
            await reaction.message.channel.send(embed = tran)
            tran.remove_field(index=1)
            tran.remove_field(index=0)


#TraditionalChinese
        if emojiid == b'\\U0001f1f9\\U0001f1fc':
            tss.google
            phrase = reaction.message.content
            trans_hk = tss.google(phrase, to_language='zh')
            tss.bing
            trans_hk = tss.google(trans_hk, to_language='zh-TW')
            tran = discord.Embed(color = 0x2ecc71)
            tran.set_author(name = f'Translation Result ')
            tran.add_field(name= f'Raw text from {reaction.message.author.name}', value = phrase, inline = False)
            tran.add_field(name= f'Result 🇹🇼 ', value = trans_hk, inline = False)
            tran.set_footer(text = f'Translator Bot From HolyShxxt Community')
            await reaction.message.channel.send(embed = tran)
            tran.remove_field(index=1)
            tran.remove_field(index=0)

#Korean
        if emojiid == b'\\U0001f1f0\\U0001f1f7':
            phrase = reaction.message.content
            tss.google
            trans_ko = tss.google(phrase, to_language='ko')
            tran = discord.Embed(color = 0x2ecc71)
            tran.set_author(name = f'Translation Result ')
            tran.add_field(name= f'Raw', value = phrase, inline = False)
            tran.add_field(name= f'Result 🇰🇷 ', value = trans_ko, inline = False)
            tran.set_footer(text = f'Translator Bot From HolyShxxt Community')
            await reaction.message.channel.send(embed = tran)
            tran.remove_field(index=1)
            tran.remove_field(index=0)

#Spanish
        if emojiid == b'\\U0001f1ea\\U0001f1f8':
            phrase = reaction.message.content
            tss.google
            trans_es = tss.google(phrase, to_language='es')
            tran = discord.Embed(color = 0x2ecc71)
            tran.set_author(name = f'Translation Result ')
            tran.add_field(name= f'Raw text from {reaction.message.author.name}', value = phrase, inline = False)
            tran.add_field(name= f'Result 🇪🇸 ', value = trans_es, inline = False)
            tran.set_footer(text = f'Translator Bot From HolyShxxt Community')
            await reaction.message.channel.send(embed = tran)
            tran.remove_field(index=1)
            tran.remove_field(index=0)
            
#Portuguese 
        if emojiid == b'\\U0001f1f5\\U0001f1f9':
            phrase = reaction.message.content
            trans_pt = tss.google(phrase, to_language='pt')
            tss.google
            tran = discord.Embed(color = 0x2ecc71)
            tran.set_author(name = f'Translation Result')
            tran.add_field(name= f'Raw text from {reaction.message.author.name}', value = phrase, inline = False)
            tran.add_field(name= f'Result  🇵🇹 ', value = trans_pt, inline = False)
            tran.set_footer(text = f'Translator Bot From HolyShxxt Community')
            await reaction.message.channel.send(embed = tran)
            tran.remove_field(index=1)
            tran.remove_field(index=0)

#SimplifiedChinese 
        if emojiid == b'\\U0001f1e8\\U0001f1f3':
            phrase = reaction.message.content
            tss.google
            trans_zh = tss.google(phrase, to_language='zh')
            tran = discord.Embed(color = 0x2ecc71)
            tran.set_author(name = f'Translation Result')
            tran.add_field(name= f'Raw text from {reaction.message.author.name}', value = phrase, inline = False)
            tran.add_field(name= f'Result  🇨🇳', value = trans_zh, inline = False)
            tran.set_footer(text = f'Translator Bot From HolyShxxt Community')
            await reaction.message.channel.send(embed = tran)
            tran.remove_field(index=1)
            tran.remove_field(index=0)

#Cantonese 
        if emojiid == b'\\U0001f1ed\\U0001f1f0':
            phrase = reaction.message.content
            tss.bing
            trans = tss.bing(phrase, to_language='yue')
            trans_ca = tss.google(trans, to_language='zh-TW')
            tran = discord.Embed(color = 0x2ecc71)
            tran.set_author(name = f'Translation Result')
            tran.add_field(name= f'Raw text from {reaction.message.author.name}', value = phrase, inline = False)
            tran.add_field(name= f'Result  🇭🇰', value = trans_ca, inline = False)
            tran.set_footer(text = f'Translator Bot From HolyShxxt Community')
            await reaction.message.channel.send(embed = tran)
            tran.remove_field(index=1)
            tran.remove_field(index=0)

#CantoneseToEnglish
        if emojiid == b'\\U0001f1ec\\U0001f1e7':
            phrase = reaction.message.content
            tss.baidu
            trans_gb = tss.bing(phrase, from_language='yue', to_language='en')
            tran = discord.Embed(color = 0x2ecc71)
            tran.set_author(name = f'Translation Result')
            tran.add_field(name= f'Raw text from {reaction.message.author.name}', value = phrase, inline = False)
            tran.add_field(name= f'Result  🇬🇧', value = trans_gb, inline = False)
            tran.set_footer(text = f'Translator Bot From HolyShxxt Community')
            await reaction.message.channel.send(embed = tran)
            tran.remove_field(index=1)
            tran.remove_field(index=0)

#Dutch
        if emojiid == b'\\U0001f1f3\\U0001f1f1':
            phrase = reaction.message.content
            tss.google
            trans_nl = tss.google(phrase, to_language='nl')
            tran = discord.Embed(color = 0x2ecc71)
            tran.set_author(name = f'Translation Result')
            tran.add_field(name= f'Raw text from {reaction.message.author.name}', value = phrase, inline = False)
            tran.add_field(name= f'Result  🇳🇱', value = trans_nl, inline = False)
            tran.set_footer(text = f'Translator Bot From HolyShxxt Community')
            await reaction.message.channel.send(embed = tran)
            tran.remove_field(index=1)
            tran.remove_field(index=0)

#Russian
        if emojiid == b'\\U0001f1f7\\U0001f1fa':
            phrase = reaction.message.content
            tss.google
            trans_ru = tss.google(phrase, to_language='ru')
            tran = discord.Embed(color = 0x2ecc71)
            tran.set_author(name = f'Translation Result')
            tran.add_field(name= f'Raw text from {reaction.message.author.name}', value = phrase, inline = False)
            tran.add_field(name= f'Result  🇷🇺', value = trans_ru, inline = False)
            tran.set_footer(text = f'Translator Bot From HolyShxxt Community')
            await reaction.message.channel.send(embed = tran)
            tran.remove_field(index=1)
            tran.remove_field(index=0)

#French
        if emojiid == b'\\U0001f1eb\\U0001f1f7':
            phrase = reaction.message.content
            tss.google
            trans_fr = tss.google(phrase, to_language='fr')
            tran = discord.Embed(color = 0x2ecc71)
            tran.set_author(name = f'Translation Result')
            tran.add_field(name= f'Raw text from {reaction.message.author.name}', value = phrase, inline = False)
            tran.add_field(name= f'Result 🇫🇷', value = trans_fr,inline = False)
            tran.set_footer(text = f'Translator Bot From HolyShxxt Community')
            await reaction.message.channel.send(embed = tran)
            tran.remove_field(index=1)
            tran.remove_field(index=0)

client.run("MTAzMjUzNzk3NjMzNDQ2MzAzNg.Ghpe_q.CIwyv41_NOOxqIWCbY8xBeIqr17dVKHkbkzVPk")
