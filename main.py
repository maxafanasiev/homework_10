import os
from collections import UserDict
import oop


ADRESS_BOOK = oop.AddressBook()
bot_working = True
clear = lambda: os.system('clear')

# #for test
# rec1 = oop.Record(oop.Name('Max'), oop.Phone('12'))
# rec2 = oop.Record(oop.Name('Matt'), oop.Phone('13'))
# rec3 = oop.Record(oop.Name('Ann'), oop.Phone('14'))
# rec1.add_phone('324324234')
# ADRESS_BOOK.addRecord(rec1)
# ADRESS_BOOK.addRecord(rec2)
# ADRESS_BOOK.addRecord(rec3)


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
            print('This name not found!')
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


@input_error
def add_record(name, phone):
    clear()
    if not name in  ADRESS_BOOK.keys():
        rec = oop.Record(oop.Name(name),oop.Phone(phone))
        ADRESS_BOOK.addRecord(rec)
        return f"{rec.name.value} : {[ phone.value for phone in rec.phones]}\n"
    else: 
        return "Name already exist. Try add phone command for add extra phone."


def change_phone(name, old_phone, new_phone):
    clear()
    rec = ADRESS_BOOK.getRecord_byName(name)
    rec.change_phone(oop.Phone(old_phone),oop.Phone(new_phone))
    return f"{rec.name.value} : {[ phone.value for phone in rec.phones]}\n"


def add_phone(name, phone):
    clear()
    rec = ADRESS_BOOK.getRecord_byName(name)
    rec.add_phone(oop.Phone(phone))
    return f"{rec.name.value} : {[ phone.value for phone in rec.phones]}"

def delete_phone(name, phone):
    clear()
    rec = ADRESS_BOOK.getRecord_byName(name)
    rec.del_phone(oop.Phone(phone))
    return f"{rec.name.value} : {[ phone.value for phone in rec.phones]}\n"


def showall():
    clear()
    res = ''
    source = ADRESS_BOOK
    for key, record in source.items():
        res += f"{key} : {[ phone.value for phone in record.phones]}\n"
    if res:
        return res
    else:
        return "Address book is empty."



def phone(name):
    clear()
    rec = ADRESS_BOOK.getRecord_byName(name)
    return f"{rec.name.value} : {[ phone.value for phone in rec.phones]}"


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
            'add': add_record,
            'change':change_phone,
            'phone':phone,
            'show all':showall,
            'good bye':close,
            'exit':close,
            'close':close,
            'help':helper,
            'add phone': add_phone,
            'delete phone': delete_phone
            }


@input_error
def get_handler(func):
    return COMMANDS[func]


@input_error
def main():
    while bot_working:
        s = input()
        command = get_handler(command_parse(s)[0])
        arguments = command_parse(s)[1]
        print(command(*arguments))



if __name__ == '__main__':
    clear()
    main()