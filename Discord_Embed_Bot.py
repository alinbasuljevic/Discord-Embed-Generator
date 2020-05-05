import discord, requests, discord_webhook, datetime, time
from bs4 import BeautifulSoup as bs

TOKEN = ' insert token here'

client = discord.Client()

bot_dictionary = {
    'Balko':'https://pbs.twimg.com/profile_images/1177062169231405056/9whojPiW_400x400.jpg',
    'Cyber':'https://pbs.twimg.com/profile_images/1184203863269634048/P98ia02p_400x400.jpg',
    'Dashe':'https://pbs.twimg.com/profile_images/1223442739834118144/WvvIilUp_400x400.png',
    'F3ather':'https://pbs.twimg.com/profile_images/1254451704575275008/f11sbgRh_400x400.jpg',
    'Ghost':'https://pbs.twimg.com/profile_images/1216808451134775296/KuKLwykd_400x400.png',
    'Project Destroyer':'https://pbs.twimg.com/profile_images/1153440082139000832/X59w9ovJ_400x400.jpg',
    'MekPreme':'https://pbs.twimg.com/profile_images/1221893634926301185/eaXls0Xt_400x400.jpg',
    'Splashforce':'https://pbs.twimg.com/profile_images/917391315746385920/cryapglx_400x400.jpg'
}

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!info'):
        embed = discord.Embed(title='Embed Generator', description='Here is how you run it', color=0x01e012, inline=True)
        embed.add_field(name='How to Use [Saved Bots]', value='!embed $ [Name of Bot], [Price], [Resell], [Information], [Useful Url]', inline=True)
        embed.add_field(name='All Other Bots', value='!embed $ [Name of Bot], [Price], [Resell], [Information], [Logo Url], [Useful Url]', inline=False)
        embed.add_field(name='Supported Bots', value=list(bot_dictionary.keys()))
        await message.channel.send(embed=embed)
        
    if message.content.startswith('!embed'):
        content = message.content.split('$')[1]
        title = content.split(',')[0]
        print (title)
        price = content.split(',')[1]
        print (price)
        resell = content.split(',')[2]
        information = content.split(',')[3]
        print (information)
        icon = content.split(',')[4]
        try:
            icon = bot_dictionary[title.strip()]
            print (icon)
            print ('Found in Dictionary')
            url = content.split(',')[4]
            print (url)
        except:
            print (icon)
            url = content.split(',')[5]
            print (url)

        embed = discord.Embed(title='{} Guide/Info'.format(title), color=0x01e012, inline=True)
        embed.add_field(name='Price', value='{}'.format(price), inline=False)
        embed.add_field(name='Resell', value='Resells for {}'.format(resell), inline=False)
        embed.add_field(name='Guide/Site Info', value='{}'.format(information), inline=False)
        embed.add_field(name='Useful Urls', value=f'[Click Here]({url})', inline=False)
        embed.set_thumbnail(url='{}'.format(icon))
        embed.set_footer(text="Skrufy#0001 By alin#8437", icon_url='https://cdn.discordapp.com/attachments/364971227644952582/707009169475240016/Logo.png')
        await message.channel.send('Embed has been generated and sent!')
        channel = client.get_channel(364971227644952582)
        await channel.send(embed=embed)



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
