import nest_asyncio 
nest_asyncio.apply()
import discord
from discord.ext import commands
import random
import datetime
import time
import os


# Prefix is set to g! for all commands
intents = discord.Intents.all()
client = commands.Bot(command_prefix = 'LE!', intents=intents)

@client.event
async def on_ready():
    # Prints a message when the bot is online and functioning
    await client.change_presence(status=discord.Status.online, activity = discord.Game(name=f"Let's join Community-GameFi NFT HolyShxxt! 🥳 🎉 Currently in {len(client.guilds)} servers! 🎉"))
    print('Ready to giveaway!')


@client.command()
async def Blessing(ctx, prize, t):
   
    # Storing the variables needed to run the rest of the commands
    channel = ctx.channel
    prize = str(prize)
    t = int(t)

    # Giveaway embed message
    give = discord.Embed(color = 0x2ecc71)
    give.set_author(name = f'LE Blessing Time!', icon_url = 'https://images.emojiterra.com/google/android-11/512px/1f6d5.png')
    give.add_field(name= f'{ctx.author.name} is summoning LE God: {prize}!', value = f'React with 💡 to enter!\n Ends in {t} minutes!', inline = False)
    end = datetime.datetime.utcnow() + datetime.timedelta(seconds=(t*60))
    give.set_footer(text = f'Blessing starts at {end.strftime("%m/%d/%Y, %H:%M")} UTC!')
    my_message = await channel.send(embed = give)
    
    # Reacts to the message
    await my_message.add_reaction("💡")

    time.sleep(t*60)

    new_message = await channel.fetch_message(my_message.id)

    # Picks a winner
    users = await new_message.reactions[0].users().flatten()
    users.pop(users.index(client.user))
    
    random.shuffle(users)
    random.shuffle(users)
    if len(users) == 0:
          await ctx.send("No one reacted.")
    else:
      await ctx.send(f"All blessings from LE God will become true reversely.") 
      give = discord.Embed(color = 0x46aefc)
      give.set_author(name = f'LE Blessing Time Starts!', icon_url = 'https://i.imgur.com/VaX0pfM.png')
      loop = len(users)-1
      print(len(users))
      x = 0
      while x < loop: #Start the loop
        r = random.randint(1,20) 
        if r == 1:
          give.add_field(name= f"LE God said: ", value = f" **  ** {users[x]} ** **'s Metamask wallet will not be hacked \n Then,  ** {users[x]} ** jump off from IFC because leaked his own recovery phrase ", inline = False)
          x = x + 1
          give.set_footer(text = f'Remaining {len(users) - x} ')
          my_message = await channel.send(embed = give)
        if r == 2: 
          give.add_field(name= f"LE God said:  ", value = f" ** {users[x]} **'s spring pocket will not be barbecued \n Then,  ** {users[x]} **'s spring pocket is overburnt and is eaten by a dog ", inline = False)
          x = x + 1
          give.set_footer(text = f'Remaining {len(users) - x} ')
          my_message = await channel.send(embed = give)
        if r == 3:
          give.add_field(name= f"LE God said:  ", value = f' ** {users[x]} ** will not be rugged.\n Then,  ** {users[x]} ** attempted suicide by hanging himself \n', inline = False)
          x = x + 1
          give.set_footer(text = f'Remaining {len(users) - x} ')
          my_message = await channel.send(embed = give)
        if r == 4:
          give.add_field(name= f"LE God said:  ", value = f' ** {users[x]} **  will not find that 1cm is standing behind \n Then,  ** {users[x]} ** is tormented by FatHo until death \n', inline = False)
          x = x + 1
          give.set_footer(text = f'Remaining {len(users) - x} ')
          my_message = await channel.send(embed = give)
        if r == 5:
          give.add_field(name= f"LE God said:  ", value = f'  ** {users[x]} ** will not be given a red card \n Then,  ** {users[x]} ** die from a stroke \n', inline = False)
          x = x + 1
          give.set_footer(text = f'Remaining {len(users) - x} ')
          my_message = await channel.send(embed = give)
        if r == 6:
          give.add_field(name= f"LE God said:  ", value = f' ** {users[x]} ** will not give out all the money to Jockey Club \n Then,  ** {users[x]} ** is killed by big ear hole \n', inline = False)
          x = x + 1
          give.set_footer(text = f'Remaining {len(users) - x} ')
          my_message = await channel.send(embed = give)
        if r == 7:
          give.add_field(name= f"LE God said:  ", value = f' ** {users[x]} ** will not need to drink plenty of Red Bull \n Then,  ** {users[x]} ** die after trying to fly \n', inline = False)
          x = x + 1
          give.set_footer(text = f'Remaining {len(users) - x} ')
          my_message = await channel.send(embed = give) 
        if r == 8:
          give.add_field(name= f"LE God said:  ", value = f" ** {users[x]} ** will not lose all HolyShxxt Tournament \n Then,  ** {users[x]} ** is killed by club's agents  \n", inline = False)
          x = x + 1
          give.set_footer(text = f'Remaining {len(users) - x} ')
          my_message = await channel.send(embed = give)
        if r == 9:
          give.add_field(name= f"LE God said:  ", value = f' ** {users[x]} ** will not lose all the Key0Coin \n Then,  ** {users[x]} ** die after broken his keyboard   \n', inline = False)
          x = x + 1
          give.set_footer(text = f'Remaining {len(users) - x} ')
          my_message = await channel.send(embed = give)
        if r == 10:
          give.add_field(name= f"LE God said:  ", value = f' ** {users[x]} ** will not see an atomic bomb is coming \n Then,  ** {users[x]} ** is sent to North Korea   \n', inline = False)
          x = x + 1
          give.set_footer(text = f'Remaining {len(users) - x} ')
          my_message = await channel.send(embed = give)
        if r == 11:
          give.add_field(name= f"LE God said:  ", value = f' ** {users[x]} ** will not throw a soap to 0nn \n Then,  ** {users[x]} ** die because of butt damaged by 1cm   \n', inline = False)
          x = x + 1
          give.set_footer(text = f'Remaining {len(users) - x} ')
          my_message = await channel.send(embed = give)
        if r == 12:
          give.add_field(name= f"LE God said:  ", value = f' ** {users[x]} ** will not be headbutted by Zidane \n Then,  ** {users[x]} ** die after myocardial infarction   \n', inline = False)
          x = x + 1
          give.set_footer(text = f'Remaining {len(users) - x} ')
          my_message = await channel.send(embed = give)
        if r == 13:
          give.add_field(name= f"LE God said:  ", value = f'  ** {users[x]} ** will not get the same hairstyle as Gervinho \n Then,  ** {users[x]} ** die after looking at the mirror   \n', inline = False)
          x = x + 1
          give.set_footer(text = f'Remaining {len(users) - x} ')
          my_message = await channel.send(embed = give)
        if r == 14:
          give.add_field(name= f"LE God said:  ", value = f'  ** {users[x]} ** will not see Cat Girl is coming \n Then,  ** {users[x]} ** is killed by an admirer of Cat Girl, Riven  \n', inline = False)
          x = x + 1
          give.set_footer(text = f'Remaining {len(users) - x} ')
          my_message = await channel.send(embed = give)
        if r == 15:
          give.add_field(name= f"LE God said:  ", value = f' ** {users[x]} ** will not see a beautiful girl with stick \n Then,  ** {users[x]} ** die in the male toilet \n', inline = False)
          x = x + 1
          give.set_footer(text = f'Remaining {len(users) - x} ')
          my_message = await channel.send(embed = give)
        if r == 16:
          give.add_field(name= f"LE God said:  ", value = f' ** {users[x]} ** will not run naked with 1cm \n Then,  ** {users[x]} ** die in Walk of Shame with Cersei \n', inline = False)
          x = x + 1
          give.set_footer(text = f'Remaining {len(users) - x} ')
          my_message = await channel.send(embed = give)
        if r == 17:
            if (x+1) < len(users)-2:
                give.add_field(name= f"LE God said:  ", value = f' ** {users[x]} ** will not get hurt easily \n Then,  ** {users[x]} ** and ** {users[x+1]} ** die in the fighting with each other  \n', inline = False)
                x = x + 2
                give.set_footer(text = f'Remaining {len(users) - x} ')
                my_message = await channel.send(embed = give)
            else:
                give.add_field(name= f"LE God said:  ", value = f' ** {users[x]} ** will not be banned by Mee6Bot \n Then,  ** {users[x]} ** die in spamming ugly photos in happy wife channel \n', inline = False)
                x = x + 1
                give.set_footer(text = f'Remaining {len(users) - x} ')
                my_message = await channel.send(embed = give)
        if r == 18:
            if (x+1) < len(users)-2:
                give.add_field(name= f"LE God said:  ", value = f' ** {users[x]} ** will become millionaire  \n Then,  ** {users[x]} ** is robbed by ** {users[x+1]} ** and both of them die in a car accident  \n', inline = False)
                x = x + 2
                give.set_footer(text = f'Remaining {len(users) - x} ')
                my_message = await channel.send(embed = give)
            else:
                give.add_field(name= f"LE God said:  ", value = f' ** {users[x]} ** will be able to learn swimming \n Then,  ** {users[x]} ** die in the tsunami \n', inline = False)
                x = x + 1
                give.set_footer(text = f'Remaining {len(users) - x} ')
                my_message = await channel.send(embed = give)
        if r == 19:
            if (x+1) < len(users)-2:
                give.add_field(name= f"LE God said:  ", value = f' ** {users[x]} ** will get a big prize in the raffle  \n Then,  ** {users[x+1]} ** get the biggest prize and mistakenly write both name of ** {users[x]} ** and ** {users[x+1]} ** on the Death Note  \n', inline = False)
                x = x + 2
                give.set_footer(text = f'Remaining {len(users) - x} ')

                my_message = await channel.send(embed = give)
            else:
                give.add_field(name= f"LE God said:  ", value = f" ** {users[x]} ** will have a beautiful handwritting \n Then,  ** {users[x]} **'s name is being found on the Death Note \n", inline = False)
                x = x + 1
                give.set_footer(text = f'Remaining {len(users) - x} ')
                my_message = await channel.send(embed = give)
        if r == 20:
            if (x+1) < len(users)-2:
                give.add_field(name= f"LE God said:  ", value = f' ** {users[x]} ** will have a romantic trip   \n Then,  ** {users[x+1]} ** back hug ** {users[x]} ** and say You Jump I Jump on Titanic  \n', inline = False)
                x = x + 2
                give.set_footer(text = f'Remaining {len(users) - x} ')
                my_message = await channel.send(embed = give)
            else:
                give.add_field(name= f"LE God said:  ", value = f" ** {users[x]} ** will get a great job \n Then,  ** {users[x]} ** works in Cambodia \n", inline = False)
                x = x + 1
                give.set_footer(text = f'Remaining {len(users) - x} ')
                my_message = await channel.send(embed = give)
                 
        give.remove_field(index=0)
        time.sleep(10)
      
      give.set_footer(text = f'Blessing End !')
      my_message = await channel.send(embed = give)
          
    if len(users) == 0:
          await ctx.send("No one reacted.")
    else:
          winner = users[len(users)-1] 

    # Announces the winner
    winning_announcement = discord.Embed(color = 0xff2424)
    winning_announcement.set_author(name = f'The Blessing Has Ended!', icon_url= 'https://images.emojiterra.com/twitter/v13.1/512px/1f4a1.png')
    winning_announcement.add_field(name = f'🎁 Prize: {prize}', value = f'🥳 **Survivor**: {winner.mention}\n 🎫 **Number of Entrants**: {len(users)}', inline = False)
    winning_announcement.set_footer(text = 'Thanks for entering!')
    await channel.send(embed = winning_announcement)

client.run([Token])
