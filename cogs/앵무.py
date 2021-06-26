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

class 앵무(commands.Cog):
    def __init__(self, client):
        self.client = client
    @cog_ext.cog_slash(name="앵무", 
                description="📁 앵무 디시콘",
                guild_ids=guild_ids,
                options=[
                    create_option(
                        name="내용",
                        description="무슨 내용인가요?",
                        option_type=3,
                        required=True,
                        choices=[
                            create_choice(
                                name="댄스",
                                value="앵무댄스"
                            ),
                            create_choice(
                                name="선글",
                                value="앵무선글"
                            ),
                            create_choice(
                                name="팝콘",
                                value="앵무팝콘"
                            ),
                            create_choice(
                                name="혼란",
                                value="앵무혼란"
                            )
                        ]
                    )
                ])
    async def _앵무(self, ctx, 내용: str):
        if 내용 == "앵무댄스":
            embed=discord.Embed(description="앵무댄스", color=embed_color)
            embed.set_image(url="https://i.ibb.co/gM3pJQx/dodaneostm.gif")
            await ctx.send(embed=embed)
        elif 내용 == "앵무선글":
            embed=discord.Embed(description="앵무선글", color=embed_color)
            embed.set_image(url="https://i.ibb.co/m6txyNv/dodantjsrmf.gif")
            await ctx.send(embed=embed)
        elif 내용 == "앵무팝콘":
            embed=discord.Embed(description="앵무팝콘", color=embed_color)
            embed.set_image(url="https://i.ibb.co/DfBNjpM/dodanvkqzhs.gif")
            await ctx.send(embed=embed)
        elif 내용 == "앵무혼란":
            embed=discord.Embed(description="앵무혼란", color=embed_color)
            embed.set_image(url="https://i.ibb.co/vsTGdyZ/dodanghsfks.gif")
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(앵무(client))