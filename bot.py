import lightbulb
import requests
import json
import time


bot = lightbulb.BotApp(token="OTk5NzAxMTEyODAwMTY5OTg1.GBCkBn.ucJ4U_5-q1giF1dzW4qXvL_F2T2mKXLlmGO8yo",
                       default_enabled_guilds=(867864188545531929, 934581952118403142, 929699967143116851))


@bot.command()
@lightbulb.command('ping', 'Pong')
@lightbulb.implements(lightbulb.PrefixCommand)
async def ping(ctx):
    before = time.monotonic()
    message = await ctx.respond("Pong!")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"Pong!  `{int(ping)}ms`")


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

    await ctx.respond(f"**FFA1**: {ffa1currentplayers}/70 Current Players | **Region**: {ffa1region}\n**FFA2**: {ffa2currentplayers}/50 Current Players | **Region**: {ffa2region}\n**MegaSplit 1**: {megasplit1currentplayers}/60 Current Players | **Region**: {megasplit1region}")


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
