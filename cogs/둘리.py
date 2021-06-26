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

class 둘리(commands.Cog):
    def __init__(self, client):
        self.client = client
    @cog_ext.cog_slash(name="둘리", 
                description="📁 둘리 디시콘",
                guild_ids=guild_ids,
                options=[
                    create_option(
                        name="내용",
                        description="무슨 내용인가요?",
                        option_type=3,
                        required=True,
                        choices=[
                            create_choice(
                                name="초능력",
                                value="둘리초능력"
                            ),
                            create_choice(
                                name="처신",
                                value="둘리처신"
                            ),
                            create_choice(
                                name="웃음",
                                value="둘리웃음"
                            ),
                            create_choice(
                                name="호잇",
                                value="둘리호잇"
                            ),
                            create_choice(
                                name="흑우",
                                value="둘리흑우"
                            ),
                            create_choice(
                                name="꼴받",
                                value="둘리꼴받"
                            ),
                            create_choice(
                                name="나가",
                                value="둘리나가"
                            ),
                            create_choice(
                                name="냄새",
                                value="둘리냄새"
                            ),
                            create_choice(
                                name="성능",
                                value="둘리성능"
                            ),
                            create_choice(
                                name="선넘네",
                                value="둘리선넘네"
                            ),
                            create_choice(
                                name="싯팔",
                                value="둘리싯팔"
                            ),
                            create_choice(
                                name="좋지",
                                value="둘리좋지"
                            ),
                            create_choice(
                                name="정신",
                                value="둘리정신"
                            ),
                            create_choice(
                                name="죽상",
                                value="둘리죽상"
                            )
                        ]
                    )
                ])
    async def _둘리(self, ctx, 내용: str):
        if 내용 == "둘리초능력":
            embed=discord.Embed(description="둘리초능력", color=embed_color)
            embed.set_image(url="https://i.ibb.co/brTzWWr/enfflchsmdfur.png")
            await ctx.send(embed=embed)
        elif 내용 == "둘리처신":
            embed=discord.Embed(description="둘리처신", color=embed_color)
            embed.set_image(url="https://i.ibb.co/68bkXKD/enfflcjtls.png")
            await ctx.send(embed=embed)
        elif 내용 == "둘리웃음":
            embed=discord.Embed(description="둘리웃음", color=embed_color)
            embed.set_image(url="https://i.ibb.co/GTzqBwp/enffldntdma.png")
            await ctx.send(embed=embed)
        elif 내용 == "둘리호잇":
            embed=discord.Embed(description="둘리호잇", color=embed_color)
            embed.set_image(url="https://i.ibb.co/jfPMZ6t/enfflghdlt.png")
            await ctx.send(embed=embed)
        elif 내용 == "둘리흑우":
            embed=discord.Embed(description="둘리흑우", color=embed_color)
            embed.set_image(url="https://i.ibb.co/Cwy8nSM/enfflgmrdn.png")
            await ctx.send(embed=embed)
        elif 내용 == "둘리꼴받":
            embed=discord.Embed(description="둘리꼴받", color=embed_color)
            embed.set_image(url="https://i.ibb.co/ZGNqMdT/enfflRhfqke.png")
            await ctx.send(embed=embed)
        elif 내용 == "둘리나가":
            embed=discord.Embed(description="둘리나가", color=embed_color)
            embed.set_image(url="https://i.ibb.co/nDTgfsR/enfflskrk.png")
            await ctx.send(embed=embed)
        elif 내용 == "둘리냄새":
            embed=discord.Embed(description="둘리냄새", color=embed_color)
            embed.set_image(url="https://i.ibb.co/LQ6TRk3/enfflsoato.png")
            await ctx.send(embed=embed)
        elif 내용 == "둘리성능":
            embed=discord.Embed(description="둘리성능", color=embed_color)
            embed.set_image(url="https://i.ibb.co/KxWvjMF/enffltjdsmd.png")
            await ctx.send(embed=embed)
        elif 내용 == "둘리선넘네":
            embed=discord.Embed(description="둘리선넘네", color=embed_color)
            embed.set_image(url="https://i.ibb.co/2N1PtPW/enffltjssjasp.png")
            await ctx.send(embed=embed)
        elif 내용 == "둘리싯팔":
            embed=discord.Embed(description="둘리싯팔", color=embed_color)
            embed.set_image(url="https://i.ibb.co/y6NxGJK/enffltltvkf.png")
            await ctx.send(embed=embed)
        elif 내용 == "둘리좋지":
            embed=discord.Embed(description="둘리좋지", color=embed_color)
            embed.set_image(url="https://i.ibb.co/2vrRB9D/enfflwhgwl.png")
            await ctx.send(embed=embed)
        elif 내용 == "둘리정신":
            embed=discord.Embed(description="둘리정신", color=embed_color)
            embed.set_image(url="https://i.ibb.co/5s9GtMr/enfflwjdtls.png")
            await ctx.send(embed=embed)
        elif 내용 == "둘리죽상":
            embed=discord.Embed(description="둘리죽상", color=embed_color)
            embed.set_image(url="https://i.ibb.co/3vyJf3X/enfflwnrtkd.png")
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(둘리(client))