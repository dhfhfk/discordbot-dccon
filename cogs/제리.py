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

class 제리(commands.Cog):
    def __init__(self, client):
        self.client = client
    @cog_ext.cog_slash(name="제리", 
                description="📁 제리 디시콘",
                guild_ids=guild_ids,
                options=[
                    create_option(
                        name="내용",
                        description="무슨 내용인가요?",
                        option_type=3,
                        required=True,
                        choices=[
                            create_choice(
                                name="메롱",
                                value="제리메롱"
                            ),
                            create_choice(
                                name="처먹",
                                value="제리처먹"
                            ),
                            create_choice(
                                name="띠용",
                                value="제리띠용"
                            ),
                            create_choice(
                                name="화들짝",
                                value="제리화들짝"
                            ),
                            create_choice(
                                name="경악",
                                value="제리경악"
                            ),
                            create_choice(
                                name="쯧쯧",
                                value="제리쯧쯧"
                            ),
                            create_choice(
                                name="끄덕",
                                value="제리끄덕"
                            ),
                            create_choice(
                                name="인사",
                                value="제리인사"
                            ),
                            create_choice(
                                name="폭소",
                                value="제리폭소"
                            )
                        ]
                    )
                ])
    async def _제리(self, ctx, 내용: str):
        if 내용 == "제리메롱":
            embed=discord.Embed(description="제리메롱", color=embed_color)
            embed.set_image(url="https://i.ibb.co/2ymkqL0/wpflapfhd.gif")
            await ctx.send(embed=embed)
        elif 내용 == "제리처먹":
            embed=discord.Embed(description="제리처먹", color=embed_color)
            embed.set_image(url="https://i.ibb.co/wsD8mfj/wpflcjajr.gif")
            await ctx.send(embed=embed)
        elif 내용 == "제리띠용":
            embed=discord.Embed(description="제리띠용", color=embed_color)
            embed.set_image(url="https://i.ibb.co/whdv6J4/wpflEldyd.gif")
            await ctx.send(embed=embed)
        elif 내용 == "제리화들짝":
            embed=discord.Embed(description="제리화들짝", color=embed_color)
            embed.set_image(url="https://i.ibb.co/qDn4516/wpflghkemfWkr.gif")
            await ctx.send(embed=embed)
        elif 내용 == "제리경악":
            embed=discord.Embed(description="제리경악", color=embed_color)
            embed.set_image(url="https://i.ibb.co/ngM8DtF/wpflruddkr.gif")
            await ctx.send(embed=embed)
        elif 내용 == "제리쯧쯧":
            embed=discord.Embed(description="제리쯧쯧", color=embed_color)
            embed.set_image(url="https://i.ibb.co/1rNnyPY/wpflWmtWmt.gif")
            await ctx.send(embed=embed)
        elif 내용 == "제리끄덕":
            embed=discord.Embed(description="제리끄덕", color=embed_color)
            embed.set_image(url="https://i.ibb.co/dL00Xk6/wpfl-Rmejr.gif")
            await ctx.send(embed=embed)
        elif 내용 == "제리인사":
            embed=discord.Embed(description="제리인사", color=embed_color)
            embed.set_image(url="https://i.ibb.co/Gs7sNxZ/wpfldlstk2.gif")
            await ctx.send(embed=embed)
        elif 내용 == "제리폭소":
            embed=discord.Embed(description="제리폭소", color=embed_color)
            embed.set_image(url="https://i.ibb.co/JKxvDfN/wpflvhrth.gif")
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(제리(client))