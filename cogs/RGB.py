from discord_slash.utils.manage_commands import create_option, create_choice
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord_slash import cog_ext, SlashContext, SlashCommand
from discord import DMChannel
import re
import asyncio
import os


guild_ids = [int(os.environ['guild_id'])]
embed_color = 0x4ac8c7

class RGB(commands.Cog):
    def __init__(self, client):
        self.client = client
    @cog_ext.cog_slash(name="RGB", 
                description="📁 RGB 디시콘",
                guild_ids=guild_ids,
                options=[
                    create_option(
                        name="내용",
                        description="무슨 내용인가요?",
                        option_type=3,
                        required=True,
                        choices=[
                        create_choice(
                            name="뽕",
                            value="RGB뽕"
                        ),
                        create_choice(
                            name="그자체",
                            value="RGB그자체"
                        )
                        ]
                    )
                ])
    async def _RGB(self, ctx, 내용: str):
        if 내용 == "RGB뽕":
            embed=discord.Embed(description="RGB뽕", color=embed_color)
            embed.set_image(url="https://i.ibb.co/Z65ttZx/RGBQhd.gif")
            await ctx.send(embed=embed)
        elif 내용 == "RGB그자체":
            embed=discord.Embed(description="RGB그자체", color=embed_color)
            embed.set_image(url="https://i.ibb.co/FY3vFF9/RGBrmwkcp.gif")
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(RGB(client))