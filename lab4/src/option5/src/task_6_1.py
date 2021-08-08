def task61(arr):
    lst = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            lst.append(arr[i][j])
    sum = 0
    for i in range(len(lst)):
        sum += lst[i]
    return sum

def task61_main():
    print(
        """
Задание 6 "Списки"

1. Пусть дана матрица чисел размером NxN, Представьте данную матрицу в виде списка. Выведите результат сложения всех элементов матрицы.
        """
    )

    arr = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    print(task61(arr))

# task61_main()