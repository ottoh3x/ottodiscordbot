import lightbulb
import requests
import json
import time
from bs4 import BeautifulSoup

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
@lightbulb.command('commands', 'commands')
@lightbulb.implements(lightbulb.SlashCommand)
async def commands(ctx):
    return await ctx.respond('**Commands**:\n**/anime <title>** : get anime details make sure to spell the name correctly and use "-" instead of space.\n**/weather <city>**\n**/online** : check how many players are on in the worst ball game ever\n**/ping**\n**/joke** : get a random joke :).')
   

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
