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

class 로고(commands.Cog):
    def __init__(self, client):
        self.client = client
    @cog_ext.cog_slash(name="로고", 
            description="📁 로고",
            guild_ids=guild_ids,
            options=[
                create_option(
                    name="상표명",
                    description="무슨 로고를 불러올까요?",
                    option_type=3,
                    required=True,
                    choices=[
                        create_choice(
                            name="HTML",
                            value="HTML"
                        ),
                        create_choice(
                            name="CSS",
                            value="CSS"
                        ),
                            create_choice(
                            name="깃헙",
                            value="깃헙"
                        ),
                        create_choice(
                            name="븩스븨",
                            value="븩스븨"
                        ),
                        create_choice(
                            name="비주얼스튜디오",
                            value="비주얼스튜디오"
                        ),
                        create_choice(
                            name="아래아한글",
                            value="아래아한글"
                        ),
                        create_choice(
                            name="애플",
                            value="애플"
                        ),
                        create_choice(
                            name="에이펙스레전드",
                            value="에이펙스레전드"
                        ),
                        create_choice(
                            name="오버워치",
                            value="오버워치"
                        ),
                        create_choice(
                            name="온라인클래스",
                            value="온라인클래스"
                        ),
                        create_choice(
                            name="유비소프트",
                            value="유비소프트"
                        ),
                        create_choice(
                            name="카카오톡",
                            value="카카오톡"
                        ),
                        create_choice(
                            name="키네마스터",
                            value="키네마스터"
                        ),
                        create_choice(
                            name="IE",
                            value="IE"
                        ),
                        create_choice(
                            name="구글",
                            value="구글"
                        ),
                        create_choice(
                            name="클래스룸",
                            value="클래스룸"
                        ),
                        create_choice(
                            name="레인보우식스시즈",
                            value="레인보우식스시즈"
                        ),
                        create_choice(
                            name="교육부",
                            value="교육부"
                        ),
                        create_choice(
                            name="삼성",
                            value="삼성"
                        ),
                        create_choice(
                            name="씽큐",
                            value="씽큐"
                        )
                    ]
                )
            ]
    )
    async def _로고(self, ctx, 상표명: str):
        if 상표명 == "HTML":
            embed=discord.Embed(description="HTML로고", color=embed_color)
            embed.set_image(url="https://i.ibb.co/h9wqbQN/html.png")
            await ctx.send(embed=embed)
        elif 상표명 == "CSS":
            embed=discord.Embed(description="CSS로고", color=embed_color)
            embed.set_image(url="https://i.ibb.co/1vnQBW2/css.png")
            await ctx.send(embed=embed)
        elif 상표명 == "깃헙":
            embed=discord.Embed(description="깃헙", color=embed_color)
            embed.set_image(url="https://i.ibb.co/6B6yDjF/rltgjqm.png")
            await ctx.send(embed=embed)
        elif 상표명 == "븩스븨":
            embed=discord.Embed(description="븩스븨", color=embed_color)
            embed.set_image(url="https://i.ibb.co/9hG8Qfs/qmlrtmqml.png")
            await ctx.send(embed=embed)
        elif 상표명 == "비주얼스튜디오":
            embed=discord.Embed(description="비주얼스튜디오", color=embed_color)
            embed.set_image(url="https://i.ibb.co/yRsStWm/qlwndjftmxbeldh.png")
            await ctx.send(embed=embed)
        elif 상표명 == "아래아한글":
            embed=discord.Embed(description="아래아한글", color=embed_color)
            embed.set_image(url="https://i.ibb.co/WskCxmT/dkfodkgksrmf.png")
            await ctx.send(embed=embed)
        elif 상표명 == "애플":
            embed=discord.Embed(description="애플", color=embed_color)
            embed.set_image(url="https://i.ibb.co/TqQKZkV/dovmf.png")
            await ctx.send(embed=embed)
        elif 상표명 == "에이펙스레전드":
            embed=discord.Embed(description="에이펙스레전드", color=embed_color)
            embed.set_image(url="https://i.ibb.co/VjqNrck/dpdlvprtmfpwjsem.png")
            await ctx.send(embed=embed)
        elif 상표명 == "오버워치":
            embed=discord.Embed(description="오버워치", color=embed_color)
            embed.set_image(url="https://i.ibb.co/JBJYpkq/dhqjdnjcl.png")
            await ctx.send(embed=embed)
        elif 상표명 == "온라인클래스":
            embed=discord.Embed(description="온라인클래스", color=embed_color)
            embed.set_image(url="https://i.ibb.co/gdv5Smh/dhsfkdlszmffotm.png")
            await ctx.send(embed=embed)
        elif 상표명 == "유비소프트":
            embed=discord.Embed(description="유비소프트", color=embed_color)
            embed.set_image(url="https://i.ibb.co/XDFLxrR/dbqlthvmxm.png")
            await ctx.send(embed=embed)
        elif 상표명 == "카카오톡":
            embed=discord.Embed(description="카카오톡", color=embed_color)
            embed.set_image(url="https://i.ibb.co/FbQHg1p/zkzkdhxhr.png")
            await ctx.send(embed=embed)
        elif 상표명 == "키네마스터":
            embed=discord.Embed(description="키네마스터", color=embed_color)
            embed.set_image(url="https://i.ibb.co/F70Kd9W/zlspaktmxj.png")
            await ctx.send(embed=embed)
        elif 상표명 == "IE":
            embed=discord.Embed(description="IE", color=embed_color)
            embed.set_image(url="https://i.ibb.co/3sZfcrp/IE.png")
            await ctx.send(embed=embed)
        elif 상표명 == "구글":
            embed=discord.Embed(description="구글", color=embed_color)
            embed.set_image(url="https://i.ibb.co/dj9cGG5/rnrmf.png")
            await ctx.send(embed=embed)
        elif 상표명 == "클래스룸":
            embed=discord.Embed(description="클래스룸", color=embed_color)
            embed.set_image(url="https://i.ibb.co/phd8R21/zmffotmfna.png")
            await ctx.send(embed=embed)
        elif 상표명 == "레인보우식스시즈":
            embed=discord.Embed(description="레인보우식스시즈", color=embed_color)
            embed.set_image(url="https://i.ibb.co/X8wFW3q/fpdlsqhdntlrtmtlwm.png")
            await ctx.send(embed=embed)
        elif 상표명 == "마인크래프트":
            embed=discord.Embed(description="마인크래프트", color=embed_color)
            embed.set_image(url="https://i.ibb.co/VM3Fm3W/akdlszmfovmxm.png")
            await ctx.send(embed=embed)
        elif 상표명 == "교육부":
            embed=discord.Embed(description="교육부", color=embed_color)
            embed.set_image(url="https://i.ibb.co/Qf6MD1X/rydbrqn.png")
            await ctx.send(embed=embed)
        elif 상표명 == "삼성":
                embed=discord.Embed(description="삼성", color=embed_color)
                embed.set_image(url="https://i.ibb.co/zxt3TFK/tkatjd.png")
                await ctx.send(embed=embed)
        elif 상표명 == "씽큐":
                embed=discord.Embed(description="씽큐", color=embed_color)
                embed.set_image(url="https://i.ibb.co/s1mbysr/Tldzb.png")
                await ctx.send(embed=embed)


def setup(client):
    client.add_cog(로고(client))