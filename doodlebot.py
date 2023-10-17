import json
import pandas as pd
from pathlib import Path
import random


class DoodleBot():
    def __init__(self):
        # Check that CSV_PATH exists
        kw_path = Path('keywords.json')
        if not kw_path.exists():
            raise ValueError('Keywords not found.')
        # Load JSON
        with open(kw_path, 'r') as f:
            kw_dict = json.load(f)
        # Load DF sideways so missing rows read as missing cols
        self.df = pd.DataFrame.from_dict(kw_dict, orient='index')
        self.df = self.df.transpose()
        self.valid_keys = self.df.columns.values
        self.last_arg_tuple = None

    def get_help(self):
        help_msg = (
            'Send a message beginning with "!prompt" that includes at least one'
            ' of the following keywords marked with a leading "%":\n'
            f"{', '.join(self.df.columns)}"
        )
        return help_msg

    def get_prompt(self, args):
        prompt_list = []
        for arg in args:
            if '%' in arg:
                # Typically keyword will be directly after "%"
                if arg[1:] in self.valid_keys:
                    replaced = self.get_random_entry(arg[1:])
                    prompt_list.append(replaced)
                else:
                    found = False
                    i = 0
                    while not found and i <= len(self.valid_keys):
                        key = self.valid_keys[i]
                        if key in arg:
                            start = arg.find('%')
                            sub = arg[start+1 : len(key)+start+1]
                            # If a faulty substituted keyword passes through,
                            # catch the KeyError exception
                            try:
                                replaced = self.get_random_entry(sub)
                            except KeyError:
                                replaced = sub
                            full = (
                                arg[:start] + replaced + arg[len(key)+start+1:])
                            prompt_list.append(full)
                            found = True
                        i += 1
                    if not found:
                        print(f'{arg} not replaced.')
            else:
                prompt_list.append(arg)
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
        prompt_list[0] = prompt_list[0].capitalize()
        return prompt_list
