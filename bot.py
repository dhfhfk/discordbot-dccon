from discord_slash.utils.manage_commands import create_option, create_choice
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash import cog_ext
from discord import DMChannel
import datetime
import re
import asyncio
import os

client = discord.Client(intents=discord.Intents.all(), activity = discord.Game(name="명령어마다 파일 배정 코딩"))
slash = SlashCommand(client, sync_commands=True)

@client.event
async def on_ready():
    print("준비된!")

victim_id = (int(595824909473808403))
guild_ids = [victim_id]

confirm_emoji = '\N{Heavy Large Circle}'
deny_emoji = '\N{Cross Mark}'
skip_emoji = '\N{Black Right-Pointing Double Triangle with Vertical Bar}'

@slash.slash(name="우리핵", 
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
                        ),
                    ]
                )
            ])
async def test(ctx, 내용: str):
    if 내용 == "우리핵안무":
        embed=discord.Embed(description="우리핵안무", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/0tJN50r/dnflgordksan.gif")
        await ctx.send(embed=embed)
        

    elif 내용 == "우리핵안녕":
        embed=discord.Embed(description="우리핵안녕", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/RgfHT8J/dnflgordkssud.gif")
        await ctx.send(embed=embed)
        

    elif 내용 == "우리핵드럼":
        embed=discord.Embed(description="우리핵드럼", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/QccRgHK/dnflgoremfja.gif")
        await ctx.send(embed=embed)
        

    elif 내용 == "우리핵박수":
        embed=discord.Embed(description="우리핵박수", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/0n38dCT/dnflgorqkrtn.gif")
        await ctx.send(embed=embed)

    elif 내용 == "우리핵갸우뚱":
        embed=discord.Embed(description="우리핵갸우뚱", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/XZ9SBzw/dnflgorridnEnd.gif")
        await ctx.send(embed=embed)

@slash.slash(name="로고", 
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
            ])
async def test(ctx, 상표명: str):
    if 상표명 == "HTML":
        embed=discord.Embed(description="HTML로고", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/h9wqbQN/html.png")
        await ctx.send(embed=embed)
    elif 상표명 == "CSS":
        embed=discord.Embed(description="CSS로고", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/1vnQBW2/css.png")
        await ctx.send(embed=embed)
    elif 상표명 == "깃헙":
        embed=discord.Embed(description="깃헙", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/6B6yDjF/rltgjqm.png")
        await ctx.send(embed=embed)
    elif 상표명 == "븩스븨":
        embed=discord.Embed(description="븩스븨", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/9hG8Qfs/qmlrtmqml.png")
        await ctx.send(embed=embed)
    elif 상표명 == "비주얼스튜디오":
        embed=discord.Embed(description="비주얼스튜디오", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/yRsStWm/qlwndjftmxbeldh.png")
        await ctx.send(embed=embed)
    elif 상표명 == "아래아한글":
        embed=discord.Embed(description="아래아한글", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/WskCxmT/dkfodkgksrmf.png")
        await ctx.send(embed=embed)
    elif 상표명 == "애플":
        embed=discord.Embed(description="애플", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/TqQKZkV/dovmf.png")
        await ctx.send(embed=embed)
    elif 상표명 == "에이펙스레전드":
        embed=discord.Embed(description="에이펙스레전드", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/VjqNrck/dpdlvprtmfpwjsem.png")
        await ctx.send(embed=embed)
    elif 상표명 == "오버워치":
        embed=discord.Embed(description="오버워치", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/JBJYpkq/dhqjdnjcl.png")
        await ctx.send(embed=embed)
    elif 상표명 == "온라인클래스":
        embed=discord.Embed(description="온라인클래스", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/gdv5Smh/dhsfkdlszmffotm.png")
        await ctx.send(embed=embed)
    elif 상표명 == "유비소프트":
        embed=discord.Embed(description="유비소프트", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/XDFLxrR/dbqlthvmxm.png")
        await ctx.send(embed=embed)
    elif 상표명 == "카카오톡":
        embed=discord.Embed(description="카카오톡", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/FbQHg1p/zkzkdhxhr.png")
        await ctx.send(embed=embed)
    elif 상표명 == "키네마스터":
        embed=discord.Embed(description="키네마스터", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/F70Kd9W/zlspaktmxj.png")
        await ctx.send(embed=embed)
    elif 상표명 == "IE":
        embed=discord.Embed(description="IE", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/3sZfcrp/IE.png")
        await ctx.send(embed=embed)
    elif 상표명 == "구글":
        embed=discord.Embed(description="구글", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/dj9cGG5/rnrmf.png")
        await ctx.send(embed=embed)
    elif 상표명 == "클래스룸":
        embed=discord.Embed(description="클래스룸", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/phd8R21/zmffotmfna.png")
        await ctx.send(embed=embed)
    elif 상표명 == "레인보우식스시즈":
        embed=discord.Embed(description="레인보우식스시즈", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/X8wFW3q/fpdlsqhdntlrtmtlwm.png")
        await ctx.send(embed=embed)
    elif 상표명 == "마인크래프트":
        embed=discord.Embed(description="마인크래프트", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/VM3Fm3W/akdlszmfovmxm.png")
        await ctx.send(embed=embed)
    elif 상표명 == "교육부":
        embed=discord.Embed(description="교육부", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/Qf6MD1X/rydbrqn.png")
        await ctx.send(embed=embed)
    elif 상표명 == "삼성":
            embed=discord.Embed(description="삼성", color=0x4ac8c7)
            embed.set_image(url="https://i.ibb.co/zxt3TFK/tkatjd.png")
            await ctx.send(embed=embed)
    elif 상표명 == "씽큐":
            embed=discord.Embed(description="씽큐", color=0x4ac8c7)
            embed.set_image(url="https://i.ibb.co/s1mbysr/Tldzb.png")
            await ctx.send(embed=embed)

@slash.slash(name="특", 
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
            ])
async def test(ctx, 내용: str):
    if 내용 == "디자이너특":
            embed=discord.Embed(description="디자이너특", color=0x4ac8c7)
            embed.set_image(url="https://i.ibb.co/JcncbDj/elwkdlsjxmr.gif")
            await ctx.send(embed=embed)
    elif 내용 == "디자이너특2":
            embed=discord.Embed(description="디자이너특2", color=0x4ac8c7)
            embed.set_image(url="https://i.ibb.co/9n6x4hQ/elwkdlsjxmr2.png")
            await ctx.send(embed=embed)
    elif 내용 == "CSS특":
            embed=discord.Embed(description="CSS특", color=0x4ac8c7)
            embed.set_image(url="https://i.ibb.co/6Js7Mty/CSSxmr.gif")
            await ctx.send(embed=embed)
    elif 내용 == "CSS특2":
            embed=discord.Embed(description="CSS특2", color=0x4ac8c7)
            embed.set_image(url="https://i.ibb.co/gFr6mXx/CSS2.gif")
            await ctx.send(embed=embed)

@slash.slash(name="앵무", 
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
async def test(ctx, 내용: str):
    if 내용 == "앵무댄스":
        embed=discord.Embed(description="앵무댄스", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/gM3pJQx/dodaneostm.gif")
        await ctx.send(embed=embed)
    elif 내용 == "앵무선글":
        embed=discord.Embed(description="앵무선글", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/m6txyNv/dodantjsrmf.gif")
        await ctx.send(embed=embed)
    elif 내용 == "앵무팝콘":
        embed=discord.Embed(description="앵무팝콘", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/DfBNjpM/dodanvkqzhs.gif")
        await ctx.send(embed=embed)
    elif 내용 == "앵무혼란":
        embed=discord.Embed(description="앵무혼란", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/vsTGdyZ/dodanghsfks.gif")
        await ctx.send(embed=embed)

@slash.slash(name="RGB", 
            description="📁 RGB 디시콘",
            guild_ids=guild_ids,
            options=[
                create_option(
                    name="내용",
                    description="무슨 내용인가요?",
                    option_type=3,
                    required=True,
                    choices=[
                    create_choice(
                        name="뽕",
                        value="RGB뽕"
                    ),
                    create_choice(
                        name="그자체",
                        value="RGB그자체"
                    )
                    ]
                )
            ])
async def test(ctx, 내용: str):
    if 내용 == "RGB뽕":
        embed=discord.Embed(description="RGB뽕", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/Z65ttZx/RGBQhd.gif")
        await ctx.send(embed=embed)
    elif 내용 == "RGB그자체":
        embed=discord.Embed(description="RGB그자체", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/FY3vFF9/RGBrmwkcp.gif")
        await ctx.send(embed=embed)

@slash.slash(name="사수", 
            description="📁 리사수 디시콘",
            guild_ids=guild_ids,
            options=[
                create_option(
                    name="내용",
                    description="무슨 내용인가요?",
                    option_type=3,
                    required=True,
                    choices=[
                        create_choice(
                            name="웃음",
                            value="사수웃음"
                        ),
                        create_choice(
                            name="화남",
                            value="사수화남"
                        ),
                        create_choice(
                            name="자랑",
                            value="사수자랑"
                        ),
                        create_choice(
                            name="썬글",
                            value="사수썬글"
                        ),
                        create_choice(
                            name="클럽",
                            value="사수클럽"
                        )
                    ]
                )
            ])
async def test(ctx, 내용: str):
    if 내용 == "사수웃음":
        embed=discord.Embed(description="사수웃음", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/N1rGd22/tktndntdma.gif")
        await ctx.send(embed=embed)
    elif 내용 == "사수화남":
        embed=discord.Embed(description="사수화남", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/6WD90vm/tktnghkska.gif")
        await ctx.send(embed=embed)
    elif 내용 == "사수자랑":
        embed=discord.Embed(description="사수자랑", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/nncpZXx/tktnwkfkd.gif")
        await ctx.send(embed=embed)
    elif 내용 == "사수썬글":
        embed=discord.Embed(description="사수썬글", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/sP9nZTV/tktn-Tjsrmf.gif")
        await ctx.send(embed=embed)
    elif 내용 == "사수클럽":
        embed=discord.Embed(description="사수클럽", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/DwHvbhs/tktnzmffjq.gif")
        await ctx.send(embed=embed)

@slash.slash(name="냥", 
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
async def test(ctx, 내용: str):
    if 내용 == "냥경악":
        embed=discord.Embed(description="냥경악", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/gDB9mzd/sidruddkr.gif")
        await ctx.send(embed=embed)
        
    elif 내용 == "냥슬픔":
        embed=discord.Embed(description="냥슬픔", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/VxZ3g53/sidtmfvma.gif")
        await ctx.send(embed=embed)
        
    elif 내용 == "냥선글":
        embed=discord.Embed(description="냥선글", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/fXgGK2s/sidtjsrmf.gif")
        await ctx.send(embed=embed)
        
    elif 내용 == "냥정색":
        embed=discord.Embed(description="냥정색", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/d43H7m6/sidwjdtor.gif")
        await ctx.send(embed=embed)

@slash.slash(name="둘리", 
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
async def test(ctx, 내용: str):
    if 내용 == "둘리초능력":
        embed=discord.Embed(description="둘리초능력", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/brTzWWr/enfflchsmdfur.png")
        await ctx.send(embed=embed)
    elif 내용 == "둘리처신":
        embed=discord.Embed(description="둘리처신", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/68bkXKD/enfflcjtls.png")
        await ctx.send(embed=embed)
    elif 내용 == "둘리웃음":
        embed=discord.Embed(description="둘리웃음", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/GTzqBwp/enffldntdma.png")
        await ctx.send(embed=embed)
    elif 내용 == "둘리호잇":
        embed=discord.Embed(description="둘리호잇", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/jfPMZ6t/enfflghdlt.png")
        await ctx.send(embed=embed)
    elif 내용 == "둘리흑우":
        embed=discord.Embed(description="둘리흑우", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/Cwy8nSM/enfflgmrdn.png")
        await ctx.send(embed=embed)
    elif 내용 == "둘리꼴받":
        embed=discord.Embed(description="둘리꼴받", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/ZGNqMdT/enfflRhfqke.png")
        await ctx.send(embed=embed)
    elif 내용 == "둘리나가":
        embed=discord.Embed(description="둘리나가", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/nDTgfsR/enfflskrk.png")
        await ctx.send(embed=embed)
    elif 내용 == "둘리냄새":
        embed=discord.Embed(description="둘리냄새", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/LQ6TRk3/enfflsoato.png")
        await ctx.send(embed=embed)
    elif 내용 == "둘리성능":
        embed=discord.Embed(description="둘리성능", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/KxWvjMF/enffltjdsmd.png")
        await ctx.send(embed=embed)
    elif 내용 == "둘리선넘네":
        embed=discord.Embed(description="둘리선넘네", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/2N1PtPW/enffltjssjasp.png")
        await ctx.send(embed=embed)
    elif 내용 == "둘리싯팔":
        embed=discord.Embed(description="둘리싯팔", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/y6NxGJK/enffltltvkf.png")
        await ctx.send(embed=embed)
    elif 내용 == "둘리좋지":
        embed=discord.Embed(description="둘리좋지", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/2vrRB9D/enfflwhgwl.png")
        await ctx.send(embed=embed)
    elif 내용 == "둘리정신":
        embed=discord.Embed(description="둘리정신", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/5s9GtMr/enfflwjdtls.png")
        await ctx.send(embed=embed)
    elif 내용 == "둘리죽상":
        embed=discord.Embed(description="둘리죽상", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/3vyJf3X/enfflwnrtkd.png")
        await ctx.send(embed=embed)

@slash.slash(name="믿거", 
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
async def test(ctx, 내용: str):
    if 내용 == "믿거애":
        embed=discord.Embed(description="믿거애", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/ByvWfmF/alerjdo.png")
        await ctx.send(embed=embed)
    elif 내용 == "믿거앱":
        embed=discord.Embed(description="믿거앱", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/VV3Xzth/alerjdoq.png")
        await ctx.send(embed=embed)
    elif 내용 == "믿거한":
        embed=discord.Embed(description="믿거한", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/Qbn3w3Q/alerjgks.png")
        await ctx.send(embed=embed)
    elif 내용 == "믿거시":
        embed=discord.Embed(description="믿거시", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/yYspgQf/alerjtl.png")
        await ctx.send(embed=embed)

@slash.slash(name="에펙", 
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
async def test(ctx, 내용: str):
    if 내용 == "에펙모잠비크":
        embed=discord.Embed(description="에펙모잠비크", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/Zz4cNgc/dpvprahwkaqlzm.png")
        await ctx.send(embed=embed)
    elif 내용 == "에펙무섭":
        embed=discord.Embed(description="에펙무섭", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/F4vXLqF/dpvprantjq.png")
        await ctx.send(embed=embed)
    elif 내용 == "에펙아크스타":
        embed=discord.Embed(description="에펙아크스타", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/m4h4R5k/dpvprdkzmtmxk.png")
        await ctx.send(embed=embed)
    elif 내용 == "에펙있었는데요":
        embed=discord.Embed(description="에펙있었는데요", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/CmZwDHG/dpvprdlTdjTsms.png")
        await ctx.send(embed=embed)
    elif 내용 == "에펙시도":
        embed=discord.Embed(description="에펙시도", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/z23pdxp/dpvprtleh.png")
        await ctx.send(embed=embed)
    elif 내용 == "에펙전설":
        embed=discord.Embed(description="에펙전설", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/3WJTBys/dpvprwjstjf.png")
        await ctx.send(embed=embed)
    elif 내용 == "에펙태보킥":
        embed=discord.Embed(description="에펙태보킥", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/mDc9YKj/dpvprxoqhzlr.png")
        await ctx.send(embed=embed)
    elif 내용 == "에펙뱀부":
        embed=discord.Embed(description="에펙뱀부", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/HBbzskp/dpvprqoaqn.png")
        await ctx.send(embed=embed)
    elif 내용 == "에펙고뱀부":
        embed=discord.Embed(description="에펙고뱀부", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/pZmBY2F/dpvprrhqoaqn.png")
        await ctx.send(embed=embed)

@slash.slash(name="레식", 
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
async def test(ctx, 내용: str):
    if 내용 == "레식레이저":
        embed=discord.Embed(description="레식레이저", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/6tpggTT/fptlrfpdlwj.png")
        await ctx.send(embed=embed)
    elif 내용 == "레식양심":
        embed=discord.Embed(description="레식양심", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/MfNR1Y0/fptlrdidtla.png")
        await ctx.send(embed=embed)
    elif 내용 == "레식알람":
        embed=discord.Embed(description="레식알람", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/Dz4HfVW/fptlrdkffka.png")
        await ctx.send(embed=embed)
    elif 내용 == "레식이래도":
        embed=discord.Embed(description="레식이래도", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/mzvdCLC/fptlrdlfoeh.png")
        await ctx.send(embed=embed)
    elif 내용 == "레식웰컴":
        embed=discord.Embed(description="레식웰컴", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/fQYdC4N/fptlrdnpfzja.png")
        await ctx.send(embed=embed)
    elif 내용 == "레식운":
        embed=discord.Embed(description="레식운", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/8XQTXQ3/fptlrdns.png")
        await ctx.send(embed=embed)
    elif 내용 == "레식돌려줘":
        embed=discord.Embed(description="레식돌려줘", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/GQSm2kR/fptlrehffuwnj.png")
        await ctx.send(embed=embed)
    elif 내용 == "레식두뇌":
        embed=discord.Embed(description="레식두뇌", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/yqy46ZB/fptlrenshl.png")
        await ctx.send(embed=embed)
    elif 내용 == "레식레딧":
        embed=discord.Embed(description="레식레딧", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/2ZNNLJH/fptlrfpelt.png")
        await ctx.send(embed=embed)
    elif 내용 == "레식헤드":
        embed=discord.Embed(description="레식헤드", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/T0Sd3Lq/fptlrgpem.png")
        await ctx.send(embed=embed)
    elif 내용 == "레식발각":
        embed=discord.Embed(description="레식발각", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/0fDxhXD/fptlrqkfrkr.png")
        await ctx.send(embed=embed)
    elif 내용 == "레식블아":
        embed=discord.Embed(description="레식블아", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/GxxQPz5/fptlrqmfdk.png")
        await ctx.send(embed=embed)
    elif 내용 == "레식불만":
        embed=discord.Embed(description="레식불만", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/Rv5ZNDX/fptlrqnfaks.png")
        await ctx.send(embed=embed)
    elif 내용 == "레식밸런스":
        embed=discord.Embed(description="레식밸런스", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/FHHf7C6/fptlrqoffjstm.png")
        await ctx.send(embed=embed)
    elif 내용 == "레식감자":
        embed=discord.Embed(description="레식감자", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/vP9TfCD/fptlrrkawk.png")
        await ctx.send(embed=embed)
    elif 내용 == "레식가라킥":
        embed=discord.Embed(description="레식가라킥", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/3MhQshn/fptlrrkfkzlr.png")
        await ctx.send(embed=embed)
    elif 내용 == "레식ㄴㅇㄱ":
        embed=discord.Embed(description="레식ㄴㅇㄱ", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/t4WKsMZ/fptlrsdr.png")
        await ctx.send(embed=embed)
    elif 내용 == "레식신총":
        embed=discord.Embed(description="레식신총", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/DbKTndH/fptlrtlschd.png")
        await ctx.send(embed=embed)
    elif 내용 == "레식스폰킬":
        embed=discord.Embed(description="레식스폰킬", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/6RcwndL/fptlrtmvhszlf.png")
        await ctx.send(embed=embed)
    elif 내용 == "레식핑구":
        embed=discord.Embed(description="레식핑구", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/ZYfCfWx/fptlrvldrn.png")
        await ctx.send(embed=embed)
    elif 내용 == "레식피자":
        embed=discord.Embed(description="레식피자", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/pLN052L/fptlrvlwk.png")
        await ctx.send(embed=embed)
    elif 내용 == "레식팩깡":
        embed=discord.Embed(description="레식팩깡", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/fkbvSzn/fptlrvorRkd.png")
        await ctx.send(embed=embed)
    elif 내용 == "레식재탕":
        embed=discord.Embed(description="레식재탕", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/zG7prwp/fptlrwoxkd.png")
        await ctx.send(embed=embed)

@slash.slash(name="프붕", 
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
async def test(ctx, 내용: str):
    if 내용 == "프붕망코드":
        embed=discord.Embed(description="프붕망코드", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/0F4M7GY/vmqndakdzhem.png")
        await ctx.send(embed=embed)
    elif 내용 == "프붕메모리":
        embed=discord.Embed(description="프붕메모리", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/wMRrmgr/vmqndapahfl.png")
        await ctx.send(embed=embed)
    elif 내용 == "프붕몇번":
        embed=discord.Embed(description="프붕몇번", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/hCRrn4P/vmqndaucqjs.png")
        await ctx.send(embed=embed)
    elif 내용 == "프붕책":
        embed=discord.Embed(description="프붕책", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/RbG2qVh/vmqndcor.png")
        await ctx.send(embed=embed)
    elif 내용 == "프붕언어탓":
        embed=discord.Embed(description="프붕언어탓", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/3kK7WxY/vmqnddjsdjxkt.png")
        await ctx.send(embed=embed)
    elif 내용 == "프붕따봉":
        embed=discord.Embed(description="프붕따봉", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/j5Z716k/vmqndEkqhd.png")
        await ctx.send(embed=embed)
    elif 내용 == "프붕밤샘":
        embed=discord.Embed(description="프붕밤샘", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/b1YZGgZ/vmqndqkatoa.png")
        await ctx.send(embed=embed)
    elif 내용 == "프붕반복":
        embed=discord.Embed(description="프붕반복", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/L0Bhxg2/vmqndqksqhr.png")
        await ctx.send(embed=embed)
    elif 내용 == "프붕스파게티":
        embed=discord.Embed(description="프붕스파게티", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/G0hVxBN/vmqndtmvkrpxl.png")
        await ctx.send(embed=embed)
    elif 내용 == "프붕생각":
        embed=discord.Embed(description="프붕생각", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/3Ytjz7F/vmqndtodrkr.png")
        await ctx.send(embed=embed)
    elif 내용 == "프붕주석":
        embed=discord.Embed(description="프붕주석", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/HFj0f48/vmqndwntjr.png")
        await ctx.send(embed=embed)
    elif 내용 == "프붕코더":
        embed=discord.Embed(description="프붕코더", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/RT04zxq/vmqndzhej.png")
        await ctx.send(embed=embed)
    elif 내용 == "프붕코드":
        embed=discord.Embed(description="프붕코드", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/PGJHPNz/vmqndzhem.png")
        await ctx.send(embed=embed)
    elif 내용 == "프붕버그":
        embed=discord.Embed(description="프붕버그", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/PjnzMv1/vmqndqjrm.png")
        await ctx.send(embed=embed)
    elif 내용 == "프붕코딩중":
        embed=discord.Embed(description="프붕코딩중", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/D5zF9FN/vmqndzheldwnd.png")
        await ctx.send(embed=embed)

@slash.slash(name="제리", 
            description="📁 제리 디시콘",
            guild_ids=guild_ids,
            options=[
                create_option(
                    name="내용",
                    description="무슨 내용인가요?",
                    option_type=3,
                    required=True,
                    choices=[
                        create_choice(
                            name="메롱",
                            value="제리메롱"
                        ),
                        create_choice(
                            name="처먹",
                            value="제리처먹"
                        ),
                        create_choice(
                            name="띠용",
                            value="제리띠용"
                        ),
                        create_choice(
                            name="화들짝",
                            value="제리화들짝"
                        ),
                        create_choice(
                            name="경악",
                            value="제리경악"
                        ),
                        create_choice(
                            name="쯧쯧",
                            value="제리쯧쯧"
                        ),
                        create_choice(
                            name="끄덕",
                            value="제리끄덕"
                        ),
                        create_choice(
                            name="인사",
                            value="제리인사"
                        ),
                        create_choice(
                            name="폭소",
                            value="제리폭소"
                        )
                    ]
                )
            ])
async def test(ctx, 내용: str):
    if 내용 == "제리메롱":
        embed=discord.Embed(description="제리메롱", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/2ymkqL0/wpflapfhd.gif")
        await ctx.send(embed=embed)
    elif 내용 == "제리처먹":
        embed=discord.Embed(description="제리처먹", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/wsD8mfj/wpflcjajr.gif")
        await ctx.send(embed=embed)
    elif 내용 == "제리띠용":
        embed=discord.Embed(description="제리띠용", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/whdv6J4/wpflEldyd.gif")
        await ctx.send(embed=embed)
    elif 내용 == "제리화들짝":
        embed=discord.Embed(description="제리화들짝", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/qDn4516/wpflghkemfWkr.gif")
        await ctx.send(embed=embed)
    elif 내용 == "제리경악":
        embed=discord.Embed(description="제리경악", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/ngM8DtF/wpflruddkr.gif")
        await ctx.send(embed=embed)
    elif 내용 == "제리쯧쯧":
        embed=discord.Embed(description="제리쯧쯧", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/1rNnyPY/wpflWmtWmt.gif")
        await ctx.send(embed=embed)
    elif 내용 == "제리끄덕":
        embed=discord.Embed(description="제리끄덕", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/dL00Xk6/wpfl-Rmejr.gif")
        await ctx.send(embed=embed)
    elif 내용 == "제리인사":
        embed=discord.Embed(description="제리인사", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/Gs7sNxZ/wpfldlstk2.gif")
        await ctx.send(embed=embed)
    elif 내용 == "제리폭소":
        embed=discord.Embed(description="제리폭소", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/JKxvDfN/wpflvhrth.gif")
        await ctx.send(embed=embed)

@slash.slash(name="컴붕", 
            description="📁 컴퓨터 디시콘",
            guild_ids=guild_ids,
            options=[
                create_option(
                    name="내용",
                    description="무슨 내용인가요?",
                    option_type=3,
                    required=True,
                    choices=[
                        create_choice(
                            name="앱등",
                            value="컴붕앱등"
                        ),
                        create_choice(
                            name="인텔",
                            value="컴붕인텔"
                        ),
                        create_choice(
                            name="RGB",
                            value="컴붕RGB"
                        ),
                        create_choice(
                            name="특가",
                            value="컴붕특가"
                        ),
                        create_choice(
                            name="발열",
                            value="컴붕발열"
                        ),
                    ]
                )
            ])
async def test(ctx, 내용: str):
    if 내용 == "컴붕앱등":
        embed=discord.Embed(description="컴붕앱등", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/jhkPpD2/zjaqnddoqemd.png")
        await ctx.send(embed=embed)
    elif 내용 == "컴붕인텔":
        embed=discord.Embed(description="컴붕인텔", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/8dWKMwh/zjaqnddlsxpf.png")
        await ctx.send(embed=embed)
    elif 내용 == "컴붕RGB":
        embed=discord.Embed(description="컴붕RGB", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/XSLnkk8/zjaqnd-RGB.png")
        await ctx.send(embed=embed)
    elif 내용 == "컴붕특가":
        embed=discord.Embed(description="컴붕특가", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/JK9x5Q3/zjaqndxmrrk.png")
        await ctx.send(embed=embed)
    elif 내용 == "컴붕발열":
        embed=discord.Embed(description="컴붕발열", color=0x4ac8c7)
        embed.set_image(url="https://i.ibb.co/7KzCQ8N/zjaqndqkfduf.png")
        await ctx.send(embed=embed)
        
@slash.slash(name="고티", description=" ", guild_ids=guild_ids)
async def 고티(ctx):
    embed=discord.Embed(description="고티", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/yVYpvGn/rhxl.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="님폰없", description=" ", guild_ids=guild_ids)
async def 님폰없(ctx):
    embed=discord.Embed(description="님폰없", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/BBZY0ZY/slavhsdjqt.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="능지", description=" ", guild_ids=guild_ids)
async def 능지(ctx):
    embed=discord.Embed(description="능지", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/zPhLbCK/smdwl.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="상담", description=" ", guild_ids=guild_ids)
async def 상담(ctx):
    embed=discord.Embed(description="상담", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/FhHh34G/tkdeka.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="사용자", description=" ", guild_ids=guild_ids)
async def 사용자(ctx):
    embed=discord.Embed(description="사용자", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/C0Ny77Q/tkdydwk.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="팟지", description=" ", guild_ids=guild_ids)
async def 팟지(ctx):
    embed=discord.Embed(description="팟지", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/3scVVPh/vktwl.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="라데온", description=" ", guild_ids=guild_ids)
async def 라데온(ctx):
    embed=discord.Embed(description="라데온", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/TgQS38s/fkepdhs.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="양심", description=" ", guild_ids=guild_ids)
async def 양심(ctx):
    embed=discord.Embed(description="양심", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/cQTkgD0/didtla.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="이글쓰", description=" ", guild_ids=guild_ids)
async def 이글쓰(ctx):
    embed=discord.Embed(description="이글쓰", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/mDnLbht/dlrmfTm.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="이파쓰", description=" ", guild_ids=guild_ids)
async def 이파쓰(ctx):
    embed=discord.Embed(description="이파쓰", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/6J1PQKP/dlvkTm.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="라이젠", description=" ", guild_ids=guild_ids)
async def 라이젠(ctx):
    embed=discord.Embed(description="라이젠", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/mzF9KZm/fkdlwps.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="IT", description=" ", guild_ids=guild_ids)
async def IT(ctx):
    embed=discord.Embed(description="IT", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/wd98YM0/IT.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="대부분버그", description=" ", guild_ids=guild_ids)
async def 대부분버그(ctx):
    embed=discord.Embed(description="대부분버그", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/Fq46YmD/eoqnqnsqjrm.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="계산중", description=" ", guild_ids=guild_ids)
async def 계산중(ctx):
    embed=discord.Embed(description="계산중", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/NK7fTYK/rPtkswnd.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="짜잔", description=" ", guild_ids=guild_ids)
async def 짜잔(ctx):
    embed=discord.Embed(description="짜잔", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/3pkXM2D/Wkwks.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="그런겜", description=" ", guild_ids=guild_ids)
async def 그런겜(ctx):
    embed=discord.Embed(description="그런겜", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/JmXyHtD/rmfjsrpa.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="이륙", description=" ", guild_ids=guild_ids)
async def 이륙(ctx):
    embed=discord.Embed(description="이륙", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/s9B1Ghq/dlfbr.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="존버또존버", description=" ", guild_ids=guild_ids)
async def 존버또존버(ctx):
    embed=discord.Embed(description="존버또존버", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/mGG923D/whsqj-Ehwhsqj.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="의외로정상", description=" ", guild_ids=guild_ids)
async def 의외로정상(ctx):
    embed=discord.Embed(description="의외로정상", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/x5j3dtG/dmldhlfhwjdtkd.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="정상", description=" ", guild_ids=guild_ids)
async def 정상(ctx):
    embed=discord.Embed(description="정상", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/DDzJtfC/wjdtkd.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="꼭사라", description=" ", guild_ids=guild_ids)
async def 꼭사라(ctx):
    embed=discord.Embed(description="꼭사라", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/J5D6L5Q/Rhrtkfk.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="환불", description=" ", guild_ids=guild_ids)
async def 환불(ctx):
    embed=discord.Embed(description="환불", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/syF5YHy/ghksqnf.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="따봉", description=" ", guild_ids=guild_ids)
async def 따봉(ctx):
    embed=discord.Embed(description="따봉", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/qsxZxfT/Ekqhd.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="편안", description=" ", guild_ids=guild_ids)
async def 편안(ctx):
    embed=discord.Embed(description="편안", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/v3Q021S/vusdks.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="어케했", description=" ", guild_ids=guild_ids)
async def 어케했(ctx):
    embed=discord.Embed(description="어케했", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/j6xRBp3/djzpgoT.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="의도된", description=" ", guild_ids=guild_ids)
async def 의도된(ctx):
    embed=discord.Embed(description="의도된", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/yRdYyFv/dmlehehls.gif")
    await ctx.send(embed=embed)

@slash.slash(name="꼬우면", description=" ", guild_ids=guild_ids)
async def 꼬우면(ctx):
    embed=discord.Embed(description="꼬우면", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/0qPmbfz/Rhdnaus.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="식은땀", description=" ", guild_ids=guild_ids)
async def 식은땀(ctx):
    embed=discord.Embed(description="식은땀", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/VNDTBn7/tlrdms-Eka.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="맞을래요", description=" ", guild_ids=guild_ids)
async def 맞을래요(ctx):
    embed=discord.Embed(description="맞을래요", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/WKwCCsZ/akwdmffo.png")
    await ctx.send(embed=embed)

@slash.slash(name="칠레감탄", description=" ", guild_ids=guild_ids)
async def 칠레감탄(ctx):
    embed=discord.Embed(description="칠레감탄", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/hYYJxxv/clffprkaxks.gif")
    await ctx.send(embed=embed)

@slash.slash(name="대기", description=" ", guild_ids=guild_ids)
async def 대기(ctx):
    embed=discord.Embed(description="대기", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/9rQgvzY/eorl.gif")
    await ctx.send(embed=embed)

@slash.slash(name="광클", description=" ", guild_ids=guild_ids)
async def 광클(ctx):
    embed=discord.Embed(description="광클", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/d7yJyfb/rhkdzmf.gif")
    await ctx.send(embed=embed)

@slash.slash(name="펀쿨끄덕", description=" ", guild_ids=guild_ids)
async def 펀쿨끄덕(ctx):
    embed=discord.Embed(description="펀쿨끄덕", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/9WymfxM/vjsznf-Rmejr.gif")
    await ctx.send(embed=embed)
@slash.slash(name="불편", description=" ", guild_ids=guild_ids)
async def 불편(ctx):
    embed=discord.Embed(description="불편", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/yNhtH1q/qnfvus.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="블루스크린", description=" ", guild_ids=guild_ids)
async def 블루스크린(ctx):
    embed=discord.Embed(description="블루스크린", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/rQgFMp9/qmffntmzmfls.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="애쉬", description=" ", guild_ids=guild_ids)
async def 애쉬(ctx):
    embed=discord.Embed(description="애쉬", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/ncrYnK4/dotnl.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="엘라샷건", description=" ", guild_ids=guild_ids)
async def 엘라샷건(ctx):
    embed=discord.Embed(description="엘라샷건", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/QmjbNMx/dpffktitrjs.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="인성문제", description=" ", guild_ids=guild_ids)
async def 인성문제(ctx):
    embed=discord.Embed(description="인성문제", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/BGmcp9n/dlstjdanswp.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="재부팅", description=" ", guild_ids=guild_ids)
async def 재부팅(ctx):
    embed=discord.Embed(description="재부팅", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/S5BqW5F/woqnxld.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="질병", description=" ", guild_ids=guild_ids)
async def 질병(ctx):
    embed=discord.Embed(description="질병", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/NKpvW95/wlfqud.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="1테라", description=" ", guild_ids=guild_ids)
async def 테라(ctx):
    embed=discord.Embed(description="1테라", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/HppH3St/1xpfk.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="갓겜", description=" ", guild_ids=guild_ids)
async def 갓겜(ctx):
    embed=discord.Embed(description="갓겜", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/17yw7qP/rktrpa.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="구글링", description=" ", guild_ids=guild_ids)
async def 구글링(ctx):
    embed=discord.Embed(description="구글링", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/3mv0Nc2/rnrmffld.png")
    await ctx.send(embed=embed)

@slash.slash(name="이과", description=" ", guild_ids=guild_ids)
async def 이과(ctx):
    embed=discord.Embed(description="이과", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/1T04P8F/Rhdnausdlrhk.png")
    await ctx.send(embed=embed)

@slash.slash(name="행복회로", description=" ", guild_ids=guild_ids)
async def 행복회로(ctx):
    embed=discord.Embed(description="행복회로", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/645zgvT/godqhrghlfh.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="과금전략", description=" ", guild_ids=guild_ids)
async def 과금전략(ctx):
    embed=discord.Embed(description="과금전략", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/WcVQfTq/rhkrmawjsfir.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="시간낭비", description=" ", guild_ids=guild_ids)
async def 시간낭비(ctx):
    embed=discord.Embed(description="시간낭비", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/sjJk02y/tlrksskdql.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="말잇못", description=" ", guild_ids=guild_ids)
async def 말잇못(ctx):
    embed=discord.Embed(description="말잇못", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/3dK37QD/akfdltaht.png")
    await ctx.send(embed=embed)

@slash.slash(name="이게왜안돼", description=" ", guild_ids=guild_ids)
async def 이게왜안돼(ctx):
    embed=discord.Embed(description="이게왜안돼", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/Qd4t38b/dlrpdhodkseho.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="이게왜돼", description=" ", guild_ids=guild_ids)
async def 이게왜돼(ctx):
    embed=discord.Embed(description="이게왜돼", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/cY93zvv/dlrpdhoeho.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="답없음", description=" ", guild_ids=guild_ids)
async def 답없음(ctx):
    embed=discord.Embed(description="답없음", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/Byt2jMQ/ekqdjqtdma.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="진짜최종", description=" ", guild_ids=guild_ids)
async def 진짜최종(ctx):
    embed=discord.Embed(description="진짜최종", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/rGfhGgH/wls-Wkchlwhd.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="맞다저장", description=" ", guild_ids=guild_ids)
async def 맞다저장(ctx):
    embed=discord.Embed(description="맞다저장", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/JrqY6bB/akwekwjwkd.png")
    await ctx.send(embed=embed)

@slash.slash(name="업데이트", description=" ", guild_ids=guild_ids)
async def 업데이트(ctx):
    embed=discord.Embed(description="업데이트", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/X33gMTY/djqepdlxm.png")
    await ctx.send(embed=embed)

@slash.slash(name="포맷", description=" ", guild_ids=guild_ids)
async def 포맷(ctx):
    embed=discord.Embed(description="포맷", color=0x4ac8c7)
    embed.set_image(url="https://i.ibb.co/tbgHz23/akqjqdmlaudfuddj.png")
    await ctx.send(embed=embed)

client.run(os.environ['token'])