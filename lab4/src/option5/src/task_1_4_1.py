def task141(lst):
    max = lst[0]
    for i in range(len(lst)):
        if lst[i] > max:
            max = lst[i]
    print(max)
    
def task141_main():
    print(
        """
Задание 1

4. Дан произвольный список, содержащий только числа.

Вариант 1. Выведите максимальное число.
        """
    )
    lst = [4, 7, 2, -100, 3, 55, 33, 6]
    print(lst)
    task141(lst)

# task141_main()