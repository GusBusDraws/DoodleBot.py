from doodlebot import DoodleBot
import json
import numpy as np
import pandas as pd

def test1():
    bot = DoodleBot()
    test = '!prompt %emotion %invertebrate holding a %sci-fi-item'
    print(test)
    args = test.split(' ')[1:]
    for arg in args:
        print('arg:               ', arg)
        print('arg[1:]:           ', arg[1:])
        print('arg.startwith("%"):', arg[1:].startswith('%'))
        print('arg in df.columns: ', arg[1:] in bot.df.columns)

def test2():
    print()
    print('test2')
    bot = DoodleBot()
    test = '!prompt %emotion %invertebrate holding a %sci-fi-item'
    print(test)
    args = test.split(' ')[1:]
    print(bot.get_prompt(args))

def end_punc(self: DoodleBot):
    print()
    print('end_punc:')
    print('---------')
    msg = r'!prompt a %adjective %reptile %sci-fi-class eats a magical %food.'
    print(msg)
    args = msg.split(' ')[1:]
    prompt = self.get_prompt(args)
    print('-->', prompt)

def quote_punc(self):
    print()
    print('quote_punc:')
    print('-----------')
    msg = r'!prompt my pet %animal works as a "%job."'
    print(msg)
    args = msg.split(' ')[1:]
    prompt = self.get_prompt(args)
    print('-->', prompt)

def build_json(self: DoodleBot):
    print()
    col_dict = self.df.to_dict(orient='list')
    col_dict_no_nan = {}
    for keyword, kw_list in col_dict.items():
        col_dict_no_nan[keyword] = []
        for kw in kw_list:
            if not pd.isnull(kw):
                col_dict_no_nan[keyword].append(kw)
    with open('keywords.json', 'w') as f:
        json.dump(col_dict_no_nan, f, indent=2, skipkeys=False)
    with open('keywords.json', 'r') as f:
        lines = f.readlines()
    # with open('keywords.json', 'w') as f:
    #     f.truncate()
    #     for line in lines:
    #         if 'NaN' not in line:
    #             f.write(line)
    print('JSON updated.')

def load_json():
    print()
    with open('keywords.json', 'r') as f:
        kw_dict = json.load(f)
    df = pd.DataFrame.from_dict(kw_dict, orient='index')
    df = df.transpose()
    print(df)
    print(df['animal'][8])
    print(pd.isnull(df['animal'][8]))
    return df

def order_json():
    print()
    with open('keywords.json', 'r') as f:
        kw_dict = json.load(f)
    print(list(kw_dict.values())[0])
    for kw, kw_list in kw_dict.items():
        kw_dict[kw] = sorted(kw_list)
    with open('keywords.json', 'w') as f:
        json.dump(kw_dict, f, indent=2, skipkeys=False)
    print(list(kw_dict.values())[0])

def reddit_args(msg: str):
    args = msg.split(' ')[1:]
    print(args)
    print(type(args))
    print(*args)
    print(len(args))

def period_test(self):
    # Note: this actually became a test for keywords that contain other keywords
    msg = (
        '!prompt a building of tension between a %passive-ing-verb'
        ' %scifi-class and the %active-ing-verb %scifi-class within'
        ' %any-location %scifi-location %cosmic-location.')
    print(msg)
    args = msg.split(' ')[1:]
    print(args)
    prompt = self.get_prompt(args)
    print('-->', prompt)

def make_suggestions():
    print()
    suggestions = {}
    with open('suggestions.json', 'w') as f:
        json.dump(suggestions, f, indent=2, skipkeys=False)

def load_suggestions():
    print()
    print('Loading suggestions.json:')
    with open('suggestions.json', 'r') as f:
        suggestions = json.load(f)
    df = pd.DataFrame.from_dict(suggestions, orient='index')
    df = df.transpose()
    print(df)
    return df

def suggest(msg):
    print()
    with open('suggestions.json', 'r') as f:
        suggestions = json.load(f)
    print(suggestions)
    print(msg)
    args = msg.split(' ')[1:]
    if len(args) < 1:
        reply = (
            'To suggest words for the DoodleBot database, use the command'
            ' "!suggest" followed by the keyword for which you\'d like to'
            ' make your suggestion, then your word.'
            ' Example: "!suggest animal penguin"'
        )
    if len(args) == 1:
        keyword = args[0]
        try:
            if keyword not in suggestions['keyword']:
                suggestions['keyword'].append(keyword)
        except KeyError:
            suggestions['keyword'] = [keyword]
        reply = (f'The keyword "{keyword}" has been suggested.')
    else:
        keyword = args[0]
        words = args[1:]
        for word in words:
            try:
                existing_words = suggestions[keyword]
                if word not in existing_words:
                    existing_words.append(word)
            except KeyError:
                suggestions[keyword] = [word]
        reply = (f'"{(", ").join(words)}" suggested for the keyword "{keyword}".')
    print(reply)
    print(suggestions)
    with open('suggestions.json', 'w') as f:
        json.dump(suggestions, f, indent=2, skipkeys=False)

def suggest_item():
    msg = '!suggest irl-item coin'
    suggest(msg)

def suggest_kw():
    msg = '!suggest cryptid'
    suggest(msg)

def suggest_list():
    msg = '!suggest cryptid mothman chupacabra bigfoot'
    suggest(msg)


if __name__ == '__main__':
    bot = DoodleBot()
    # end_punc(bot)
    # quote_punc(bot)
    # build_json(bot)
    # df = load_json()
    # order_json()
    # reddit_args('!prompt')
    # period_test(bot)
    # make_suggestions()
    suggest_item()
    suggest_kw()
    suggest_list()
    load_suggestions()

