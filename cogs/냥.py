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

class 냥(commands.Cog):
    def __init__(self, client):
        self.client = client
    @cog_ext.cog_slash(name="냥", 
                description="📁 냐옹이 디시콘",
                guild_ids=guild_ids,
                options=[
                    create_option(
                        name="내용",
                        description="무슨 내용인가요?",
                        option_type=3,
                        required=True,
                        choices=[
                            create_choice(
                                name="경악",
                                value="냥경악"
                            ),
                            create_choice(
                                name="슬픔",
                                value="냥슬픔"
                            ),
                            create_choice(
                                name="선글",
                                value="냥선글"
                            ),
                            create_choice(
                                name="정색",
                                value="냥정색"
                            )
                        ]
                    )
                ])
    async def _냥(self, ctx, 내용: str):
        if 내용 == "냥경악":
            embed=discord.Embed(description="냥경악", color=embed_color)
            embed.set_image(url="https://i.ibb.co/gDB9mzd/sidruddkr.gif")
            await ctx.send(embed=embed)
            
        elif 내용 == "냥슬픔":
            embed=discord.Embed(description="냥슬픔", color=embed_color)
            embed.set_image(url="https://i.ibb.co/VxZ3g53/sidtmfvma.gif")
            await ctx.send(embed=embed)
            
        elif 내용 == "냥선글":
            embed=discord.Embed(description="냥선글", color=embed_color)
            embed.set_image(url="https://i.ibb.co/fXgGK2s/sidtjsrmf.gif")
            await ctx.send(embed=embed)
            
        elif 내용 == "냥정색":
            embed=discord.Embed(description="냥정색", color=embed_color)
            embed.set_image(url="https://i.ibb.co/d43H7m6/sidwjdtor.gif")
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(냥(client))