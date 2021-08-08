def task211():
    my_number = 5
    print("my_number = %d" % my_number)
    
    while 1:
        user_number = int(input("user_number := "))
        if user_number < my_number:
            break

def task211_main():
    print(
        """
Задание 2 "Строки и списки"

1. Пусть задано некоторое число my_number. Пользователь вводит с клавиатуры свое число user_number.

Вариант 1. Запрашивайте у пользователя вводить число user_number до тех пор, пока оно не будет меньше my_number.
        """
    )

    task211()

# task211_main()