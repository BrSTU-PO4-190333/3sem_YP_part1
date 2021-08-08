def task221(lst):
    for i in range(len(lst)):
        length = len(lst[i])
        if 5 < length and length < 10:
            print(lst[i])

def task221_main():
    print(
        """
Задание 2 "Строки и списки"

2. Пусть задан список, содержащий строки.

Вариант 1. Выведите построчно все строки размером от 5 до 10 символов.
        """
    )

    lst = [
        'aaa',
        'bbbbbb',
        'ccccc',
        'dddddddddd',
        'eeeeeeeee'
    ]

    task221(lst)

# task221_main()
