def task241(string):
    res = ''
    for i in range(len(string)):
        res += str(ord(string[i]))
    return res

def task241_main():
    print(
        """
Задание 2 "Строки и списки"

4. Пусть дана строка:

Вариант 1. На основе данной строки сформируйте новую, содержащую только цифры. Выведите новую строку.
        """
    )

    print(task241('qwerty'))

# task241_main()