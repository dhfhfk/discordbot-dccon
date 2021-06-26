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

class 레식(commands.Cog):
    def __init__(self, client):
        self.client = client
    @cog_ext.cog_slash(name="레식", 
                description="📁 레인보우식스시즈 디시콘",
                guild_ids=guild_ids,
                options=[
                    create_option(
                        name="내용",
                        description="무슨 내용인가요?",
                        option_type=3,
                        required=True,
                        choices=[
                            create_choice(
                                name="레이저",
                                value="레식레이저"
                            ),
                            create_choice(
                                name="양심",
                                value="레식양심"
                            ),
                            create_choice(
                                name="알람",
                                value="레식알람"
                            ),
                            create_choice(
                                name="이래도",
                                value="레식이래도"
                            ),
                            create_choice(
                                name="웰컴",
                                value="레식웰컴"
                            ),
                            create_choice(
                                name="운",
                                value="레식운"
                            ),
                            create_choice(
                                name="돌려줘",
                                value="레식돌려줘"
                            ),
                            create_choice(
                                name="두뇌",
                                value="레식두뇌"
                            ),
                            create_choice(
                                name="레딧",
                                value="레식레딧"
                            ),
                            create_choice(
                                name="헤드",
                                value="레식헤드"
                            ),
                            create_choice(
                                name="발각",
                                value="레식발각"
                            ),
                            create_choice(
                                name="블아",
                                value="레식블아"
                            ),
                            create_choice(
                                name="불만",
                                value="레식불만"
                            ),
                            create_choice(
                                name="밸런스",
                                value="레식밸런스"
                            ),
                            create_choice(
                                name="감자",
                                value="레식감자"
                            ),
                            create_choice(
                                name="가라킥",
                                value="레식가라킥"
                            ),
                            create_choice(
                                name="ㄴㅇㄱ",
                                value="레식ㄴㅇㄱ"
                            ),
                            create_choice(
                                name="신총",
                                value="레식신총"
                            ),
                            create_choice(
                                name="스폰킬",
                                value="레식스폰킬"
                            ),
                            create_choice(
                                name="핑구",
                                value="레식핑구"
                            ),
                            create_choice(
                                name="피자",
                                value="레식피자"
                            ),
                            create_choice(
                                name="팩깡",
                                value="레식팩깡"
                            ),
                            create_choice(
                                name="재탕",
                                value="레식재탕"
                            )
                        ]
                    )
                ])
    async def _레식(self, ctx, 내용: str):
        if 내용 == "레식레이저":
            embed=discord.Embed(description="레식레이저", color=embed_color)
            embed.set_image(url="https://i.ibb.co/6tpggTT/fptlrfpdlwj.png")
            await ctx.send(embed=embed)
        elif 내용 == "레식양심":
            embed=discord.Embed(description="레식양심", color=embed_color)
            embed.set_image(url="https://i.ibb.co/MfNR1Y0/fptlrdidtla.png")
            await ctx.send(embed=embed)
        elif 내용 == "레식알람":
            embed=discord.Embed(description="레식알람", color=embed_color)
            embed.set_image(url="https://i.ibb.co/Dz4HfVW/fptlrdkffka.png")
            await ctx.send(embed=embed)
        elif 내용 == "레식이래도":
            embed=discord.Embed(description="레식이래도", color=embed_color)
            embed.set_image(url="https://i.ibb.co/mzvdCLC/fptlrdlfoeh.png")
            await ctx.send(embed=embed)
        elif 내용 == "레식웰컴":
            embed=discord.Embed(description="레식웰컴", color=embed_color)
            embed.set_image(url="https://i.ibb.co/fQYdC4N/fptlrdnpfzja.png")
            await ctx.send(embed=embed)
        elif 내용 == "레식운":
            embed=discord.Embed(description="레식운", color=embed_color)
            embed.set_image(url="https://i.ibb.co/8XQTXQ3/fptlrdns.png")
            await ctx.send(embed=embed)
        elif 내용 == "레식돌려줘":
            embed=discord.Embed(description="레식돌려줘", color=embed_color)
            embed.set_image(url="https://i.ibb.co/GQSm2kR/fptlrehffuwnj.png")
            await ctx.send(embed=embed)
        elif 내용 == "레식두뇌":
            embed=discord.Embed(description="레식두뇌", color=embed_color)
            embed.set_image(url="https://i.ibb.co/yqy46ZB/fptlrenshl.png")
            await ctx.send(embed=embed)
        elif 내용 == "레식레딧":
            embed=discord.Embed(description="레식레딧", color=embed_color)
            embed.set_image(url="https://i.ibb.co/2ZNNLJH/fptlrfpelt.png")
            await ctx.send(embed=embed)
        elif 내용 == "레식헤드":
            embed=discord.Embed(description="레식헤드", color=embed_color)
            embed.set_image(url="https://i.ibb.co/T0Sd3Lq/fptlrgpem.png")
            await ctx.send(embed=embed)
        elif 내용 == "레식발각":
            embed=discord.Embed(description="레식발각", color=embed_color)
            embed.set_image(url="https://i.ibb.co/0fDxhXD/fptlrqkfrkr.png")
            await ctx.send(embed=embed)
        elif 내용 == "레식블아":
            embed=discord.Embed(description="레식블아", color=embed_color)
            embed.set_image(url="https://i.ibb.co/GxxQPz5/fptlrqmfdk.png")
            await ctx.send(embed=embed)
        elif 내용 == "레식불만":
            embed=discord.Embed(description="레식불만", color=embed_color)
            embed.set_image(url="https://i.ibb.co/Rv5ZNDX/fptlrqnfaks.png")
            await ctx.send(embed=embed)
        elif 내용 == "레식밸런스":
            embed=discord.Embed(description="레식밸런스", color=embed_color)
            embed.set_image(url="https://i.ibb.co/FHHf7C6/fptlrqoffjstm.png")
            await ctx.send(embed=embed)
        elif 내용 == "레식감자":
            embed=discord.Embed(description="레식감자", color=embed_color)
            embed.set_image(url="https://i.ibb.co/vP9TfCD/fptlrrkawk.png")
            await ctx.send(embed=embed)
        elif 내용 == "레식가라킥":
            embed=discord.Embed(description="레식가라킥", color=embed_color)
            embed.set_image(url="https://i.ibb.co/3MhQshn/fptlrrkfkzlr.png")
            await ctx.send(embed=embed)
        elif 내용 == "레식ㄴㅇㄱ":
            embed=discord.Embed(description="레식ㄴㅇㄱ", color=embed_color)
            embed.set_image(url="https://i.ibb.co/t4WKsMZ/fptlrsdr.png")
            await ctx.send(embed=embed)
        elif 내용 == "레식신총":
            embed=discord.Embed(description="레식신총", color=embed_color)
            embed.set_image(url="https://i.ibb.co/DbKTndH/fptlrtlschd.png")
            await ctx.send(embed=embed)
        elif 내용 == "레식스폰킬":
            embed=discord.Embed(description="레식스폰킬", color=embed_color)
            embed.set_image(url="https://i.ibb.co/6RcwndL/fptlrtmvhszlf.png")
            await ctx.send(embed=embed)
        elif 내용 == "레식핑구":
            embed=discord.Embed(description="레식핑구", color=embed_color)
            embed.set_image(url="https://i.ibb.co/ZYfCfWx/fptlrvldrn.png")
            await ctx.send(embed=embed)
        elif 내용 == "레식피자":
            embed=discord.Embed(description="레식피자", color=embed_color)
            embed.set_image(url="https://i.ibb.co/pLN052L/fptlrvlwk.png")
            await ctx.send(embed=embed)
        elif 내용 == "레식팩깡":
            embed=discord.Embed(description="레식팩깡", color=embed_color)
            embed.set_image(url="https://i.ibb.co/fkbvSzn/fptlrvorRkd.png")
            await ctx.send(embed=embed)
        elif 내용 == "레식재탕":
            embed=discord.Embed(description="레식재탕", color=embed_color)
            embed.set_image(url="https://i.ibb.co/zG7prwp/fptlrwoxkd.png")
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(레식(client))