import discord
from discord_slash import SlashCommand # Importing the newly installed library.
import os
from discord_slash.utils.manage_commands import create_option

client = discord.Client(intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True) # Declares slash commands through the client.

@client.event
async def on_ready():
    print("준비된!")

guild_ids = [595824909473808403]

# @slash.slash(name='ping', description="작동 확인")
# async def _ping(ctx):
#     await ctx.send(f"Pong! ({client.latency*1000}ms)")

@slash.slash(name="우리핵안무", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 우리핵안무(ctx):
    embed=discord.Embed(description="우리핵안무", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/0tJN50r/dnflgordksan.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="우리핵안녕", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 우리핵안경(ctx):
    embed=discord.Embed(description="우리핵안녕", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/RgfHT8J/dnflgordkssud.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="우리핵우쭐", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 우리핵우쭐(ctx):
    embed=discord.Embed(description="우리핵우쭐", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/LSFYDDV/dnflgordnWnf.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="우리핵애교", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 우리핵애교(ctx):
    embed=discord.Embed(description="우리핵애교", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/h8S8qDZ/dnflgordory.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="우리핵드럼", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 우리핵드럼(ctx):
    embed=discord.Embed(description="우리핵드럼", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/QccRgHK/dnflgoremfja.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="우리핵흐뭇", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 우리핵흐뭇(ctx):
    embed=discord.Embed(description="우리핵흐뭇", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/DtwzB4F/dnflgorgmant.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="우리핵빵야", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 우리핵빵야(ctx):
    embed=discord.Embed(description="우리핵빵야", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/PmQCP05/dnflgor-Qkddi.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="우리핵박수", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 우리핵박수(ctx):
    embed=discord.Embed(description="우리핵박수", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/jLdkV8L/dnflgorqkrtn.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="우리핵갸우뚱", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 우리핵갸우뚱(ctx):
    embed=discord.Embed(description="우리핵갸우뚱", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/XZ9SBzw/dnflgorridnEnd.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="우리핵쌍안경", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 우리핵쌍안경(ctx):
    embed=discord.Embed(description="우리핵쌍안경", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/nzkLz7J/dnflgorTkddksrud.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="우리핵투정", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 우리핵투정(ctx):
    embed=discord.Embed(description="우리핵투정", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/2ZxrHyd/dnflgorxnwjd.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="앵무문워크", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 앵무문워크(ctx):
    embed=discord.Embed(description="앵무문워크", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/Wt2DZm1/dodanansdnjzm.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="앵무댄스", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 앵무댄스(ctx):
    embed=discord.Embed(description="앵무댄스", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/gM3pJQx/dodaneostm.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="앵무눈물", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 앵무눈물(ctx):
    embed=discord.Embed(description="앵무눈물", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/TcjHZQv/dodansnsanf.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="앵무선글", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 앵무선글(ctx):
    embed=discord.Embed(description="앵무선글", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/m6txyNv/dodantjsrmf.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="앵무팝콘", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 앵무팝콘(ctx):
    embed=discord.Embed(description="앵무팝콘", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/DfBNjpM/dodanvkqzhs.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="혼란앵무", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 혼란앵무(ctx):
    embed=discord.Embed(description="혼란앵무", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/S5hfbCd/ghsfksdodan.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="RGB", description="디시콘을 보내줌", guild_ids=guild_ids)
async def RGB(ctx):
    embed=discord.Embed(description="RGB", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/W5xDP35/RGB.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="RGB더줘", description="디시콘을 보내줌", guild_ids=guild_ids)
async def RGB더줘(ctx):
    embed=discord.Embed(description="RGB더줘", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/MCkFVkN/RGBejwnj.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="RGB램", description="디시콘을 보내줌", guild_ids=guild_ids)
async def RGB램(ctx):
    embed=discord.Embed(description="RGB램", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/9rVHdgc/RGBfoa.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="RGB한국", description="디시콘을 보내줌", guild_ids=guild_ids)
async def RGB한국(ctx):
    embed=discord.Embed(description="RGB한국", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/tX44kQt/RGBgksrnr.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="RGB뽕", description="디시콘을 보내줌", guild_ids=guild_ids)
async def RGB뽕(ctx):
    embed=discord.Embed(description="RGB뽕", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/Z65ttZx/RGBQhd.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="RGB빔", description="디시콘을 보내줌", guild_ids=guild_ids)
async def RGB빔(ctx):
    embed=discord.Embed(description="RGB빔", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/7nyFst9/RGBqla.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="RGB그자체", description="디시콘을 보내줌", guild_ids=guild_ids)
async def RGB그자체(ctx):
    embed=discord.Embed(description="RGB그자체", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/FY3vFF9/RGBrmwkcp.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="RGB스트립", description="디시콘을 보내줌", guild_ids=guild_ids)
async def RGB스트립(ctx):
    embed=discord.Embed(description="RGB스트립", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/PQrw24B/RGBtmxmflq.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="웃음수", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 웃음수(ctx):
    embed=discord.Embed(description="웃음수", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/7v3HQdv/dntdmatn.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="웃사수", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 웃사수(ctx):
    embed=discord.Embed(description="웃사수", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/XVkR0r4/dnttktn.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="또웃수", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 또웃수(ctx):
    embed=discord.Embed(description="또웃수", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/zPXw8RX/Ehdnttn.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="당당수", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 당당수(ctx):
    embed=discord.Embed(description="당당수", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/VjNHSxs/ekdekdtn.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="화난수", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 화난수(ctx):
    embed=discord.Embed(description="화난수", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/0XrDjD6/ghkskstn.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="힙사수", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 힙사수(ctx):
    embed=discord.Embed(description="힙사수", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/9H03xkw/glqtktn.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="자랑수", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 자랑수(ctx):
    embed=discord.Embed(description="자랑수", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/6RRJPGK/wkfkdtn.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="자기과시", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 자기과시(ctx):
    embed=discord.Embed(description="자기과시", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/9YTjq7p/wkrlrhktl.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="냥모찌", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 냥모찌(ctx):
    embed=discord.Embed(description="냥모찌", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/YDGXZnS/sidahWl.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="냥구토", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 냥구토(ctx):
    embed=discord.Embed(description="냥구토", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/MNGvbNy/sidrnxh.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="냥경악", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 냥경악(ctx):
    embed=discord.Embed(description="냥경악", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/5v3RFZX/sidruddkr.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="냥경악2", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 냥경악2(ctx):
    embed=discord.Embed(description="냥경악2", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/c64f6yq/sidruddkr2.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="냥경악3", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 냥경악3(ctx):
    embed=discord.Embed(description="냥경악3", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/KhQynQn/sidruddkr3.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="냥슬픔", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 냥슬픔(ctx):
    embed=discord.Embed(description="냥슬픔", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/VxZ3g53/sidtmfvma.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="냥선글", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 냥선글(ctx):
    embed=discord.Embed(description="냥선글", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/fXgGK2s/sidtjsrmf.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="냥정색", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 냥정색(ctx):
    embed=discord.Embed(description="냥정색", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/d43H7m6/sidwjdtor.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="썬글수", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 썬글수(ctx):
    embed=discord.Embed(description="썬글수", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/c31PqFh/Tjsrmftn.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="클럽수", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 클럽수(ctx):
    embed=discord.Embed(description="클럽수", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/BgS2wVM/zmffjqtn.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="코딩중", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 코딩중(ctx):
    embed=discord.Embed(description="코딩중", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/GsMdKbQ/zheldwnd.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="제리작별", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 제리작별(ctx):
    embed=discord.Embed(description="제리작별", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/YXLJ4Kh/wpflwkrquf.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="제리끄덕", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 제리끄덕(ctx):
    embed=discord.Embed(description="제리끄덕", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/5rNjbsz/wpflRmejr.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="제리냄새", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 제리냄새(ctx):
    embed=discord.Embed(description="제리냄새", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/541yHWf/wpflsoato.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="제리인사", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 제리인사(ctx):
    embed=discord.Embed(description="제리인사", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/VQtCLB2/wpfldlstk.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="제리인사2", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 제리인사2(ctx):
    embed=discord.Embed(description="제리인사2", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/Gs7sNxZ/wpfldlstk2.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="제리불편", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 제리불편(ctx):
    embed=discord.Embed(description="제리불편", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/Sfy5ZNP/wpflqnfvus.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="제리폭소", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 제리폭소(ctx):
    embed=discord.Embed(description="제리폭소", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/JKxvDfN/wpflvhrth.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="둘리못살아", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 둘리못살아(ctx):
    embed=discord.Embed(description="둘리못살아", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/svjkV45/enfflahttkfdk.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="둘리초능력", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 둘리초능력(ctx):
    embed=discord.Embed(description="둘리초능력", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/brTzWWr/enfflchsmdfur.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="둘리철썩", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 둘리철썩(ctx):
    embed=discord.Embed(description="둘리철썩", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/QcFxQPd/enfflcjfTjr.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="둘리처신", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 둘리처신(ctx):
    embed=discord.Embed(description="둘리처신", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/68bkXKD/enfflcjtls.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="둘리웃음", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 둘리웃음(ctx):
    embed=discord.Embed(description="둘리웃음", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/GTzqBwp/enffldntdma.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="둘리호잇", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 둘리호잇(ctx):
    embed=discord.Embed(description="둘리호잇", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/jfPMZ6t/enfflghdlt.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="둘리호의", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 둘리호의(ctx):
    embed=discord.Embed(description="둘리호의", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/ZgXKH8L/enfflghdml.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="둘리흑우", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 둘리흑우(ctx):
    embed=discord.Embed(description="둘리흑우", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/Cwy8nSM/enfflgmrdn.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="둘리밥줘", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 둘리밥줘(ctx):
    embed=discord.Embed(description="둘리밥줘", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/0ZyrcBd/enfflqkqwnj.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="둘리꼴받", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 둘리꼴받(ctx):
    embed=discord.Embed(description="둘리꼴받", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/ZGNqMdT/enfflRhfqke.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="둘리나가", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 둘리나가(ctx):
    embed=discord.Embed(description="둘리나가", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/nDTgfsR/enfflskrk.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="둘리냄새", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 둘리냄새(ctx):
    embed=discord.Embed(description="둘리냄새", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/LQ6TRk3/enfflsoato.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="둘리성능", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 둘리성능(ctx):
    embed=discord.Embed(description="둘리성능", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/KxWvjMF/enffltjdsmd.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="둘리선넘네", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 둘리선넘네(ctx):
    embed=discord.Embed(description="둘리선넘네", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/2N1PtPW/enffltjssjasp.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="둘리싯팔", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 둘리싯팔(ctx):
    embed=discord.Embed(description="둘리싯팔", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/y6NxGJK/enffltltvkf.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="둘리좋지", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 둘리좋지(ctx):
    embed=discord.Embed(description="둘리좋지", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/2vrRB9D/enfflwhgwl.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="둘리정신", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 둘리정신(ctx):
    embed=discord.Embed(description="둘리정신", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/5s9GtMr/enfflwjdtls.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="둘리죽상", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 둘리죽상(ctx):
    embed=discord.Embed(description="둘리죽상", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/3vyJf3X/enfflwnrtkd.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="댕모찌", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 댕모찌(ctx):
    embed=discord.Embed(description="댕모찌", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/N6JByfF/eodahWl.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="라이젠", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 라이젠(ctx):
    embed=discord.Embed(description="라이젠", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/mzF9KZm/fkdlwps.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="또버그", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 또버그(ctx):
    embed=discord.Embed(description="또버그", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/N7p6WZw/Ehqjrm.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="IT", description="디시콘을 보내줌", guild_ids=guild_ids)
async def IT(ctx):
    embed=discord.Embed(description="IT", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/X7v1v86/IT.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="대부분버그", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 대부분버그(ctx):
    embed=discord.Embed(description="대부분버그", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/Fq46YmD/eoqnqnsqjrm.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="계산중", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 계산중(ctx):
    embed=discord.Embed(description="계산중", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/NK7fTYK/rPtkswnd.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="뉴스수", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 뉴스수(ctx):
    embed=discord.Embed(description="뉴스수", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/vzd5Tss/sbtmtn.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="짜잔", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 짜잔(ctx):
    embed=discord.Embed(description="짜잔", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/3pkXM2D/Wkwks.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="깃헙", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 깃헙(ctx):
    embed=discord.Embed(description="깃헙", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/NscGpjy/rltgjq.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="그런겜", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 그런겜(ctx):
    embed=discord.Embed(description="그런겜", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/JmXyHtD/rmfjsrpa.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="이륙", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 이륙(ctx):
    embed=discord.Embed(description="이륙", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/s9B1Ghq/dlfbr.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="존버하자", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 존버하자(ctx):
    embed=discord.Embed(description="존버하자", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/c1ZcLd1/whsqjgkwk.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="의외정상", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 의외정상(ctx):
    embed=discord.Embed(description="의외정상", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/YkrNHZt/dmldhlwjdtkd.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="정상", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 정상(ctx):
    embed=discord.Embed(description="정상", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/DDzJtfC/wjdtkd.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="꼭사라", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 꼭사라(ctx):
    embed=discord.Embed(description="꼭사라", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/J5D6L5Q/Rhrtkfk.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="노트북", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 노트북(ctx):
    embed=discord.Embed(description="노트북", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/8sbh9sH/shxmqnr.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="환불", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 환불(ctx):
    embed=discord.Embed(description="환불", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/syF5YHy/ghksqnf.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="제리도발", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 제리도발(ctx):
    embed=discord.Embed(description="제리도발", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/n8c23xH/wpflehqkf.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="AMD", description="디시콘을 보내줌", guild_ids=guild_ids)
async def AMD(ctx):
    embed=discord.Embed(description="AMD", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/G38yN0M/AMD.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="따귀", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 따귀(ctx):
    embed=discord.Embed(description="따귀", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/dMxkg47/Ekrnl.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="따봉", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 따봉(ctx):
    embed=discord.Embed(description="따봉", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/qsxZxfT/Ekqhd.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="뱀부즐", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 뱀부즐(ctx):
    embed=discord.Embed(description="뱀부즐", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/X5GPtbb/qoaqnwmf.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="고뱀부", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 고뱀부(ctx):
    embed=discord.Embed(description="고뱀부", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/NNrcP18/rhqoaqn.png")
    await ctx.send(embed=embed)

@slash.slash(name="편안", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 편안(ctx):
    embed=discord.Embed(description="편안", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/v3Q021S/vusdks.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="어케했", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 어케했(ctx):
    embed=discord.Embed(description="어케했", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/j6xRBp3/djzpgoT.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="의도된", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 의도된(ctx):
    embed=discord.Embed(description="의도된", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/yRdYyFv/dmlehehls.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="불편", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 불편(ctx):
    embed=discord.Embed(description="불편", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/2ymLSLf/qnfvus.png")
    await ctx.send(embed=embed)
    
@slash.slash(name="꼬우면", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 꼬우면(ctx):
    embed=discord.Embed(description="꼬우면", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/0qPmbfz/Rhdnaus.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="네말이맞아", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 네말이맞아(ctx):
    embed=discord.Embed(description="네말이맞아", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/xSP9MFm/spakfdlakwdk.gif")
    await ctx.send(embed=embed)
    
@slash.slash(name="식은땀", description="디시콘을 보내줌", guild_ids=guild_ids)
async def 식은땀(ctx):
    embed=discord.Embed(description="식은땀", color=0xFFFFFF)
    embed.set_image(url="https://i.ibb.co/2YYfDzB/tlrdms-Eka.gif")
    await ctx.send(embed=embed)      



# 로그에 Detected discord.Client! It is highly recommended to use `commands.Bot`. Do not add any `on_socket_response` event. 메세지뜸, 해결해야함.
# 명령어 제한 100개

client.run(os.environ['token'])