from discord_slash.utils.manage_commands import create_option, create_choice
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord_slash import cog_ext, SlashContext, SlashCommand
from discord import DMChannel
import re
import asyncio
import os


guild_ids = [367303729566711808]
embed_color = 0x4ac8c7

class 사수(commands.Cog):
    def __init__(self, client):
        self.client = client
    @cog_ext.cog_slash(name="사수", 
                description="📁 리사수 디시콘",
                guild_ids=guild_ids,
                options=[
                    create_option(
                        name="내용",
                        description="무슨 내용인가요?",
                        option_type=3,
                        required=True,
                        choices=[
                            create_choice(
                                name="웃음",
                                value="사수웃음"
                            ),
                            create_choice(
                                name="화남",
                                value="사수화남"
                            ),
                            create_choice(
                                name="자랑",
                                value="사수자랑"
                            ),
                            create_choice(
                                name="썬글",
                                value="사수썬글"
                            ),
                            create_choice(
                                name="클럽",
                                value="사수클럽"
                            )
                        ]
                    )
                ])
    async def _사수(self, ctx, 내용: str):
        if 내용 == "사수웃음":
            embed=discord.Embed(description="사수웃음", color=embed_color)
            embed.set_image(url="https://i.ibb.co/N1rGd22/tktndntdma.gif")
            await ctx.send(embed=embed)
        elif 내용 == "사수화남":
            embed=discord.Embed(description="사수화남", color=embed_color)
            embed.set_image(url="https://i.ibb.co/6WD90vm/tktnghkska.gif")
            await ctx.send(embed=embed)
        elif 내용 == "사수자랑":
            embed=discord.Embed(description="사수자랑", color=embed_color)
            embed.set_image(url="https://i.ibb.co/nncpZXx/tktnwkfkd.gif")
            await ctx.send(embed=embed)
        elif 내용 == "사수썬글":
            embed=discord.Embed(description="사수썬글", color=embed_color)
            embed.set_image(url="https://i.ibb.co/sP9nZTV/tktn-Tjsrmf.gif")
            await ctx.send(embed=embed)
        elif 내용 == "사수클럽":
            embed=discord.Embed(description="사수클럽", color=embed_color)
            embed.set_image(url="https://i.ibb.co/DwHvbhs/tktnzmffjq.gif")
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(사수(client))