class Person:
    counter = 0
    this_object_number = 0

    name = str()
    surname = str()
    middlename = str()

    def __init__(self):
        Person.counter += 1
        self.this_object_number = Person.counter
        print('Consructor Person #%d\n' % Person.counter)

    def __init__(self, name = 'Имя', surname = 'Фамилия', middlename = 'Отчество'):
        Person.counter += 1
        self.this_object_number = Person.counter
        print('Consructor with parametrs Person #%d\n' % Person.counter)
        self.name = name
        self.surname = surname
        self.middlename = middlename

    def show(self):
        print('{')
        print('\t%10s: %s' % ('name', self.name))
        print('\t%10s: %s' % ('surname', self.surname))
        print('\t%10s: %s' % ('middlename', self.middlename))
        print('}\n')

    def set_name(self, name = 'Имя'):
        self.name = name

    def set_surname(self, surname = 'Фамилия'):
        self.surname = surname

    def set_middlename(self, middlename = 'Отчество'):
        self.middlename = middlename

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname
    
    def get_middlename(self):
        return self.middlename

    def read(self):
        self.name = str(input('Имя призывника: '))
        self.surname = str(input('Фамилия призывника: '))
        self.middlename = str(input('Отчество призывника: '))

    def __del__(self):
        print('destructor Person #%d\n' % self.this_object_number)

class Militarian(Person):
    __position = str()

    def __init__(self):
        Militarian.counter += 1
        self.this_object_number = Militarian.counter
        print('Consructor Militarian #%d\n' % Militarian.counter)

    def __init__(self, name = 'Имя', surname = 'Фамилия', middlename = 'Отчество', position = 'Рядовой'):
        Militarian.counter += 1
        self.this_object_number = Militarian.counter
        print('Consructor with parametrs Militarian #%d\n' % Militarian.counter)
        self.name = name
        self.surname = surname
        self.middlename = middlename
        self.__position = position

    def show(self):
        print('{')
        print('\t%10s: %s' % ('name', self.name))
        print('\t%10s: %s' % ('surname', self.surname))
        print('\t%10s: %s' % ('middlename', self.middlename))
        print('\t%10s: %s' % ('position', self.__position))
        print('}\n')

    def set_position(self, position = 'Рядовой\n'):
        self.__position = position

    def get_position(self):
        return self.__position

    def read(self):
        self.name = str(input('Имя призывника: '))
        self.surname = str(input('Фамилия призывника: '))
        self.middlename = str(input('Отчество призывника: '))
        self.__position = str(input('Должность: '))

    def __del__(self):
        print('destructor Militarian #%d\n' % self.this_object_number)

class Conscript(Person):
    __age = int()

    def __init__(self):
        Conscript.counter += 1
        self.this_object_number = Conscript.counter
        print('Consructor Conscript #%d\n' % Conscript.counter)

    def __init__(self, name = 'Имя', surname = 'Фамилия', middlename = 'Отчество', age = '0'):
        Conscript.counter += 1
        self.this_object_number = Conscript.counter
        print('Consructor with parametrs Conscript #%d\n' % Conscript.counter)
        self.name = name
        self.surname = surname
        self.middlename = middlename
        self.__age = age

    def show(self):
        print('{')
        print('\t%10s: %s' % ('name', self.name))
        print('\t%10s: %s' % ('surname', self.surname))
        print('\t%10s: %s' % ('middlename', self.middlename))
        print('\t%10s: %s' % ('age', self.__age))
        print('}\n')

    def set_age(self, age = 0):
        self.__age = age

    def get_age(self):
        return self.__age

    def read(self):
        self.name = str(input('Имя призывника: '))
        self.surname = str(input('Фамилия призывника: '))
        self.middlename = str(input('Отчество призывника: '))
        self.__age = int(input('Возвраст: '))

    def __del__(self):
        print('destructor Conscript #%d\n' % self.this_object_number)

if __name__ == '__main__':
    person = Person()
    person.show()
    person.read()
    person.show()

    militarian = Militarian()
    militarian.show()
    militarian.read()
    militarian.show()

    conscript = Conscript()
    conscript.show()
    conscript.read()
    conscript.show()

    person1 = Person()
    person1.set_name('Aaa')
    person1.set_surname('Bbb')
    person1.set_middlename('Ccc')
    print(person1.get_name())
    print(person1.get_surname())
    print(person1.get_middlename())
    
    militarian1 = Militarian()
    militarian1.set_name('Ddd')
    militarian1.set_surname('Eee')
    militarian1.set_middlename('Fff')
    militarian1.set_position('Ggg')
    print(militarian1.get_name())
    print(militarian1.get_surname())
    print(militarian1.get_middlename())
    print(militarian1.get_position())

    conscript1 = Conscript()
    conscript1.set_name('Hhh')
    conscript1.set_surname('Iii')
    conscript1.set_middlename('Jjj')
    conscript1.set_age(17)
    print(conscript1.get_name())
    print(conscript1.get_surname())
    print(conscript1.get_middlename())
    print(conscript1.get_age())
