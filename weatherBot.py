import os
import discord
from discord.ext import commands
import requests


bot = commands.Bot(command_prefix='')

@bot.command()
async def temp_help(ctx):
    await ctx.send(f'command: `temp city country` '
                   f'\nexample: `temp muscat om` '
                   f'\nfor more info about the bot type command `temp_bot`')



@bot.command()
async def temp_bot(ctx):
    await ctx.send(f'created by <@{userid}>'
                   f'\nlanguage: python'
                   f'\napi: <https://openweathermap.org/current>'
                   f'\nsource code: <https://github.com/iamabdh>')


@bot.command()
async def temp(ctx, city, cont="om"):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city},{cont}&appid={apiKey}'
    response = requests.get(url)
    x = response.json()

    check = response.status_code
    if check == 200:
        await ctx.send(f"it's { round(x['main']['temp'] - 273.15)}°C in {x['name']}")
    else:
        await ctx.send(f'“__please enter valid city and country name__” '
                       f'\nfor more help type command `temp_help`')

bot.run(os.environ['discord_token'])
