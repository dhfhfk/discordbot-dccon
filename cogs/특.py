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

class 특(commands.Cog):
    def __init__(self, client):
        self.client = client
    @cog_ext.cog_slash(name="특", 
                description="📁 개발자특 바쁨",
                guild_ids=guild_ids,
                options=[
                    create_option(
                        name="내용",
                        description="무슨 내용인가요?",
                        option_type=3,
                        required=True,
                        choices=[
                            create_choice(
                                name="디자이너",
                                value="디자이너특"
                            ),
                            create_choice(
                                name="디자이너2",
                                value="디자이너특2"
                            ),
                            create_choice(
                                name="CSS",
                                value="CSS특"
                            ),
                            create_choice(
                                name="CSS2",
                                value="CSS특2"
                            )
                        ]
                    )
                ]
        )
    async def _특(self, ctx, 내용: str):
        if 내용 == "디자이너특":
                embed=discord.Embed(description="디자이너특", color=embed_color)
                embed.set_image(url="https://i.ibb.co/JcncbDj/elwkdlsjxmr.gif")
                await ctx.send(embed=embed)
        elif 내용 == "디자이너특2":
                embed=discord.Embed(description="디자이너특2", color=embed_color)
                embed.set_image(url="https://i.ibb.co/9n6x4hQ/elwkdlsjxmr2.png")
                await ctx.send(embed=embed)
        elif 내용 == "CSS특":
                embed=discord.Embed(description="CSS특", color=embed_color)
                embed.set_image(url="https://i.ibb.co/6Js7Mty/CSSxmr.gif")
                await ctx.send(embed=embed)
        elif 내용 == "CSS특2":
                embed=discord.Embed(description="CSS특2", color=embed_color)
                embed.set_image(url="https://i.ibb.co/gFr6mXx/CSS2.gif")
                await ctx.send(embed=embed)

def setup(client):
    client.add_cog(특(client))