# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup as BS

import discord
from discord.ext import commands


TOKEN = ''

def am(country, prm):
	if country == 'country/world':
		country = ''
	r = requests.get('https://www.worldometers.info/coronavirus/' + country)
	html = BS(r.content, 'html.parser')
	corona_title = html.select('#maincounter-wrap > h1')
	corona_count = html.select('.maincounter-number > span')
	if prm == 'cases':
		ans = corona_title[0].text + ' ' + corona_count[0].text
		return ans
	elif prm == 'deaths':
		ans = corona_title[1].text + ' ' + corona_count[1].text
		return ans
	elif prm == 'recovered':
		ans = corona_title[2].text + ' ' + corona_count[2].text
		return ans
	else:
		return 'error'

bot = commands.Bot(command_prefix='/')

@bot.command(pass_context=True)
async def covid(ctx, country, prm):
	if prm == 'cases':
		strg = am('country/' + country, prm)
		await ctx.send(strg)
	elif prm == 'deaths':
		strg = am('country/' + country, prm)
		await ctx.send(strg)
	elif prm == 'recovered':
		strg = am('country/' + country, prm)
		await ctx.send(strg)
	else:
		await ctx.send('strg')

bot.run(TOKEN)
