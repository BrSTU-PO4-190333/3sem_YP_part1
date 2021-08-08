def task131(lst):
    sum = 0
    for i in range(len(lst)):
        if lst[i] > 10:
            sum += lst[i]
    print(sum)
    


def task131_main():
    print(
        """
Задание 1

Пункт 3. Дан произвольный список, содержащий только числа.

Вариант 1. Выведите результат сложения всех чисел больше 10.
        """
    )
    lst = [-10, 5, 6, 15, 3, 16, 7]
    print(lst)
    task131(lst)

# task131_main()