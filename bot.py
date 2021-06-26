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

client = Bot(command_prefix = "prefix", intents=discord.Intents.all(), activity = discord.Game(name="새로운기능 코딩"))
slash = SlashCommand(client, sync_commands=True, sync_on_cog_reload=True, override_type=True)

@client.event
async def on_ready():
    print("준비된!")

guild_ids = [int(os.environ['guild_id'])]
embed_color = 0x4ac8c7

if __name__ == '__main__':
    for cog in os.listdir("./cogs"):
        if cog.endswith(".py"):
            try:
                cog = f"cogs.{cog.replace('.py', '')}"
                client.load_extension(cog)
                client.get_command(cog)
            except Exception as e:
                print(f"🔴 | {cog}")
                raise e
            else:
                print("🟢 | {}".format(cog))

@slash.slash(name="명령어", 
            description="🚧 명령어 ON/OFF",
            guild_ids=guild_ids,
            options=[
                create_option(
                    name="작업",
                    description="무슨 작업을 할까요?",
                    option_type=3,
                    required=True,
                    choices=[
                        create_choice(
                            name="켜기",
                            value="load"
                        ),
                        create_choice(
                            name="끄기",
                            value="unload"
                        ),
                        create_choice(
                            name="리로드",
                            value="reload"
                        )
                    ]
                ),
                create_option(
                    name="명령어",
                    description="무슨 명령어를 작업할까요?",
                    option_type=3,
                    required=True,
                    choices=[
                        create_choice(
                            name="ping",
                            value="ping"
                        ),
                        create_choice(
                            name="콘관리",
                            value="콘관리"
                        ),
                        create_choice(
                            name="우리핵",
                            value="우리핵"
                        )
                    ]
                )
            ]
)
async def cogs_m(ctx, 작업: str, 명령어: str):
    if 작업 == "load":
        try:
            client.load_extension(f'cogs.{명령어}')
            print(f'✅ | "{작업}: Cogs.{명령어}" | {ctx.author.name} 에 의해 정상적으로 활성화됨')
            timestamp = datetime.datetime.now(datetime.timezone.utc)
            url = ctx.author.avatar_url
            embed=discord.Embed(title=f"{작업}: Cogs.{명령어}", color=embed_color)
            embed.set_author(name=f"{ctx.author.name}", icon_url=url)
            embed.add_field(name="￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣", value="🟢 | 정상적으로 활성화했어요!", inline=False)
            embed.set_footer(text=timestamp.astimezone().strftime('%Y-%m-%d %H:%M:%S'))
            await ctx.send(hidden = True, embed=embed)
        except commands.ExtensionNotFound as e:
            print(f'🔴 | "{작업}: Cogs.{명령어}" | {ctx.author.name}: {e}')
            url = ctx.author.avatar_url
            embed=discord.Embed(title=f"⁉ {작업}: Cogs.{명령어}")
            embed.set_author(name=f"{ctx.author.name}", icon_url=url)
            embed.add_field(name="￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣", value="🔴 | 에러: 찾을 수 없습니다!", inline=False)
            await ctx.send(hidden = True, embed=embed)
        except commands.ExtensionAlreadyLoaded as e:
            print(f'🔴 | "{작업}: Cogs.{명령어}" | {ctx.author.name}: {e}')
            url = ctx.author.avatar_url
            embed=discord.Embed(title=f"⁉ {작업}: Cogs.{명령어}")
            embed.set_author(name=f"{ctx.author.name}", icon_url=url)
            embed.add_field(name="￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣", value="🔴 | 에러: 이미 로드되어있습니다!", inline=False)
            await ctx.send(hidden = True, embed=embed)
        except commands.NoEntryPointError as e:
            print(f'🔴 | "{작업}: Cogs.{명령어}" | {ctx.author.name}: {e}')
            url = ctx.author.avatar_url
            embed=discord.Embed(title=f"⁉ {작업}: Cogs.{명령어}")
            embed.set_author(name=f"{ctx.author.name}", icon_url=url)
            embed.add_field(name="￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣", value="🔴 | 에러: 파일에 setup point가 존재하지 않습니다!", inline=False)
            await ctx.send(hidden = True, embed=embed)
        except commands.ExtensionFailed as e:
            print(f'🔴 | "{작업}: Cogs.{명령어}" | {ctx.author.name}: {e}')
            url = ctx.author.avatar_url
            embed=discord.Embed(title=f"⁉ {작업}: Cogs.{명령어}")
            embed.set_author(name=f"{ctx.author.name}", icon_url=url)
            embed.add_field(name="￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣", value="🔴 | 에러: 불러오는데에 실패했습니다!", inline=False)
            await ctx.send(hidden = True, embed=embed)
            
            
    elif 작업 == "unload":
        try:
            client.unload_extension(f'cogs.{명령어}')
            print(f'❎ | "{작업}: Cogs.{명령어}" | {ctx.author.name} 에 의해 정상적으로 비활성화됨')
            timestamp = datetime.datetime.now(datetime.timezone.utc)
            url = ctx.author.avatar_url
            embed=discord.Embed(title=f"{작업}: Cogs.{명령어}", color=embed_color)
            embed.set_author(name=f"{ctx.author.name}", icon_url=url)
            embed.add_field(name="￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣", value="🟢 | 정상적으로 비활성화했어요!", inline=False)
            embed.set_footer(text=timestamp.astimezone().strftime('%Y-%m-%d %H:%M:%S'))
            await ctx.send(hidden = True, embed=embed)
            return
        except commands.ExtensionNotFound as e:
            print(f'🔴 | "{작업}: Cogs.{명령어}" | {ctx.author.name}: {e}')
            url = ctx.author.avatar_url
            embed=discord.Embed(title=f"⁉ {작업}: Cogs.{명령어}")
            embed.set_author(name=f"{ctx.author.name}", icon_url=url)
            embed.add_field(name="￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣", value="🔴 | 에러: 찾을 수 없습니다!", inline=False)
            await ctx.send(hidden = True, embed=embed)
        except commands.ExtensionNotLoaded as e:
            print(f'🔴 | "{작업}: Cogs.{명령어}" | {ctx.author.name}: {e}')
            url = ctx.author.avatar_url
            embed=discord.Embed(title=f"⁉ {작업}: Cogs.{명령어}")
            embed.set_author(name=f"{ctx.author.name}", icon_url=url)
            embed.add_field(name="￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣", value="🔴 | 에러: 이미 비활성화 되어있습니다!", inline=False)
            await ctx.send(hidden = True, embed=embed)
    elif 작업 == "reload":
        try:
            client.reload_extension(f'cogs.{명령어}')
            print(f'🔄 | "{작업}: Cogs.{명령어}" | {ctx.author.name} 에 의해 정상적으로 재시작됨')
            timestamp = datetime.datetime.now(datetime.timezone.utc)
            url = ctx.author.avatar_url
            embed=discord.Embed(title=f"{작업}: Cogs.{명령어}", color=embed_color)
            embed.set_author(name=f"{ctx.author.name}", icon_url=url)
            embed.add_field(name="￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣", value="🟢 | 정상적으로 재시작했어요!", inline=False)
            embed.set_footer(text=timestamp.astimezone().strftime('%Y-%m-%d %H:%M:%S'))
            await ctx.send(hidden = True, embed=embed)
        except commands.ExtensionNotLoaded as e:
            print(f'🔴 | "{작업}: Cogs.{명령어}" | {ctx.author.name}: {e}')
            url = ctx.author.avatar_url
            embed=discord.Embed(title=f"⁉ {작업}: Cogs.{명령어}")
            embed.set_author(name=f"{ctx.author.name}", icon_url=url)
            embed.add_field(name="￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣", value="🔴 | 에러: 로드되어있지 않습니다!", inline=False)
            await ctx.send(hidden = True, embed=embed)
        except commands.ExtensionNotFound as e:
            print(f'🔴 | "{작업}: Cogs.{명령어}" | {ctx.author.name}: {e}')
            url = ctx.author.avatar_url
            embed=discord.Embed(title=f"⁉ {작업}: Cogs.{명령어}")
            embed.set_author(name=f"{ctx.author.name}", icon_url=url)
            embed.add_field(name="￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣", value="🔴 | 에러: 찾을 수 없습니다!", inline=False)
            await ctx.send(hidden = True, embed=embed)
        except commands.NoEntryPointError as e:
            print(f'🔴 | "{작업}: Cogs.{명령어}" | {ctx.author.name}: {e}')
            url = ctx.author.avatar_url
            embed=discord.Embed(title=f"⁉ {작업}: Cogs.{명령어}")
            embed.set_author(name=f"{ctx.author.name}", icon_url=url)
            embed.add_field(name="￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣", value="🔴 | 에러: 파일에 setup point가 존재하지 않습니다!", inline=False)
            await ctx.send(hidden = True, embed=embed)
        except commands.ExtensionFailed as e:
            print(f'🔴 | "{작업}: Cogs.{명령어}" | {ctx.author.name}: {e}')
            url = ctx.author.avatar_url
            embed=discord.Embed(title=f"⁉ {작업}: Cogs.{명령어}")
            embed.set_author(name=f"{ctx.author.name}", icon_url=url)
            embed.add_field(name="￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣", value="🔴 | 에러: 불러오는데에 실패했습니다!", inline=False)
            await ctx.send(hidden = True, embed=embed)
        
