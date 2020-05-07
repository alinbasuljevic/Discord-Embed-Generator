import discord, requests, discord_webhook, datetime, time
from bs4 import BeautifulSoup as bs

TOKEN = 'insert token here'

client = discord.Client()

bot_dictionary = {
    'Balko': {
        'logo':'https://pbs.twimg.com/profile_images/1177062169231405056/9whojPiW_400x400.jpg',
        'price':'360/Yearly',
        'guide':'They usually either embed a password into a link or into their password page where you will press a button to enter the site. Once you get onto the site proceed as normal on a shopify site until you get to checkout and you will press “Pay with Paypal” and you will be redirected.'
        },
    'Cyber': {
        'logo':'https://pbs.twimg.com/profile_images/1184203863269634048/P98ia02p_400x400.jpg',
        'price':'',
        'guide':''
        },
    'Dashe': {
        'logo':'https://pbs.twimg.com/profile_images/1223442739834118144/WvvIilUp_400x400.png',
        'price':'',
        'guide':''
        },
    'F3ather': {
        'logo':'https://pbs.twimg.com/profile_images/1254451704575275008/f11sbgRh_400x400.jpg',
        'price':'',
        'guide':''
        },
    'Ghost': {
        'logo':'https://pbs.twimg.com/profile_images/1216808451134775296/KuKLwykd_400x400.png',
        'price':'',
        'guide':''
        },
    'Project Destroyer': {
        'logo':'https://pbs.twimg.com/profile_images/1153440082139000832/X59w9ovJ_400x400.jpg',
        'price':'',
        'guide':''
        },
    'MekPreme': {
        'logo':'https://pbs.twimg.com/profile_images/1221893634926301185/eaXls0Xt_400x400.jpg',
        'price':'',
        'guide':''
        },
    'Splashforce': {
        'logo':'https://pbs.twimg.com/profile_images/917391315746385920/cryapglx_400x400.jpg',
        'price':'',
        'guide':''
        }
}

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!info'):
        embed = discord.Embed(title='Embed Generator', description='Here is how you run it', color=0x01e012, inline=True)
        embed.add_field(name='How to Use [Saved Bots]', value='!embed $ [Name of Bot], [Resell], [Useful Url], [Restock Method]', inline=True)
        embed.add_field(name='All Other Bots', value='!embed $ [Name of Bot], [Price], [Resell], [Information], [Logo Url], [Useful Url], [Restock Method]', inline=False)
        embed.add_field(name='Supported Bots', value=list(bot_dictionary.keys()))
        await message.channel.send(embed=embed)
        
    if message.content.startswith('!embed'):
        content = message.content.split('$')[1]
        try:
            title = content.split(',')[0]
            price = bot_dictionary[title.strip()]['price']
            resell = content.split(',')[1]
            information = bot_dictionary[title.strip()]['guide']
            icon = bot_dictionary[title.strip()]['logo']
            url = content.split(',')[2]
            restock_method = content.split(',')[3]
            print (title)
            print (price)
            print (resell)
            print (information)
            print (icon)
            print (url)
            print (restock_method)
        except:
            title = content.split(',')[0]
            price = content.split(',')[1]
            resell = content.split(',')[2]
            information = content.split(',')[3]
            icon = content.split(',')[4]
            url = content.split(',')[5]
            restock_method = content.split(',')[6]
            print (title)
            print (price)
            print (resell)
            print (information)
            print (icon)
            print (url)
            print (restock_method)

        embed = discord.Embed(title='{} Guide/Info'.format(title), color=0x01e012, inline=True)
        embed.add_field(name='Price', value='{}'.format(price), inline=False)
        embed.add_field(name='Resell', value='Resells for {}'.format(resell), inline=False)
        embed.add_field(name='Guide/Site Info', value='{}'.format(information), inline=False)
        embed.add_field(name='Useful Urls', value=f'[Click Here]({url})', inline=False)
        embed.add_field(name='Restock Method', value='{}'.format(restock_method))
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
