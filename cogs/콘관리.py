from discord_slash.utils.manage_commands import create_option, create_choice
import discord
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash import cog_ext, SlashContext
from discord import DMChannel
import re
import asyncio
import os

guild_ids = [int(os.environ['guild_id'])]

client = discord.Client(intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True)

confirm_emoji = '\N{Heavy Large Circle}'
deny_emoji = '\N{Cross Mark}'
skip_emoji = '\N{Black Right-Pointing Double Triangle with Vertical Bar}'

class conmanage(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(name="콘", 
                description="원하는 이미지를 콘으로 만들어보세요!",
                options=[
                    create_option(
                        name="작업",
                        description="무슨 작업을 진행할까요?",
                        option_type=3,
                        required=True,
                        choices=[
                            create_choice(
                                name="생성",
                                value="Create"
                            ),
                            create_choice(
                                name="수정",
                                value="Edit"
                            ),
                            create_choice(
                                name="삭제",
                                value="Delete"
                            ),
                            create_choice(
                                name="목록",
                                value="List"
                            )
                        ]
                    )
                ])
    async def con(self, ctx, 작업: str, pass_context=True):
        if 작업 == "Create":
            embed=discord.Embed(title="최종 기능 추가 안내")
            embed.add_field(name="1. 명령어를 어떻게 추가하느냐", value="Discord Cogs Extension을 사용하면 명령어들을 확장프로그램처럼 껐다 켰다 할 수 있는데, 이게 Slash 명령어에도 적용이 되고, 자동완성 등록이 되는지가 문제. 테스트해 봤는데 어떻게 하는지 도저히 모르겠음", inline=False)
            embed.add_field(name="2. 봇 호스팅 관련 문제", value="디스코드 봇을 로컬에서 직접 돌리는 게 아니라 무료 호스팅 사이트를 이용하다 보니, 수정한 소스코드를 깃허브에 커밋하면, Heroku에서 빌드하고 시작하는 방식임. 가끔 Heroku에서 빌드제한을 걸어서 빌드가 제대로 작동되지 않는 경우가 있음. ", inline=False)
            embed.add_field(name="3. 이미지 호스팅 문제", value="Imgbb에서 제공하는 API가 유료라서 사용하기 좀 그럼, 디스코드 자체 이미지 링크를 따오고 있지만 불안정함", inline=False)
            embed.add_field(name="그래서 결론은?", value="콘 추가는 그냥 기존의 방식을 따르는 것으로로 일단 결정함, 일단 반자동화에 신경 쓰면 될 듯", inline=False)
            await ctx.send(hidden = True, embed=embed)
            embed=discord.Embed(title="콘 생성 [ 1/7 ]", description="￣￣￣￣￣￣￣￣￣￣￣￣￣￣", color=0x4ac8c7)
            embed.add_field(name=f"상위 태그 분류에 등록할까요?", value="예) /냥: 냥슬픔, 냥경악 ", inline=True)
            embed.set_footer(text="등록시 ⭕, 미등록시 ⏭️, 취소시 ❌")
            tagmsg = await ctx.send(embed=embed)
            await tagmsg.add_reaction(confirm_emoji)
            await tagmsg.add_reaction(skip_emoji)
            await tagmsg.add_reaction(deny_emoji)
            @client.event
            async def on_reaction_add(reaction, user):
                if user.bot == 1:
                    return None

                if str(reaction.emoji) == deny_emoji: # 등록 취소
                    await tagmsg.delete()
                    await ctx.send(hidden = True, content="콘 생성이 취소되었습니다.")
                    return

                if str(reaction.emoji) == confirm_emoji: #태그 등록
                    await tagmsg.delete()
                    embed=discord.Embed(title="콘 생성 [ 1/7 ]", description="￣￣￣￣￣￣￣￣￣￣￣￣￣￣", color=0x4ac8c7)
                    embed.add_field(name="1. 분류 태그를 보내주세요.", value="↳ 채팅으로 보내기", inline=True)
                    embed.set_footer(text="취소시 ❌")
                    msg = await ctx.send(embed=embed)
                    await msg.add_reaction(deny_emoji)
                    @client.event
                    async def on_reaction_add(reaction, user):
                        if user.bot == 1:
                            return None
                        if str(reaction.emoji) == deny_emoji:
                            await msg.delete()
                            await ctx.send(hidden = True, content="콘 생성이 취소되었습니다.")
                            return
                    contag = await client.wait_for("message")
                    await msg.delete()
                    embed=discord.Embed(title="콘 생성 [ 2/7 ]", description="￣￣￣￣￣￣￣￣￣￣￣￣￣￣", color=0x4ac8c7)
                    embed.add_field(name="1. 생성할 콘 이름을 보내주세요.", value="↳ 채팅으로 보내기", inline=True)
                    embed.set_footer(text="취소시 ❌")
                    msg = await ctx.send(embed=embed) # 콘 이름 보내라는 임베드 메세지 전송
                    await msg.add_reaction(deny_emoji) # 취소시 ❌ 이모티콘 리액션 달기
                    @client.event
                    async def on_reaction_add(reaction, user):
                        if user.bot == 1:
                            return None
                        if str(reaction.emoji) == deny_emoji: # 취소시 ❌ 이모티콘이 추가되면 
                            await msg.delete()
                            await ctx.send(hidden = True, content="콘 생성이 취소되었습니다.")
                            return
                    conname = await client.wait_for("message")
                    await msg.delete()
                    embed=discord.Embed(title="콘 생성 [ 3/7 ]", description="￣￣￣￣￣￣￣￣￣￣￣￣￣￣", color=0x4ac8c7)
                    embed.add_field(name=f"{contag.content}{conname.content}", value=" 로 등록할까요?", inline=True)
                    embed.set_footer(text="결정시 ⭕, 취소시 ❌")
                    name_confirm = await ctx.send(embed=embed)
                    await name_confirm.add_reaction(confirm_emoji)
                    await name_confirm.add_reaction(deny_emoji)
                    @client.event
                    async def on_reaction_add(reaction, user):
                        if user.bot == 1:
                            return None
                        if str(reaction.emoji) == deny_emoji:
                            await name_confirm.delete()
                            await ctx.send(hidden = True, content="콘 생성이 취소되었습니다.")
                            return None
                        if str(reaction.emoji) == confirm_emoji:
                            await name_confirm.delete()
                            embed=discord.Embed(title="콘 생성 [ 4/7 ]", description="￣￣￣￣￣￣￣￣￣￣￣￣￣￣", color=0x4ac8c7)
                            embed.add_field(name=f"1. 생성될 콘 이름: ", value=f"{contag.content}{conname.content}", inline=False)
                            embed.add_field(name="2. 생성할 콘 이미지를 보내주세요.", value="↳ 채팅으로 이미지 보내기", inline=False)
                            embed.set_footer(text="취소시 ❌, 100x100을 추천합니다.")
                            msg = await ctx.send(embed=embed)
                            await msg.add_reaction(deny_emoji)
                            @client.event
                            async def on_reaction_add(reaction, user):
                                if user.bot == 1:
                                    return None
                                if str(reaction.emoji) == deny_emoji:
                                    await msg.delete()
                                    await ctx.send(hidden = True, content="콘 생성이 취소되었습니다.")
                                    return None
                            conurl = await client.wait_for("message")
                            await msg.delete()
                            image = conurl.attachments[0]
                            embed.set_image(url=conurl)
                            embed=discord.Embed(title="콘 생성 [ 5/7 ]", description="￣￣￣￣￣￣￣￣￣￣￣￣￣￣", color=0x4ac8c7)
                            embed.add_field(name=f"이 이미지로 등록할까요?", value="100x100을 추천합니다.", inline=True)
                            embed.set_footer(text="결정시 ⭕, 취소시 ❌")
                            embed.set_image(url=image)
                            msg = await ctx.send(embed=embed)
                            await msg.add_reaction(confirm_emoji)
                            await msg.add_reaction(deny_emoji)
                            @client.event
                            async def on_reaction_add(reaction, user):
                                if user.bot == 1:
                                    return None
                                if str(reaction.emoji) == deny_emoji:
                                    await msg.delete()
                                    await ctx.send(hidden = True, content="콘 생성이 취소되었습니다.")
                                    return
                                if str(reaction.emoji) == confirm_emoji:
                                    await msg.delete()
                                    embed=discord.Embed(title="최종 미리보기", description=f"{contag.content}{conname.content}", color=0x4ac8c7)
                                    embed.set_footer(text="결정시 ⭕, 취소시 ❌")
                                    embed.set_image(url=image)
                                    preview = await ctx.send(embed=embed)
                                    await preview.add_reaction(confirm_emoji)
                                    await preview.add_reaction(deny_emoji)
                                    @client.event
                                    async def on_reaction_add(reaction, user):
                                        if user.bot == 1:
                                            return None
                                        if str(reaction.emoji) == deny_emoji:
                                            await preview.delete()
                                            await ctx.send(hidden = True, content="콘 생성이 취소되었습니다.")
                                            return
                                        if str(reaction.emoji) == confirm_emoji:
                                            await preview.delete()
                                            embed=discord.Embed(title="최종 기능 추가 안내")
                                            embed.add_field(name="1. 명령어를 어떻게 추가하느냐", value="Discord Cogs Extension을 사용하면 명령어들을 확장프로그램처럼 껐다 켰다 할 수 있는데, 이게 Slash 명령어에도 적용이 되고, 자동완성 등록이 되는지가 문제. 테스트해 봤는데 어떻게 하는지 도저히 모르겠음", inline=False)
                                            embed.add_field(name="2. 봇 호스팅 관련 문제", value="디스코드 봇을 로컬에서 직접 돌리는 게 아니라 무료 호스팅 사이트를 이용하다 보니, 수정한 소스코드를 깃허브에 커밋하면, Heroku에서 빌드하고 시작하는 방식임. 가끔 Heroku에서 빌드제한을 걸어서 빌드가 제대로 작동되지 않는 경우가 있음. ", inline=False)
                                            embed.add_field(name="3. 이미지 호스팅 문제", value="Imgbb에서 제공하는 API가 유료라서 사용하기 좀 그럼, 디스코드 자체 이미지 링크를 따오고 있지만 불안정함", inline=False)
                                            embed.add_field(name="그래서 결론은?", value="콘 추가는 그냥 기존의 방식을 따르는 것으로로 일단 결정함, 일단 반자동화에 신경 쓰면 될 듯", inline=False)
                                            await ctx.send(hidden = True, embed=embed)
                                            return


                

                if str(reaction.emoji) == skip_emoji: # 태그 미등록
                    await tagmsg.delete()
                    embed=discord.Embed(title="콘 생성 [ 2/7 ]", description="￣￣￣￣￣￣￣￣￣￣￣￣￣￣", color=0x4ac8c7)
                    embed.add_field(name="1. 생성할 콘 이름을 보내주세요.", value="↳ 채팅으로 보내기", inline=True)
                    embed.set_footer(text="취소시 ❌")
                    msg = await ctx.send(embed=embed)
                    await msg.add_reaction(deny_emoji)
                    @client.event
                    async def on_reaction_add(reaction, user):
                        if user.bot == 1:
                            return None
                        if str(reaction.emoji) == deny_emoji:
                            await msg.delete()
                            await ctx.send(hidden = True, content="콘 생성이 취소되었습니다.")
                            return
                    conname = await client.wait_for("message")
                    await msg.delete()
                    embed=discord.Embed(title="콘 생성 [ 3/7 ]", description="￣￣￣￣￣￣￣￣￣￣￣￣￣￣", color=0x4ac8c7)
                    embed.add_field(name=f"{conname.content}", value=" 로 등록할까요?", inline=True)
                    embed.set_footer(text="결정시 ⭕, 취소시 ❌")
                    name_confirm = await ctx.send(embed=embed)
                    await name_confirm.add_reaction(confirm_emoji)
                    await name_confirm.add_reaction(deny_emoji)
                
                    @client.event
                    async def on_reaction_add(reaction, user):
                        if user.bot == 1:
                            return None
                        if str(reaction.emoji) == deny_emoji:
                            await name_confirm.delete()
                            await ctx.send(hidden = True, content="콘 생성이 취소되었습니다.")
                            return None
                        if str(reaction.emoji) == confirm_emoji:
                            await name_confirm.delete()
                            embed=discord.Embed(title="콘 생성 [ 4/7 ]", description="￣￣￣￣￣￣￣￣￣￣￣￣￣￣", color=0x4ac8c7)
                            embed.add_field(name=f"1. 생성될 콘 이름: ", value=f"{conname.content}", inline=False)
                            embed.add_field(name="2. 생성할 콘 이미지를 보내주세요.", value="↳ 채팅으로 이미지 보내기", inline=False)
                            embed.set_footer(text="취소시 ❌, 100x100을 추천합니다.")
                            msg = await ctx.send(embed=embed)
                            await msg.add_reaction(deny_emoji)
                            @client.event
                            async def on_reaction_add(reaction, user):
                                if user.bot == 1:
                                    return None
                                if str(reaction.emoji) == deny_emoji:
                                    await msg.delete()
                                    await ctx.send(hidden = True, content="콘 생성이 취소되었습니다.")
                                    return None
                            conurl = await client.wait_for("message")
                            await msg.delete()
                            image = conurl.attachments[0]
                            embed.set_image(url=conurl)
                            embed=discord.Embed(title="콘 생성 [ 5/7 ]", description="￣￣￣￣￣￣￣￣￣￣￣￣￣￣", color=0x4ac8c7)
                            embed.add_field(name=f"이 이미지로 등록할까요?", value="100x100을 추천합니다.", inline=True)
                            embed.set_footer(text="결정시 ⭕, 취소시 ❌")
                            embed.set_image(url=image)
                            msg = await ctx.send(embed=embed)
                            await msg.add_reaction(confirm_emoji)
                            await msg.add_reaction(deny_emoji)
                            @client.event
                            async def on_reaction_add(reaction, user):
                                if user.bot == 1:
                                    return None
                                if str(reaction.emoji) == deny_emoji:
                                    await msg.delete()
                                    await ctx.send(hidden = True, content="콘 생성이 취소되었습니다.")
                                    return
                                if str(reaction.emoji) == confirm_emoji:
                                    await msg.delete()
                                    embed=discord.Embed(title="최종 미리보기", description=f"{conname.content}", color=0x4ac8c7)
                                    embed.set_footer(text="결정시 ⭕, 취소시 ❌")
                                    embed.set_image(url=image)
                                    preview = await ctx.send(embed=embed)
                                    await preview.add_reaction(confirm_emoji)
                                    await preview.add_reaction(deny_emoji)
                                    @client.event
                                    async def on_reaction_add(reaction, user):
                                        if user.bot == 1:
                                            return None
                                        if str(reaction.emoji) == deny_emoji:
                                            await preview.delete()
                                            await ctx.send(hidden = True, content="콘 생성이 취소되었습니다.")
                                            return
                                        if str(reaction.emoji) == confirm_emoji:
                                            await preview.delete()
                                            embed=discord.Embed(title="최종 기능 추가 안내")
                                            embed.add_field(name="1. 명령어를 어떻게 추가하느냐", value="Discord Cogs Extension을 사용하면 명령어들을 확장프로그램처럼 껐다 켰다 할 수 있는데, 이게 Slash 명령어에도 적용이 되고, 자동완성 등록이 되는지가 문제. 테스트해 봤는데 어떻게 하는지 도저히 모르겠음", inline=False)
                                            embed.add_field(name="2. 봇 호스팅 관련 문제", value="디스코드 봇을 로컬에서 직접 돌리는 게 아니라 무료 호스팅 사이트를 이용하다 보니, 수정한 소스코드를 깃허브에 커밋하면, Heroku에서 빌드하고 시작하는 방식임. 가끔 Heroku에서 빌드제한을 걸어서 빌드가 제대로 작동되지 않는 경우가 있음. ", inline=False)
                                            embed.add_field(name="3. 이미지 호스팅 문제", value="Imgbb에서 제공하는 API가 유료라서 사용하기 좀 그럼, 디스코드 자체 이미지 링크를 따오고 있지만 불안정함", inline=False)
                                            embed.add_field(name="그래서 결론은?", value="콘 추가는 그냥 기존의 방식을 따르는 것으로로 일단 결정함, 일단 반자동화에 신경 쓰면 될 듯", inline=False)
                                            await ctx.send(hidden = True, embed=embed)
                                            return





        elif 작업 == "Edit":
            await ctx.send(content="기능 구현중입니다.")
        elif 작업 == "Delete":
            await ctx.send(content="기능 구현중입니다.")
        elif 작업 == "List":
            await ctx.send(content="기능 구현중입니다.")

def setup(client):
    client.add_cog(conmanage(client))

