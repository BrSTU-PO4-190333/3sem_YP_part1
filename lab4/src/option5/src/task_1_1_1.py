import math

def task111(a, b, c, k):
    if a == 0:
        print("a = 0. Error: div on zero")
        return -1
    elif b == 0:
        print("b = 0. Error: div on zero")
        return -1
    else:
        part1 = math.pow(a, 2) / math.pow(b, 2) + math.pow(c, 2) * math.pow(a, 2)
        part2 = a + b + c * (k - a / math.pow(b, 3))
        part3 = c + (k/b - k/a) * c
        result = part1 + part2 + part3
        if result >= 0:
            return result
        else:
            return -result

def task111_main():

    print(
        """
    Задание 1

    1. Напишите программу для решения примера (по вариантам). Предусмотрите проверку деления на ноль. Все необходимые переменные пользователь вводит через консоль. Запись |пример| означает <<взять по модулю>>, т. е. если значение получится отрицательным, необходимо сменить знак с минуса на плюс.

    Вариант 1. |a^2 / b^2} + c^2 * a^2) / (a + b + c * (k - a / b^3)) + c + ({k / b} - k / a) * c|$
        """
    )

    a = int(input("a := "))
    b = int(input("b := "))
    c = int(input("c := "))
    k = int(input("k := "))
    print(task111(a,b,c,k))

# task111_main()