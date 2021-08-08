import math
import numpy

def task311(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] = math.pow(arr[i][j], 2)
 


def task311_main():
    print(
        """
Задание 3 "Матрицы"

Пусть дана матрица:

1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
2 3 4 5 6 7 8 9
9 8 7 6 5 4 3 2
1 3 5 7 9 7 5 3
3 1 5 3 2 6 5 7
1 7 5 9 7 3 1 5
2 6 3 5 1 7 3 2

Вариант №1. Определите структуру для хранения матрицы.

1. Напишите функцию возведения всех элементов матрицы в квадрат.
        """
    )

    arr = numpy.array([
        [1, 2, 3, 4, 5, 6, 7, 8],
        [8, 7, 6, 5, 4, 3, 2, 1],
        [2, 3, 4, 5, 6, 7, 8, 9],
        [9, 8, 7, 6, 5, 4, 3, 2],
        [1, 3, 5, 7, 9, 7, 5, 3],
        [3, 1, 5, 3, 2, 6, 5, 7],
        [1, 7, 5, 9, 7, 3, 1, 5],
        [2, 6, 3, 5, 1, 7, 3, 2]
    ])

    print(arr)
    print()
    task311(arr)
    print(arr)

# task311_main()