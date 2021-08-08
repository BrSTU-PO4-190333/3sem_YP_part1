def task121(lst):
    for i in range(len(lst)):
        if (i + 1) % 2 == 0:
            print(lst[i])

def task121_main():
    print(
        """
Задание 1

2. Дан произвольный список, содержащий и строки и числа.

Вариант 1. Выведите все четные элементы построчно.
        """
    )
    lst = ['33', 2, 4, 5.3, 2.4, 5555.3, '443', 'ergr', 'wee', 'efe']
    print(lst)
    task121(lst)

# task121_main()