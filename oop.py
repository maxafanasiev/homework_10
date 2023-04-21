from collections import UserDict


class AddressBook(UserDict):
    def addRecord(self,record):
        self.data[record.name.value] = record

    def getRecord_byName(self,name):
        return self.data[name]


class Field:
    def __init__(self, value):
        self.value = value
    

class Name(Field):
    pass
        



class Phone(Field):
    pass


class Record:
    def __init__(self,name, phone=None):
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)


    def add_phone(self, phone: Phone):
        self.phones.append(phone)


    def del_phone(self, phone: Phone):
        for n in self.phones:
            if n.value == phone.value:
                self.phones.remove(n)


    def change_phone(self,old_phone: Phone, new_phone: Phone):
        self.del_phone(old_phone)
        self.add_phone(new_phone)
