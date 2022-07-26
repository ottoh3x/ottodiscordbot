import lightbulb
import requests
import json
import time
from bs4 import BeautifulSoup
import socket
import random


skins = ["https://skins.vanis.io/s/e8dH91",
"https://skins.vanis.io/s/5eyDXp",
"https://skins.vanis.io/s/0p0eDS",
"https://skins.vanis.io/s/0dwYNO",
"https://skins.vanis.io/s/LLaPcd",
"https://skins.vanis.io/s/47tRRD",
"https://skins.vanis.io/s/EWKXsA",
"https://skins.vanis.io/s/gDn27a",
"https://skins.vanis.io/s/tav9cJ",
"https://skins.vanis.io/s/gYVX7t",
"https://skins.vanis.io/s/rsWLXV",
"https://skins.vanis.io/s/JktXqo",
"https://skins.vanis.io/s/uuNE72",
"https://skins.vanis.io/s/ourD1Z",
"https://skins.vanis.io/s/93VF2l",
"https://skins.vanis.io/s/rRUQaA",
"https://skins.vanis.io/s/1bkRKW",
"https://skins.vanis.io/s/CGKRdC",
"https://skins.vanis.io/s/m6DVK9",
"https://skins.vanis.io/s/znbiG9",
"https://skins.vanis.io/s/bAc0XK",
"https://skins.vanis.io/s/Nh2wp8",
"https://skins.vanis.io/s/FPa85u",
"https://skins.vanis.io/s/trtcgF",
"https://skins.vanis.io/s/7gOgMS",
"https://skins.vanis.io/s/QGpoFG",
"https://skins.vanis.io/s/w6AkAs",
"https://skins.vanis.io/s/FSQ8p1",
"https://skins.vanis.io/s/9zzNwj",
"https://skins.vanis.io/s/DmPmmU",
"https://skins.vanis.io/s/ywGIA8",
"https://skins.vanis.io/s/MybluM",
"https://skins.vanis.io/s/aJVE3c",
"https://skins.vanis.io/s/7MoyCI",
"https://skins.vanis.io/s/xVXzEQ",
"https://skins.vanis.io/s/x8Eb00",
"https://skins.vanis.io/s/H8RS3A",
"https://skins.vanis.io/s/gViABe",
"https://skins.vanis.io/s/qTCmOm",
"https://skins.vanis.io/s/HFurgu",
"https://skins.vanis.io/s/A9xfSn",
"https://skins.vanis.io/s/0VhANk",
"https://skins.vanis.io/s/PNB2xs",
"https://skins.vanis.io/s/vz3kGX",
"https://skins.vanis.io/s/xxFUhM",
"https://skins.vanis.io/s/JrAf0T",
"https://skins.vanis.io/s/EDz9TH",
"https://skins.vanis.io/s/BKwKtu",
"https://skins.vanis.io/s/RByxwD",
"https://skins.vanis.io/s/1Txuhu",
"https://skins.vanis.io/s/vazO4f",
"https://skins.vanis.io/s/wYVTMd",
"https://skins.vanis.io/s/lfCGkl",
"https://skins.vanis.io/s/EFiy92",
"https://skins.vanis.io/s/xkkPgn",
"https://skins.vanis.io/s/DMQY78",
"https://skins.vanis.io/s/vu8xlT",
"https://skins.vanis.io/s/Yu8Reo",
"https://skins.vanis.io/s/ZF6tbE",
"https://skins.vanis.io/s/sh9j97",
"https://skins.vanis.io/s/igup7V",
"https://skins.vanis.io/s/Tk3DvP",
"https://skins.vanis.io/s/hodaqk",
"https://skins.vanis.io/s/1FqrAT",
"https://skins.vanis.io/s/XgOz8L",
"https://skins.vanis.io/s/9RtCCt",
"https://skins.vanis.io/s/J6zmMD",
"https://skins.vanis.io/s/P8dJpU",
"https://skins.vanis.io/s/NhI6vT"]

bot = lightbulb.BotApp(token="OTk5NzAxMTEyODAwMTY5OTg1.GBCkBn.ucJ4U_5-q1giF1dzW4qXvL_F2T2mKXLlmGO8yo"
                       )


