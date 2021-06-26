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

class 우리핵(commands.Cog):
    def __init__(self, client):
        self.client = client
    @cog_ext.cog_slash(name="우리핵", 
                description="📁 우리핵 디시콘",
                guild_ids=guild_ids,
                options=[
                    create_option(
                        name="내용",
                        description="무슨 내용인가요?",
                        option_type=3,
                        required=True,
                        choices=[
                            create_choice(
                                name="안무",
                                value="우리핵안무"
                            ),
                            create_choice(
                                name="안녕",
                                value="우리핵안녕"
                            ),
                            create_choice(
                                name="드럼",
                                value="우리핵드럼"
                            ),
                            create_choice(
                                name="박수",
                                value="우리핵박수"
                            ),
                            create_choice(
                                name="갸우뚱",
                                value="우리핵갸우뚱"
                            )
                        ]
                    )
                ]
    )
    async def _우리핵(self, ctx: SlashContext, 내용: str):
        if 내용 == "우리핵안무":
            embed=discord.Embed(description="우리핵안무", color=embed_color)
            embed.set_image(url="https://i.ibb.co/0tJN50r/dnflgordksan.gif")
            await ctx.send(embed=embed)
            

        elif 내용 == "우리핵안녕":
            embed=discord.Embed(description="우리핵안녕", color=embed_color)
            embed.set_image(url="https://i.ibb.co/RgfHT8J/dnflgordkssud.gif")
            await ctx.send(embed=embed)
            

        elif 내용 == "우리핵드럼":
            embed=discord.Embed(description="우리핵드럼", color=embed_color)
            embed.set_image(url="https://i.ibb.co/QccRgHK/dnflgoremfja.gif")
            await ctx.send(embed=embed)
            

        elif 내용 == "우리핵박수":
            embed=discord.Embed(description="우리핵박수", color=embed_color)
            embed.set_image(url="https://i.ibb.co/0n38dCT/dnflgorqkrtn.gif")
            await ctx.send(embed=embed)

        elif 내용 == "우리핵갸우뚱":
            embed=discord.Embed(description="우리핵갸우뚱", color=embed_color)
            embed.set_image(url="https://i.ibb.co/XZ9SBzw/dnflgorridnEnd.gif")
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(우리핵(client))