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

class 프붕(commands.Cog):
    def __init__(self, client):
        self.client = client
    @cog_ext.cog_slash(name="프붕", 
                description="📁 프로그래밍 디시콘",
                guild_ids=guild_ids,
                options=[
                    create_option(
                        name="내용",
                        description="무슨 내용인가요?",
                        option_type=3,
                        required=True,
                        choices=[
                        create_choice(
                            name="망코드",
                            value="프붕망코드"
                        ),
                        create_choice(
                            name="메모리",
                            value="프붕메모리"
                        ),
                        create_choice(
                            name="몇번",
                            value="프붕몇번"
                        ),
                        create_choice(
                            name="책",
                            value="프붕책"
                        ),
                        create_choice(
                            name="언어탓",
                            value="프붕언어탓"
                        ),
                        create_choice(
                            name="따봉",
                            value="프붕따봉"
                        ),
                        create_choice(
                            name="밤샘",
                            value="프붕밤샘"
                        ),
                        create_choice(
                            name="반복",
                            value="프붕반복"
                        ),
                        create_choice(
                            name="스파게티",
                            value="프붕스파게티"
                        ),
                        create_choice(
                            name="생각",
                            value="프붕생각"
                        ),
                        create_choice(
                            name="주석",
                            value="프붕주석"
                        ),
                        create_choice(
                            name="코더",
                            value="프붕코더"
                        ),
                        create_choice(
                            name="코드",
                            value="프붕코드"
                        ),
                        create_choice(
                            name="버그",
                            value="프붕버그"
                        ),
                        create_choice(
                            name="코딩중",
                            value="프붕코딩중"
                        )
                        ]
                    )
                ])
    async def _프붕(self, ctx, 내용: str):
        if 내용 == "프붕망코드":
            embed=discord.Embed(description="프붕망코드", color=embed_color)
            embed.set_image(url="https://i.ibb.co/0F4M7GY/vmqndakdzhem.png")
            await ctx.send(embed=embed)
        elif 내용 == "프붕메모리":
            embed=discord.Embed(description="프붕메모리", color=embed_color)
            embed.set_image(url="https://i.ibb.co/wMRrmgr/vmqndapahfl.png")
            await ctx.send(embed=embed)
        elif 내용 == "프붕몇번":
            embed=discord.Embed(description="프붕몇번", color=embed_color)
            embed.set_image(url="https://i.ibb.co/hCRrn4P/vmqndaucqjs.png")
            await ctx.send(embed=embed)
        elif 내용 == "프붕책":
            embed=discord.Embed(description="프붕책", color=embed_color)
            embed.set_image(url="https://i.ibb.co/RbG2qVh/vmqndcor.png")
            await ctx.send(embed=embed)
        elif 내용 == "프붕언어탓":
            embed=discord.Embed(description="프붕언어탓", color=embed_color)
            embed.set_image(url="https://i.ibb.co/3kK7WxY/vmqnddjsdjxkt.png")
            await ctx.send(embed=embed)
        elif 내용 == "프붕따봉":
            embed=discord.Embed(description="프붕따봉", color=embed_color)
            embed.set_image(url="https://i.ibb.co/j5Z716k/vmqndEkqhd.png")
            await ctx.send(embed=embed)
        elif 내용 == "프붕밤샘":
            embed=discord.Embed(description="프붕밤샘", color=embed_color)
            embed.set_image(url="https://i.ibb.co/b1YZGgZ/vmqndqkatoa.png")
            await ctx.send(embed=embed)
        elif 내용 == "프붕반복":
            embed=discord.Embed(description="프붕반복", color=embed_color)
            embed.set_image(url="https://i.ibb.co/L0Bhxg2/vmqndqksqhr.png")
            await ctx.send(embed=embed)
        elif 내용 == "프붕스파게티":
            embed=discord.Embed(description="프붕스파게티", color=embed_color)
            embed.set_image(url="https://i.ibb.co/G0hVxBN/vmqndtmvkrpxl.png")
            await ctx.send(embed=embed)
        elif 내용 == "프붕생각":
            embed=discord.Embed(description="프붕생각", color=embed_color)
            embed.set_image(url="https://i.ibb.co/3Ytjz7F/vmqndtodrkr.png")
            await ctx.send(embed=embed)
        elif 내용 == "프붕주석":
            embed=discord.Embed(description="프붕주석", color=embed_color)
            embed.set_image(url="https://i.ibb.co/HFj0f48/vmqndwntjr.png")
            await ctx.send(embed=embed)
        elif 내용 == "프붕코더":
            embed=discord.Embed(description="프붕코더", color=embed_color)
            embed.set_image(url="https://i.ibb.co/RT04zxq/vmqndzhej.png")
            await ctx.send(embed=embed)
        elif 내용 == "프붕코드":
            embed=discord.Embed(description="프붕코드", color=embed_color)
            embed.set_image(url="https://i.ibb.co/PGJHPNz/vmqndzhem.png")
            await ctx.send(embed=embed)
        elif 내용 == "프붕버그":
            embed=discord.Embed(description="프붕버그", color=embed_color)
            embed.set_image(url="https://i.ibb.co/PjnzMv1/vmqndqjrm.png")
            await ctx.send(embed=embed)
        elif 내용 == "프붕코딩중":
            embed=discord.Embed(description="프붕코딩중", color=embed_color)
            embed.set_image(url="https://i.ibb.co/D5zF9FN/vmqndzheldwnd.png")
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(프붕(client))