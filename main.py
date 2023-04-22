import os
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
    if name not in ADRESS_BOOK.keys():
        rec = oop.Record(oop.Name(name),oop.Phone(phone))
        ADRESS_BOOK.addRecord(rec)
        return f"{rec.name.value} : {[ phone.value for phone in rec.phones]}\n"
    return "Name already exist. Try add phone command for add extra phone."


def change_phone(name, old_phone, new_phone):
    clear()
    rec = ADRESS_BOOK.getRecord_byName(name)
    if new_phone != old_phone and old_phone in [phone.value for phone in rec.phones] and new_phone not in [phone.value for phone in rec.phones]:
        rec.change_phone(oop.Phone(old_phone),oop.Phone(new_phone))
        return f"{rec.name.value} : {[ phone.value for phone in rec.phones]}\n"
    return "This phone not found, or phone already exist."


def add_phone(name, phone):
    clear()
    rec = ADRESS_BOOK.getRecord_byName(name)
    if phone not in [ phone.value for phone in rec.phones]:
        rec.add_phone(oop.Phone(phone))
        return f"{rec.name.value} : {[ phone.value for phone in rec.phones]}"
    return "This phone already added."

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


def unknown_command():
    return "Unknown command, try again"


def command_parse(s):
    for key, cmd in  COMMANDS.items():
        if key in s.lower():
            return cmd, s[len(key):].strip().split()
    return unknown_command, []


COMMANDS = {'hello':hello,
            'add phone': add_phone,
            'change':change_phone,
            'find phone':phone,
            'show all':showall,
            'good bye':close,
            'exit':close,
            'close':close,
            'delete phone': delete_phone,
            'add': add_record,
            'help':helper,
            }


@input_error
def main():
    while bot_working:
        s = input()
        command, arguments = command_parse(s)
        print(command(*arguments))



if __name__ == '__main__':
    clear()
    main()