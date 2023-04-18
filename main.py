import os

bot_working = True
clear = lambda: os.system('clear')


contact_dict = {'Max':121212121,
                'John':42131221}


def input_error(func):
    def inner(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except UnboundLocalError:
            print('Enter command')
            return func(*args,**kwargs)
        except TypeError:
            print('Enter name and phone separated by a space!')
            return func(*args,**kwargs)
        except KeyError:
            print('This name found!')
            return func(*args,**kwargs)
        except IndexError:
            print('This name found! Enter another name.')
            return func(*args,**kwargs)
    return(inner)


def helper():
    clear()
    res = ''
    for key in COMMANDS.keys():
        res += f"{key}\n"
    return "Available bot function:\n" + res


def close():
    clear()
    global bot_working
    bot_working = False
    return ("Good bye!")


def hello():
    clear()
    return ('How can I help you?')


def add(name, phone):
    clear()
    contact_dict.update({name: phone})
    return f"{name} : {phone}"


def change(name, new_phone):
    clear()
    if name in contact_dict.keys():
        contact_dict[name] = new_phone
        return f"{name} : {new_phone}"
    raise IndexError


def showall():
    clear()
    res = ''
    for name, phone in contact_dict.items():
        res += f"{name} : {phone} \n"
    return res


def phone(name):
    clear()
    return f"{name} : {contact_dict[name]}"


def command_parse(s):
    com = s.lower()
    for key in  COMMANDS.keys():
        if key in com:
            command = key
    com = com.split(command)
    args = com[1].split(' ')
    args.remove('')
    if args:
        args[0] = args[0].capitalize()
    return command, args


COMMANDS = {'hello':hello,
            'add': add,
            'change':change,
            'phone':phone,
            'show all':showall,
            'good bye':close,
            'exit':close,
            'close':close,
            'help':helper,
            }


def get_handler(func):
    return COMMANDS[func]


@input_error
def main():
    while bot_working:
        s = input()
        print(get_handler(command_parse(s)[0])(*command_parse(s)[1]))



if __name__ == '__main__':
    clear()
    main()