class Polyclinic:
    __count = 0
    __this_object_number = int()

    __phone = str()
    __address = str()
    __number = int()

    def __init__(self):
        Polyclinic.__count += 1
        print('Constructor without parametrs #%d' % Polyclinic.__count)
        self.__this_object_number = Polyclinic.__count

    def __init__(self, phone = '+370-162-00-00-00', address = 'Brest', number = 6):
        Polyclinic.__count += 1
        print('Constructor with parametrs #%d' % Polyclinic.__count)
        self.__this_object_number = Polyclinic.__count
        
        try:
            self.__phone = phone
            self.__address = address
            self.__number = int(number)
        except ValueError as e:
            print('Error in constructor #%d: __init__(self, phone, address, number)' % self.__this_object_number)
            print(e)

    def show(self):
        print('object = {')
        print('\t%8s: %s,' % ('phone', self.__phone))
        print('\t%8s: %s,' % ('adress', self.__address))
        print('\t%8s: %d' % ('number', self.__number))
        print('}')

    def set_phone(self, phone = '+375-162-00-00-00'):
        self.__phone = phone

    def set_address(self, address = '...'):
        self.__address = address

    def set_number(self, number = 0):
        self.__number = number

    def get_phone(self):
        return self.__phone

    def get_address(self):
        return self.__address

    def get_number(self):
        return self.__number

    def __del__(self):
        print('destructor #%d' % self.__this_object_number)
        Polyclinic.__count -= 1

if __name__ == '__main__':
    a = Polyclinic()
    b = Polyclinic()
    c = Polyclinic()
    d = Polyclinic()
    e = Polyclinic()
    f = Polyclinic()
    g = Polyclinic()
    h = Polyclinic()
    i = Polyclinic()

    print('\nCall destructors:')
    del d
    del e
    del f
    print()

    # Пробует гетеры и сеторы
    j = Polyclinic()
    j.show()

    j.set_phone('123')
    print(j.get_phone())

    j.set_address('qqqqqq')
    print(j.get_address())

    j.set_number(555)
    print(j.get_number())

    j.show()
    print()

    # Пробуем конструктор с параметрами
    h = Polyclinic('34g4', '43gh54', 444)
    h.show()