@slash.slash(name="고티", description=" ", guild_ids=guild_ids)
async def 고티(ctx):
    embed=discord.Embed(description="고티", color=embed_color)
    embed.set_image(url="https://i.ibb.co/yVYpvGn/rhxl.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="님폰없", description=" ", guild_ids=guild_ids)
async def 님폰없(ctx):
    embed=discord.Embed(description="님폰없", color=embed_color)
    embed.set_image(url="https://i.ibb.co/BBZY0ZY/slavhsdjqt.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="능지", description=" ", guild_ids=guild_ids)
async def 능지(ctx):
    embed=discord.Embed(description="능지", color=embed_color)
    embed.set_image(url="https://i.ibb.co/zPhLbCK/smdwl.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="상담", description=" ", guild_ids=guild_ids)
async def 상담(ctx):
    embed=discord.Embed(description="상담", color=embed_color)
    embed.set_image(url="https://i.ibb.co/FhHh34G/tkdeka.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="사용자", description=" ", guild_ids=guild_ids)
async def 사용자(ctx):
    embed=discord.Embed(description="사용자", color=embed_color)
    embed.set_image(url="https://i.ibb.co/C0Ny77Q/tkdydwk.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="팟지", description=" ", guild_ids=guild_ids)
async def 팟지(ctx):
    embed=discord.Embed(description="팟지", color=embed_color)
    embed.set_image(url="https://i.ibb.co/3scVVPh/vktwl.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="라데온", description=" ", guild_ids=guild_ids)
async def 라데온(ctx):
    embed=discord.Embed(description="라데온", color=embed_color)
    embed.set_image(url="https://i.ibb.co/TgQS38s/fkepdhs.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="양심", description=" ", guild_ids=guild_ids)
async def 양심(ctx):
    embed=discord.Embed(description="양심", color=embed_color)
    embed.set_image(url="https://i.ibb.co/cQTkgD0/didtla.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="이글쓰", description=" ", guild_ids=guild_ids)
async def 이글쓰(ctx):
    embed=discord.Embed(description="이글쓰", color=embed_color)
    embed.set_image(url="https://i.ibb.co/mDnLbht/dlrmfTm.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="이파쓰", description=" ", guild_ids=guild_ids)
async def 이파쓰(ctx):
    embed=discord.Embed(description="이파쓰", color=embed_color)
    embed.set_image(url="https://i.ibb.co/6J1PQKP/dlvkTm.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="라이젠", description=" ", guild_ids=guild_ids)
async def 라이젠(ctx):
    embed=discord.Embed(description="라이젠", color=embed_color)
    embed.set_image(url="https://i.ibb.co/mzF9KZm/fkdlwps.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="IT", description=" ", guild_ids=guild_ids)
async def IT(ctx):
    embed=discord.Embed(description="IT", color=embed_color)
    embed.set_image(url="https://i.ibb.co/wd98YM0/IT.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="대부분버그", description=" ", guild_ids=guild_ids)
async def 대부분버그(ctx):
    embed=discord.Embed(description="대부분버그", color=embed_color)
    embed.set_image(url="https://i.ibb.co/Fq46YmD/eoqnqnsqjrm.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="계산중", description=" ", guild_ids=guild_ids)
async def 계산중(ctx):
    embed=discord.Embed(description="계산중", color=embed_color)
    embed.set_image(url="https://i.ibb.co/NK7fTYK/rPtkswnd.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="짜잔", description=" ", guild_ids=guild_ids)
async def 짜잔(ctx):
    embed=discord.Embed(description="짜잔", color=embed_color)
    embed.set_image(url="https://i.ibb.co/3pkXM2D/Wkwks.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="그런겜", description=" ", guild_ids=guild_ids)
async def 그런겜(ctx):
    embed=discord.Embed(description="그런겜", color=embed_color)
    embed.set_image(url="https://i.ibb.co/JmXyHtD/rmfjsrpa.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="이륙", description=" ", guild_ids=guild_ids)
async def 이륙(ctx):
    embed=discord.Embed(description="이륙", color=embed_color)
    embed.set_image(url="https://i.ibb.co/s9B1Ghq/dlfbr.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="존버또존버", description=" ", guild_ids=guild_ids)
async def 존버또존버(ctx):
    embed=discord.Embed(description="존버또존버", color=embed_color)
    embed.set_image(url="https://i.ibb.co/mGG923D/whsqj-Ehwhsqj.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="의외로정상", description=" ", guild_ids=guild_ids)
async def 의외로정상(ctx):
    embed=discord.Embed(description="의외로정상", color=embed_color)
    embed.set_image(url="https://i.ibb.co/x5j3dtG/dmldhlfhwjdtkd.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="정상", description=" ", guild_ids=guild_ids)
async def 정상(ctx):
    embed=discord.Embed(description="정상", color=embed_color)
    embed.set_image(url="https://i.ibb.co/DDzJtfC/wjdtkd.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="꼭사라", description=" ", guild_ids=guild_ids)
async def 꼭사라(ctx):
    embed=discord.Embed(description="꼭사라", color=embed_color)
    embed.set_image(url="https://i.ibb.co/J5D6L5Q/Rhrtkfk.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="환불", description=" ", guild_ids=guild_ids)
async def 환불(ctx):
    embed=discord.Embed(description="환불", color=embed_color)
    embed.set_image(url="https://i.ibb.co/syF5YHy/ghksqnf.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="따봉", description=" ", guild_ids=guild_ids)
async def 따봉(ctx):
    embed=discord.Embed(description="따봉", color=embed_color)
    embed.set_image(url="https://i.ibb.co/qsxZxfT/Ekqhd.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="편안", description=" ", guild_ids=guild_ids)
async def 편안(ctx):
    embed=discord.Embed(description="편안", color=embed_color)
    embed.set_image(url="https://i.ibb.co/v3Q021S/vusdks.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="어케했", description=" ", guild_ids=guild_ids)
async def 어케했(ctx):
    embed=discord.Embed(description="어케했", color=embed_color)
    embed.set_image(url="https://i.ibb.co/j6xRBp3/djzpgoT.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="의도된", description=" ", guild_ids=guild_ids)
async def 의도된(ctx):
    embed=discord.Embed(description="의도된", color=embed_color)
    embed.set_image(url="https://i.ibb.co/yRdYyFv/dmlehehls.gif")
    await ctx.send(embed=embed)

@slash.slash(name="꼬우면", description=" ", guild_ids=guild_ids)
async def 꼬우면(ctx):
    embed=discord.Embed(description="꼬우면", color=embed_color)
    embed.set_image(url="https://i.ibb.co/0qPmbfz/Rhdnaus.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="식은땀", description=" ", guild_ids=guild_ids)
async def 식은땀(ctx):
    embed=discord.Embed(description="식은땀", color=embed_color)
    embed.set_image(url="https://i.ibb.co/VNDTBn7/tlrdms-Eka.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="맞을래요", description=" ", guild_ids=guild_ids)
async def 맞을래요(ctx):
    embed=discord.Embed(description="맞을래요", color=embed_color)
    embed.set_image(url="https://i.ibb.co/WKwCCsZ/akwdmffo.png")
    await ctx.send(embed=embed)

@slash.slash(name="칠레감탄", description=" ", guild_ids=guild_ids)
async def 칠레감탄(ctx):
    embed=discord.Embed(description="칠레감탄", color=embed_color)
    embed.set_image(url="https://i.ibb.co/hYYJxxv/clffprkaxks.gif")
    await ctx.send(embed=embed)

@slash.slash(name="대기", description=" ", guild_ids=guild_ids)
async def 대기(ctx):
    embed=discord.Embed(description="대기", color=embed_color)
    embed.set_image(url="https://i.ibb.co/9rQgvzY/eorl.gif")
    await ctx.send(embed=embed)

@slash.slash(name="광클", description=" ", guild_ids=guild_ids)
async def 광클(ctx):
    embed=discord.Embed(description="광클", color=embed_color)
    embed.set_image(url="https://i.ibb.co/d7yJyfb/rhkdzmf.gif")
    await ctx.send(embed=embed)

@slash.slash(name="펀쿨끄덕", description=" ", guild_ids=guild_ids)
async def 펀쿨끄덕(ctx):
    embed=discord.Embed(description="펀쿨끄덕", color=embed_color)
    embed.set_image(url="https://i.ibb.co/9WymfxM/vjsznf-Rmejr.gif")
    await ctx.send(embed=embed)
@slash.slash(name="불편", description=" ", guild_ids=guild_ids)
async def 불편(ctx):
    embed=discord.Embed(description="불편", color=embed_color)
    embed.set_image(url="https://i.ibb.co/yNhtH1q/qnfvus.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="블루스크린", description=" ", guild_ids=guild_ids)
async def 블루스크린(ctx):
    embed=discord.Embed(description="블루스크린", color=embed_color)
    embed.set_image(url="https://i.ibb.co/rQgFMp9/qmffntmzmfls.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="애쉬", description=" ", guild_ids=guild_ids)
async def 애쉬(ctx):
    embed=discord.Embed(description="애쉬", color=embed_color)
    embed.set_image(url="https://i.ibb.co/ncrYnK4/dotnl.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="엘라샷건", description=" ", guild_ids=guild_ids)
async def 엘라샷건(ctx):
    embed=discord.Embed(description="엘라샷건", color=embed_color)
    embed.set_image(url="https://i.ibb.co/QmjbNMx/dpffktitrjs.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="인성문제", description=" ", guild_ids=guild_ids)
async def 인성문제(ctx):
    embed=discord.Embed(description="인성문제", color=embed_color)
    embed.set_image(url="https://i.ibb.co/BGmcp9n/dlstjdanswp.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="재부팅", description=" ", guild_ids=guild_ids)
async def 재부팅(ctx):
    embed=discord.Embed(description="재부팅", color=embed_color)
    embed.set_image(url="https://i.ibb.co/S5BqW5F/woqnxld.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="질병", description=" ", guild_ids=guild_ids)
async def 질병(ctx):
    embed=discord.Embed(description="질병", color=embed_color)
    embed.set_image(url="https://i.ibb.co/NKpvW95/wlfqud.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="1테라", description=" ", guild_ids=guild_ids)
async def 테라(ctx):
    embed=discord.Embed(description="1테라", color=embed_color)
    embed.set_image(url="https://i.ibb.co/HppH3St/1xpfk.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="갓겜", description=" ", guild_ids=guild_ids)
async def 갓겜(ctx):
    embed=discord.Embed(description="갓겜", color=embed_color)
    embed.set_image(url="https://i.ibb.co/17yw7qP/rktrpa.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="구글링", description=" ", guild_ids=guild_ids)
async def 구글링(ctx):
    embed=discord.Embed(description="구글링", color=embed_color)
    embed.set_image(url="https://i.ibb.co/3mv0Nc2/rnrmffld.png")
    await ctx.send(embed=embed)

@slash.slash(name="이과", description=" ", guild_ids=guild_ids)
async def 이과(ctx):
    embed=discord.Embed(description="이과", color=embed_color)
    embed.set_image(url="https://i.ibb.co/1T04P8F/Rhdnausdlrhk.png")
    await ctx.send(embed=embed)

@slash.slash(name="행복회로", description=" ", guild_ids=guild_ids)
async def 행복회로(ctx):
    embed=discord.Embed(description="행복회로", color=embed_color)
    embed.set_image(url="https://i.ibb.co/645zgvT/godqhrghlfh.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="과금전략", description=" ", guild_ids=guild_ids)
async def 과금전략(ctx):
    embed=discord.Embed(description="과금전략", color=embed_color)
    embed.set_image(url="https://i.ibb.co/WcVQfTq/rhkrmawjsfir.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="시간낭비", description=" ", guild_ids=guild_ids)
async def 시간낭비(ctx):
    embed=discord.Embed(description="시간낭비", color=embed_color)
    embed.set_image(url="https://i.ibb.co/sjJk02y/tlrksskdql.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="말잇못", description=" ", guild_ids=guild_ids)
async def 말잇못(ctx):
    embed=discord.Embed(description="말잇못", color=embed_color)
    embed.set_image(url="https://i.ibb.co/3dK37QD/akfdltaht.png")
    await ctx.send(embed=embed)

@slash.slash(name="이게왜안돼", description=" ", guild_ids=guild_ids)
async def 이게왜안돼(ctx):
    embed=discord.Embed(description="이게왜안돼", color=embed_color)
    embed.set_image(url="https://i.ibb.co/Qd4t38b/dlrpdhodkseho.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="이게왜돼", description=" ", guild_ids=guild_ids)
async def 이게왜돼(ctx):
    embed=discord.Embed(description="이게왜돼", color=embed_color)
    embed.set_image(url="https://i.ibb.co/cY93zvv/dlrpdhoeho.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="답없음", description=" ", guild_ids=guild_ids)
async def 답없음(ctx):
    embed=discord.Embed(description="답없음", color=embed_color)
    embed.set_image(url="https://i.ibb.co/Byt2jMQ/ekqdjqtdma.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="진짜최종", description=" ", guild_ids=guild_ids)
async def 진짜최종(ctx):
    embed=discord.Embed(description="진짜최종", color=embed_color)
    embed.set_image(url="https://i.ibb.co/rGfhGgH/wls-Wkchlwhd.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="맞다저장", description=" ", guild_ids=guild_ids)
async def 맞다저장(ctx):
    embed=discord.Embed(description="맞다저장", color=embed_color)
    embed.set_image(url="https://i.ibb.co/JrqY6bB/akwekwjwkd.png")
    await ctx.send(embed=embed)

@slash.slash(name="업데이트", description=" ", guild_ids=guild_ids)
async def 업데이트(ctx):
    embed=discord.Embed(description="업데이트", color=embed_color)
    embed.set_image(url="https://i.ibb.co/X33gMTY/djqepdlxm.png")
    await ctx.send(embed=embed)

@slash.slash(name="포맷", description=" ", guild_ids=guild_ids)
async def 포맷(ctx):
    embed=discord.Embed(description="포맷", color=embed_color)
    embed.set_image(url="https://i.ibb.co/tbgHz23/akqjqdmlaudfuddj.png")
    await ctx.send(embed=embed)

client.run(os.environ['token'])