import random

def task231():
    result = ''
    for i in range(5):
        number = random.randint(65, 90)
        symbol = chr(number)
        result += symbol
    return result

def task231_main():
    print(
        """
Задание 2 "Строки и списки"

3. Сгенерируйте и выведите:

Вариант 1. Случайную строку, состоящую из 5 символов, содержащую только заглавные буквы русского алфавита.
        """
    )

    print(task231())

# task231_main()