from collections import UserDict


class AddressBook(UserDict):
    def __init__(self):
        self.data = {}

    def __setitem__(self, key, item):
        self.data[key] = item


    def addRecord(self,record):
        self.data[record.name.value] = record

    def getRecord_byName(self,name):
        return self.data[name]


class Field:
    pass
    

class Name(Field):
    def __init__(self, name) -> None:
        self.value = name



class Phone(Field):
    def __init__(self, phone) -> None:
        self.value = phone


class Record:
    def __init__(self,name, phone=None):
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)


    def add_phone(self, phone: Phone):
        self.phones.append(Phone(phone))


    def del_phone(self, phone: Phone):
        for n in self.phones:
            if n.value == phone:
                self.phones.remove(n)


    def change_phone(self,old_phone, new_phone: Phone):
        self.del_phone(old_phone)
        self.add_phone(new_phone)
