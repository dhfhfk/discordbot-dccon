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

class 에펙(commands.Cog):
    def __init__(self, client):
        self.client = client
    @cog_ext.cog_slash(name="에펙", 
                description="📁 에이펙스레전드 디시콘",
                guild_ids=guild_ids,
                options=[
                    create_option(
                        name="내용",
                        description="무슨 내용인가요?",
                        option_type=3,
                        required=True,
                        choices=[
                            create_choice(
                                name="모잠비크",
                                value="에펙모잠비크"
                            ),
                            create_choice(
                                name="무섭",
                                value="에펙무섭"
                            ),
                            create_choice(
                                name="아크스타",
                                value="에펙아크스타"
                            ),
                            create_choice(
                                name="있었는데요",
                                value="에펙있었는데요"
                            ),
                            create_choice(
                                name="시도",
                                value="에펙시도"
                            ),
                            create_choice(
                                name="전설",
                                value="에펙전설"
                            ),
                            create_choice(
                                name="태보킥",
                                value="에펙태보킥"
                            ),
                            create_choice(
                                name="뱀부",
                                value="에펙뱀부"
                            ),
                            create_choice(
                                name="고뱀부",
                                value="에펙고뱀부"
                            )
                        ]
                    )
                ])
    async def _에펙(self, ctx, 내용: str):
        if 내용 == "에펙모잠비크":
            embed=discord.Embed(description="에펙모잠비크", color=embed_color)
            embed.set_image(url="https://i.ibb.co/Zz4cNgc/dpvprahwkaqlzm.png")
            await ctx.send(embed=embed)
        elif 내용 == "에펙무섭":
            embed=discord.Embed(description="에펙무섭", color=embed_color)
            embed.set_image(url="https://i.ibb.co/F4vXLqF/dpvprantjq.png")
            await ctx.send(embed=embed)
        elif 내용 == "에펙아크스타":
            embed=discord.Embed(description="에펙아크스타", color=embed_color)
            embed.set_image(url="https://i.ibb.co/m4h4R5k/dpvprdkzmtmxk.png")
            await ctx.send(embed=embed)
        elif 내용 == "에펙있었는데요":
            embed=discord.Embed(description="에펙있었는데요", color=embed_color)
            embed.set_image(url="https://i.ibb.co/CmZwDHG/dpvprdlTdjTsms.png")
            await ctx.send(embed=embed)
        elif 내용 == "에펙시도":
            embed=discord.Embed(description="에펙시도", color=embed_color)
            embed.set_image(url="https://i.ibb.co/z23pdxp/dpvprtleh.png")
            await ctx.send(embed=embed)
        elif 내용 == "에펙전설":
            embed=discord.Embed(description="에펙전설", color=embed_color)
            embed.set_image(url="https://i.ibb.co/3WJTBys/dpvprwjstjf.png")
            await ctx.send(embed=embed)
        elif 내용 == "에펙태보킥":
            embed=discord.Embed(description="에펙태보킥", color=embed_color)
            embed.set_image(url="https://i.ibb.co/mDc9YKj/dpvprxoqhzlr.png")
            await ctx.send(embed=embed)
        elif 내용 == "에펙뱀부":
            embed=discord.Embed(description="에펙뱀부", color=embed_color)
            embed.set_image(url="https://i.ibb.co/HBbzskp/dpvprqoaqn.png")
            await ctx.send(embed=embed)
        elif 내용 == "에펙고뱀부":
            embed=discord.Embed(description="에펙고뱀부", color=embed_color)
            embed.set_image(url="https://i.ibb.co/pZmBY2F/dpvprrhqoaqn.png")
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(에펙(client))