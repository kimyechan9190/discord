import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print("이 프로그램은 AIM#0590이 무료로 공유하는 프로그램입니다.")

cid = 출근 채널 아이디
tid = 퇴근 채널 아이디
gid = 공지채널 아이디
dii = 관리자 채널 아이디
aid = 관리자 고유 ID
gtid = 블랙리스트 채널 ID
lid = 구매로그채널 ID
token = "봇 토큰"

@client.event
async def on_message(message):
    if message.content.startswith("!출근"):
        if message.author.id == aid:
            if message.channel.id == dii:
                embed = discord.Embed(title=f"{message.author.name}님이 출근하셨습니다.", color=0x00ff00)
                await client.get_channel(int(cid)).send (embed=embed)

    if message.content.startswith("!퇴근"):
        if message.author.id == aid:
            if message.channel.id == dii:
                embed = discord.Embed(title=f"{message.author.name}님이 퇴근하셨습니다.", color=0x00ff00)
                await client.get_channel(int(tid)).send (embed=embed)

    if message.content.startswith("!제품추가"):
        if message.author.id == aid:
            if message.channel.id == dii:
                await message.channel.send("제품 이름을 입력해주세요.")
                name = await client.wait_for('message', check=lambda message: message.author == message.author)
                name = name.content
                await message.channel.send("제품 가격을 입력해주세요.")
                k = await client.wait_for('message', check=lambda message: message.author == message.author)
                k = k.content
                await message.channel.send("제품 설명을 입력해주세요.")
                s = await client.wait_for('message', check=lambda message: message.author == message.author)
                s = s.content
                await message.channel.send("사진 URL을 입력해주세요.")
                url = await client.wait_for('message', check=lambda message: message.author == message.author)
                url = url.content
                await message.channel.send("제품 채널 ID를 입력해주세요.")
                id = await client.wait_for('message', check=lambda message: message.author == message.author)
                id = id.content
                await message.channel.send("제품추가가 완료되었습니다.")
                embed = discord.Embed(title=name, color=0x000000)
                embed.add_field(name="가격", value=str(k), inline=False)
                embed.add_field(name="기능", value=str(s))
                embed.set_image(url=f"{url}")
                await client.get_channel(int(id)).send (embed=embed)

    if message.content.startswith("!공지"):
        if message.author.id == aid:
            if message.channel.id == dii:
                msg = message.content[4:]
                embed = discord.Embed(title="공지사항", color=0x000000)
                embed.set_footer(text=msg)
                await client.get_channel(int(gid)).send (embed=embed)

    if message.content.startswith('!블랙리스트'):
        if message.author.guild_permissions.ban_members:
            try:
                target = message.mentions[0]
            except:
                await message.channel.send('유저가 지정되지 않았습니다')
                return

            j = message.content.split(" ")
            try:
                reason = j[2]
            except IndexError:
                reason = 'None'
            embed = discord.Embed(title='블랙리스트',
                                  description=f'{target}님이 {message.guild.name} 블랙리스트에 추가되었습니다.\n사유: {reason}',
                                  colour=discord.Colour.red())
            try:
                await target.send(embed=embed)
            except:
                pass
            embed = discord.Embed(title="블랙리스트 추가", color=0x000000)
            embed.add_field(name="닉네임", value=str(target), inline=False)
            embed.add_field(name="아이디", value=str(target.id), inline=False)
            embed.add_field(name="사유", value=str(reason), inline=False)
            await client.get_channel(int(gtid)).send(embed=embed)
            await target.ban(reason=reason)

    if message.content.startswith("!로그"):
        if message.author.id == aid:
            if message.channel.id == dii:
                target = message.mentions[0]
                await message.channel.send("제품 이름을 입력해주세요.")
                name = await client.wait_for('message', check=lambda message: message.author == message.author)
                name = name.content
                embed = discord.Embed(title=f"{target}님 {name} 제품 구매 감사합니다!")
                await client.get_channel(int(lid)).send(embed=embed)

client.run(token)