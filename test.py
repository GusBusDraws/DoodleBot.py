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
    msg = (
        '!prompt a building of tension between a %passive-ing-verb'
        ' %scifi-class and the %active-ing-verb %scifi-class within'
        ' %location %scifi-location %cosmic-location.')
    print(msg)
    args = msg.split(' ')[1:]
    print(args)
    prompt = self.get_prompt(args)
    print('-->', prompt)


if __name__ == '__main__':
    bot = DoodleBot()
    # end_punc(bot)
    # quote_punc(bot)
    # build_json(bot)
    # df = load_json()
    # order_json()
    # reddit_args('!prompt')
    period_test(bot)