@bot.command()
@lightbulb.option(f"city", 'ur city')
@lightbulb.command('weather', 'it gives u details abt the weather')
@lightbulb.implements(lightbulb.SlashCommand)
async def weather(ctx):
    url = f"http://api.weatherapi.com/v1/current.json?key=d0f6ff5c4eaa40b0b94195841222207&q={ctx.options.city}&aqi=no"
    d = requests.get(url).text
    data = json.loads(d)
    citi = data['location']['name']
    region = data['location']['region']
    country = data['location']['country']
    time = data['location']['localtime']
    temp = data['current']['temp_c']
    condition = data['current']['condition']['text']

    await ctx.respond(f"**Temperature**: {temp} °\n**Condition**: {condition}\n**City**: {citi}\n**Country**: {country}\n**Region**: {region}\n**Time**: {time}")


@bot.command()
@lightbulb.command('ping', 'Pong')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    before = time.monotonic()
    message = await ctx.respond("Pong!")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"Pong!  `{int(ping)}ms`")

@bot.command()
@lightbulb.command('skin', 'Returns a vanis skin.')
@lightbulb.implements(lightbulb.SlashCommand)
async def skin(ctx):
    skin = random.choice(skins)
    return await ctx.respond(f"- {skin}")


@bot.command()
@lightbulb.command('commands', 'commands')
@lightbulb.implements(lightbulb.SlashCommand)
async def commands(ctx):
    return await ctx.respond('**Commands**:\n**/anime <title>** : get anime details make sure to spell the name correctly and use "-" instead of space.\n**/weather <city>**\n**/online** : check how many players are on in the worst ball game ever\n**/ping**\n**/joke** : get a random joke :).\n**/meme** : get a random meme :D.\n**/skin**: it returns a random vanis skin')
   

@bot.command()
@lightbulb.command('gotch', 'fun trick')
@lightbulb.implements(lightbulb.SlashCommand)
async def gotch(ctx):
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return await ctx.respond(f"**IP Address:** {ip_address}")



@bot.command()
@lightbulb.command('joke', 'get a random joke')
@lightbulb.implements(lightbulb.SlashCommand)
async def joke(ctx):
    url="https://icanhazdadjoke.com"
    r = requests.get(url).text
    soup = BeautifulSoup(r,"html.parser")
    joke = soup.find("p","subtitle").text
    return await ctx.respond(joke)

@bot.command()
@lightbulb.command('meme', 'get a random meme')
@lightbulb.implements(lightbulb.SlashCommand)
async def meme(ctx):
    url="https://meme-api.herokuapp.com/gimme"
    r = requests.get(url).json()['url']
    return await ctx.respond(r)

@bot.command()
@lightbulb.command('online', 'online players')
@lightbulb.implements(lightbulb.SlashCommand)
async def online(ctx):

    url = f'https://vanis.io/gameservers.json'
    r = requests.get(url).json()
    ffa1currentplayers = r[26]['currentPlayers']
    ffa2currentplayers = r[0]['currentPlayers']
    ffa1region = r[26]['region']
    ffa2region = r[0]['region']
    megasplit1currentplayers = r[27]['currentPlayers']
    megasplit1region = r[27]['region']

    await ctx.respond(f"**FFA1**: {ffa1currentplayers}/70 Current Players\n**FFA2**: {ffa2currentplayers}/50 Current Players \n**MegaSplit 1**: {megasplit1currentplayers}/60 Current Players")


@bot.command()
@lightbulb.option(f"title", 'anime title')
@lightbulb.command('anime', 'anime details')
@lightbulb.implements(lightbulb.SlashCommand)
async def anime(ctx):
    url = f'https://ottogo.vercel.app/api/details/{ctx.options.title}'
    r = requests.get(url).json()
    title = r['title']
    released = r['year']
    summary = r['plot_summary'].strip()
    episodes = r['episodes']
    status = r['status']
    await ctx.respond(f"**Title**: {title}\n**Date Of Release**: {released}\n**Summary**: {summary}\n**Episodes**: {episodes}\n**Status**: {status} ")


bot.run()
