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

class 컴붕(commands.Cog):
    def __init__(self, client):
        self.client = client 
    @cog_ext.cog_slash(name="컴붕", 
                description="📁 컴퓨터 디시콘",
                guild_ids=guild_ids,
                options=[
                    create_option(
                        name="내용",
                        description="무슨 내용인가요?",
                        option_type=3,
                        required=True,
                        choices=[
                            create_choice(
                                name="앱등",
                                value="컴붕앱등"
                            ),
                            create_choice(
                                name="인텔",
                                value="컴붕인텔"
                            ),
                            create_choice(
                                name="RGB",
                                value="컴붕RGB"
                            ),
                            create_choice(
                                name="특가",
                                value="컴붕특가"
                            ),
                            create_choice(
                                name="발열",
                                value="컴붕발열"
                            ),
                        ]
                    )
                ])
    async def _컴붕(self, ctx, 내용: str):
        if 내용 == "컴붕앱등":
            embed=discord.Embed(description="컴붕앱등", color=embed_color)
            embed.set_image(url="https://i.ibb.co/jhkPpD2/zjaqnddoqemd.png")
            await ctx.send(embed=embed)
        elif 내용 == "컴붕인텔":
            embed=discord.Embed(description="컴붕인텔", color=embed_color)
            embed.set_image(url="https://i.ibb.co/8dWKMwh/zjaqnddlsxpf.png")
            await ctx.send(embed=embed)
        elif 내용 == "컴붕RGB":
            embed=discord.Embed(description="컴붕RGB", color=embed_color)
            embed.set_image(url="https://i.ibb.co/XSLnkk8/zjaqnd-RGB.png")
            await ctx.send(embed=embed)
        elif 내용 == "컴붕특가":
            embed=discord.Embed(description="컴붕특가", color=embed_color)
            embed.set_image(url="https://i.ibb.co/JK9x5Q3/zjaqndxmrrk.png")
            await ctx.send(embed=embed)
        elif 내용 == "컴붕발열":
            embed=discord.Embed(description="컴붕발열", color=embed_color)
            embed.set_image(url="https://i.ibb.co/7KzCQ8N/zjaqndqkfduf.png")
            await ctx.send(embed=embed)
        

def setup(client):
    client.add_cog(컴붕(client))