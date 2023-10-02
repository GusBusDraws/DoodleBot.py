from bot import DoodleBot

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
    msg = r'!prompt a big %reptile %sci-fi-class eats a magical %food.'
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


if __name__ == '__main__':
    bot = DoodleBot()
    end_punc(bot)
    quote_punc(bot)

