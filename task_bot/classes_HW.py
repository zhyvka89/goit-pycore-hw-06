from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        super().__init__(name)


class Phone(Field):
    def __init__(self, phone_number):
        super().__init__(self.validate(phone_number))
        # self.phone_number = self.validate(phone_number)

    def validate(self, phone_number):
        if len(phone_number) != 10:
            raise ValueError('Phone number should be 10 digits long.')
        return phone_number
        

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number):
        if phone_number in self.phones:
            self.phones.remove(phone_number)
        else:
            raise ValueError('Phone number does not exist.')
        
    def edit_phone(self, old_phone_number, new_phone_number):
        for index, phone_number in enumerate(self.phones):
            if phone_number.value == old_phone_number:
                self.phones[index] = Phone(new_phone_number)

    def find_phone(self, phone_number):
        for number in self.phones:
            if number.value == phone_number:
                return phone_number
        

class AddressBook(UserDict):
    def add_record(self, record):
        if record.name.value not in self.data:
            self.data[record.name.value] = record
        else:
            print('Contact name already exist.')

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise KeyError('Contact name not found.')

    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            raise KeyError("Record not found.")
