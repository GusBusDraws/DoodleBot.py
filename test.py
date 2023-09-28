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
    bot = DoodleBot()
    test = '!prompt %emotion %invertebrate holding a %sci-fi-item'
    print(test)
    args = test.split(' ')[1:]
    print(bot.get_prompt(args))


if __name__ == '__main__':
    test2()
