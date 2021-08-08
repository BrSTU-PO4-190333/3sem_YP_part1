def task621(lst, addedLst):
    for i in range(len(addedLst)):
        lst.pop(0)
    for i in range(len(addedLst) - 1, -1, -1):
        lst.insert(0, addedLst[i])
    return lst

def task621_main():
    print(
        """
Задание 6 "Списки"

2. Пусть дан список из 10 элементов.

Вариант 1. Удалите первые 2 элемента и добавьте 2 новых. Выведите список на экран.
        """
    )

    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(lst)
    addedLst = [111, 222]
    print(addedLst)
    lst = task621(lst, addedLst)
    print(lst)

# task621_main()