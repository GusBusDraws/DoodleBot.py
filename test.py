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

def end_punc(self):
    print()
    print('end_punc:')
    print('---------')
    msg = r'!prompt a big %reptile %sci-fi-class eats a magical %food.'
    print(msg)
    args = msg.split(' ')[1:]
    prompt_list = []
    for arg in args:
        if '%' in arg:
            # Typically keyword will be directly after "%"
            if arg[1:] in self.valid_keys:
                print(f'{arg[1:]=}')
                replaced = self.get_random_entry(arg[1:])
                print(f'{replaced=}')
                prompt_list.append(replaced)
            else:
                print(f'{arg=}')
                found = False
                i = 0
                while not found and i <= len(self.valid_keys):
                    key = self.valid_keys[i]
                    if key in arg:
                        start = arg.find('%')
                        sub = arg[start+1 : len(key)+1]
                        print(f'{sub=}')
                        replaced = self.get_random_entry(sub)
                        print(f'{replaced=}')
                        full = arg[:start] + replaced + arg[len(key)+1:]
                        print(f'{full=}')
                        prompt_list.append(full)
                        found = True
                    i += 1
                if not found:
                    print(f'{arg} not replaced.')
        else:
            prompt_list.append(arg)
    prompt_list = self.check_grammar(prompt_list)
    prompt = ' '.join(prompt_list)
    print(prompt)

def quote_punc(self):
    print()
    print('quote_punc:')
    print('-----------')
    msg = r'!prompt my pet %animal works as a "%job."'
    print(msg)
    args = msg.split(' ')[1:]
    prompt_list = []
    for arg in args:
        if '%' in arg:
            # Typically keyword will be directly after "%"
            if arg[1:] in self.valid_keys:
                print(f'{arg[1:]=}')
                replaced = self.get_random_entry(arg[1:])
                print(f'{replaced=}')
                prompt_list.append(replaced)
            else:
                print(f'{arg=}')
                found = False
                i = 0
                while not found and i <= len(self.valid_keys):
                    key = self.valid_keys[i]
                    if key in arg:
                        start = arg.find('%')
                        sub = arg[start+1 : len(key)+start+1]
                        print(f'{sub=}')
                        replaced = self.get_random_entry(sub)
                        print(f'{replaced=}')
                        full = arg[:start] + replaced + arg[len(key)+start+1:]
                        print(f'{full=}')
                        prompt_list.append(full)
                        found = True
                    i += 1
                if not found:
                    print(f'{arg} not replaced.')
        else:
            prompt_list.append(arg)
    prompt_list = self.check_grammar(prompt_list)
    prompt = ' '.join(prompt_list)
    print(prompt)


if __name__ == '__main__':
    bot = DoodleBot()
    quote_punc(bot)

