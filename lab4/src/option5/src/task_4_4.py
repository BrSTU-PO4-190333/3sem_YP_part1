def task44(string):
    counter = 0
    for i in string:
        counter += 1
    print('number symbols: %d' % counter)
    
    words = string.split()
    print("number words: %d" % len(words))

def task44_main():
    print(
        """
Задание 4 "Строки"

4. Пусть дана строка произвольной длины. Выведите информацию о том, сколько в ней символов и сколько слов.
        """
    )

    string = 'Далеко-далеко за словесными горами в стране гласных и согласных живут рыбные тексты.'

    print(string)
    print()
    task44(string)

# task44_main()