import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import pandas as pd
import random


intents = discord.Intents.default()
intents.message_content = True


CSV_PATH = ('what-to-draw-2021-09-14-1953.csv')

class DoodleBot(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix='!', intents=intents)
        # Check that CSV_PATH exists
        if os.path.exists(CSV_PATH):
            self.df = pd.read_csv(CSV_PATH)
        else:
            raise ValueError('CSV not found')
        self.last_arg_tuple = None

    def get_help(self):
        help_msg = (
            'Type a message after "!prompt" that includes one of the'
            ' following keywords marked with a leading "%":\n'
            f"{', '.join(self.df.columns)}"
        )
        return help_msg

    def get_prompt(self, arg_tuple):
        prompt_list = [
            self.get_random_entry(arg[1:])
            if arg.startswith('%') and arg[1:] in self.df.columns.values
            else arg for arg in arg_tuple
        ]
        prompt_list = self.check_grammar(prompt_list)
        prompt = ' '.join(prompt_list)
        return prompt

    def get_random_entry(self, col):
        rand_entry = random.choice(self.df[col])
        if pd.isnull(rand_entry):
            rand_entry = self.get_random_entry(col)
        elif rand_entry in self.df.columns.values:
            rand_entry = self.get_random_entry(rand_entry)
        return rand_entry

    def check_grammar(self, prompt_list):
        for i, word in enumerate(prompt_list):
            if word == 'a':
                # If the next word in prompt_list starts with a vowel:
                if prompt_list[i + 1][0] in 'aeiou':
                    # Replace the item at this position in prompt_list (word)
                    # with 'an' instead of 'a'
                    prompt_list[i] = 'an'
            elif word == 'an':
                # If the next word in prompt_list does not start with a vowel:
                if prompt_list[i + 1][0] not in 'aeiou':
                    # Replace the item at this position in prompt_list (word)
                    # with 'a' instead of 'an'
                    prompt_list[i] = 'a'
            if i == 0:
                prompt_list[i] = word.capitalize()
        return prompt_list

bot = DoodleBot()

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command()
async def prompt(ctx, *args):
    # If no arguments are passed after the command
    if len(args) == 0:
        await ctx.send(bot.get_help())
    else:
        bot.last_arg_tuple = args
        response = f"Here's your prompt:\n{bot.get_prompt(args)}"
        print(f'{ctx.author.name}: ', ctx.message.content)
        print(f'{args=}')
        print(f'{bot.user}:', response)
        await ctx.channel.send(response)

@bot.command()
async def reroll(ctx):
    if bot.last_arg_tuple is None:
        await ctx.send('Try calling !prompt first!')
    else:
        prompt = bot.get_prompt(bot.last_arg_tuple)
        await ctx.send(prompt)


if __name__ == '__main__':
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')
    bot.run(token)
