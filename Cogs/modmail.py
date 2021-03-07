import discord as d
import random
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import BucketType



class modmail(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    @commands.dm_only()
    async def on_message(self, message):
        channels = self.bot.get_all_channels()
        channel = get(channels, guild__name="Clark's Chamber", name='staff-chat')
        try:
            if message.channel == message.author.dm_channel:
                await channel.send(embed=d.Embed(title=f'Modmail from {message.author}', color=0x2c2f33, description=f"{message.content}").set_footer(text=f'ID: {message.author.id}'))
                await message.channel.send('Your message has been sent!', delete_after=7)
        except:
            pass

    ## ^ simple modmail event, it works, that's all that matters.






def setup(bot):
    bot.add_cog(modmail(bot))
