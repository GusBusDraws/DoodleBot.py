import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from pathlib import Path
# Local imports
from doodlebot import DoodleBot


description = (
    'DoodleBot is a prompt-generation bot that helps reduce'
    ' friction when making art.')
intents = discord.Intents.default()
intents.message_content = True
doodle_state = DoodleBot()
bot = commands.Bot(command_prefix='!', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command()
async def prompt(ctx, *args):
    # If no arguments are passed after the command
    if len(args) == 0:
        await ctx.send(doodle_state.get_help())
    else:
        doodle_state.last_arg_tuple = args
        result = doodle_state.get_prompt(args)
        response = f"Here's your prompt:\n{result}"
        print(f'{ctx.author.name}: ', ctx.message.content)
        print(f'{args=}')
        print(f'{bot.user}:', response)
        await ctx.channel.send(response)

@bot.command()
async def reroll(ctx):
    if doodle_state.last_arg_tuple is None:
        await ctx.send('Try calling !prompt first!')
    else:
        prompt = doodle_state.get_prompt(doodle_state.last_arg_tuple)
        await ctx.send(prompt)

@bot.command()
async def suggest(ctx, *args):
    response = doodle_state.suggest(args)
    print(f'{ctx.author.name}: ', ctx.message.content)
    print(f'{args=}')
    print(f'{bot.user}:', response)
    await ctx.channel.send(response)


if __name__ == '__main__':
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')
    bot.run(token)
