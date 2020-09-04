
import discord
import random
import asyncio

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content == '.ping':
            await message.channel.send('Pinging {}'.format(message.author.mention))
                
        if message.content.startswith('.invite gnome'):
            await message.channel.send('https://discord.gg/zWPWwQC')

        if message.content.startswith('.r11'):
            await message.channel.send('you must not pirate dipshit')

        if message.content.startswith('.wink'):
            await message.channel.send(':wink:')

        if message.content.startswith('.slep'):
            await message.channel.send('https://cdn.discordapp.com/emojis/395626850887532544.png?v=1')

        if message.content.startswith('.credits'):
            await message.channel.send('Lazr-Coder, UwUham-Helping, Gnome-idk i feel like putting him here')

        if message.content.startswith('.invite meme'):
            await message.channel.send('https://discord.gg/7ECUWDp')

        if message.content.startswith('.pizzatime'):
            await message.channel.send(':pizza:')

        if message.content.startswith('.dip'):
            await message.channel.send('shit')

        if message.content.startswith('.invite bot'):
            await message.channel.send('ask in <#745916861404938250> to add your bot')

        if message.content.startswith('!fight'):
            await message.channel.send ('you seem to be in <#745916861404938250>')

        if message.content.startswith('.ice cream'):
            await message.channel.send(':ice_cream:')

        if message.content.startswith('.shitpost'):
            await message.channel.send('go to <#744832077106774026> ffs')

        if message.content.startswith('.rule'):
            await message.channel.send('go re-read <#745907341723172914> ffs')

        if message.content.startswith('.r3'):
            await message.channel.send('memes are allowed in <#751502174189781074>')

        if message.content.startswith('.ping lazr'):
            await message.channel.send('ping <@664297659686715403> in <#749006035423068180> ffs')


    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'Welcome {0.mention} to {1.name}!'.format(member, guild)
            await guild.system_channel.send(to_send)


client = MyClient()
client.run('NzQ0Nzk4NTQzOTkwMjI2OTk0.Xzodsg.yOofRErtIPIpuGCsv7SWAT5qfyg')
