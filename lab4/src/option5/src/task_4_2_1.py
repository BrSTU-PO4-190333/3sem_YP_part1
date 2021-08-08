def task421(string):
    arr = string.split('_')
    for i in range(len(arr)):
        arr[i] = arr[i].split(';')
        name = arr[i][0]
        surname = arr[i][1]
        middlename = arr[i][2]
        age = arr[i][3]
        category = arr[i][4]
        
        name_surname_middlename = name + ' ' + surname + ' ' + middlename
        
        print("%-36s\t%-16s\t%-12s" % (name_surname_middlename, category, age))

def task421_main():
    print(
        """
Задание 4 "Строки"

Пункт 2. Пусть дана строковая переменная, содержащая информацию о студентах:

my_string = 'Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса'

Вариант 1. Выведите информацию в виде:

Ф И О                    Категория          Возраст
Иванов Иван Иванович     Студент 3 курса    23 года
Петров Семен Игоревич    Студент 2 курса    22 года
        """
    )

    my_string = 'Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса'

    task421(my_string)

# task421_main()