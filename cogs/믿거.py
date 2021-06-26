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

class 믿거(commands.Cog):
    def __init__(self, client):
        self.client = client
    @cog_ext.cog_slash(name="믿거", 
                description="📁 믿고거를 디시콘",
                guild_ids=guild_ids,
                options=[
                    create_option(
                        name="내용",
                        description="무슨 내용인가요?",
                        option_type=3,
                        required=True,
                        choices=[
                            create_choice(
                                name="애",
                                value="믿거애"
                            ),
                            create_choice(
                                name="앱",
                                value="믿거앱"
                            ),
                            create_choice(
                                name="한",
                                value="믿거한"
                            ),
                            create_choice(
                                name="시",
                                value="믿거시"
                            )
                        ]
                    )
                ])
    async def _믿거(self, ctx, 내용: str):
        if 내용 == "믿거애":
            embed=discord.Embed(description="믿거애", color=embed_color)
            embed.set_image(url="https://i.ibb.co/ByvWfmF/alerjdo.png")
            await ctx.send(embed=embed)
        elif 내용 == "믿거앱":
            embed=discord.Embed(description="믿거앱", color=embed_color)
            embed.set_image(url="https://i.ibb.co/VV3Xzth/alerjdoq.png")
            await ctx.send(embed=embed)
        elif 내용 == "믿거한":
            embed=discord.Embed(description="믿거한", color=embed_color)
            embed.set_image(url="https://i.ibb.co/Qbn3w3Q/alerjgks.png")
            await ctx.send(embed=embed)
        elif 내용 == "믿거시":
            embed=discord.Embed(description="믿거시", color=embed_color)
            embed.set_image(url="https://i.ibb.co/yYspgQf/alerjtl.png")
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(믿거(client))