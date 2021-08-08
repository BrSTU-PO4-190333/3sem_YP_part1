import os

from task_1_1_1 import task111_main
from task_1_2_1 import task121_main
from task_1_3_1 import task131_main
from task_1_4_1 import task141_main

from task_2_1_1 import task211_main
from task_2_2_1 import task221_main
from task_2_3_1 import task231_main
from task_2_4_1 import task241_main

from task_3_1_1 import task311_main
from task_3_2_1 import task321_main
from task_3_4_1 import task341_main
from task_3_5_3 import task353_main
from task_3_6_3 import task363_main
from task_3_7_3 import task373_main
from task_3_8_1 import task381_main

from task_4_1_1 import task411_main
from task_4_2_1 import task421_main
from task_4_3_1 import task431_main
from task_4_4   import task44_main

from task_6_1   import task61_main
from task_6_2_1 import task621_main
from task_6_3_1 import task631_main
from task_6_4_1 import task641_main

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def pause():
    print('Press any key to continue...')
    string = input()

def menu():
    cls()
    print(
        """
1. Задание 1
2. Задание 2
3. Задание 3
4. Задание 4
6. Задание 6
0. Выход из из программы
        """
    )
    case = input() # запись строки
    case = case[0] # взятие первого символа со строки
    case = ord(case) # перевод символа в число

    if case == ord('0'):
        return

    elif case == ord('1'):
        sum_menu_1()
        menu()

    elif case == ord('2'):
        sum_menu_2()
        menu()

    elif case == ord('3'):
        sum_menu_3()
        menu()

    elif case == ord('4'):
        sum_menu_4()
        menu()

    elif case == ord('6'):
        sum_menu_6()
        menu()

    else:
        menu()

def sum_menu_1():
    cls()
    print(
    """
1. 111
2. 121
3. 131
4. 141
0. Выход в главное меню
    """
    )

    case = input() # запись строки
    case = case[0] # взятие первого символа со строки
    case = ord(case) # перевод символа в число

    cls()

    if case == ord('0'):
        return

    elif case == ord('1'):
        task111_main()

    elif case == ord('2'):
        task121_main()

    elif case == ord('3'):
        task131_main()

    elif case == ord('4'):
        task141_main() 

    else:
        return

    pause()

def sum_menu_2():
    cls()
    print(
    """
1. 211
2. 221
3. 231
4. 241
0. Выход в главное меню
    """
    )

    case = input() # запись строки
    case = case[0] # взятие первого символа со строки
    case = ord(case) # перевод символа в число

    cls()

    if case == ord('0'):
        return

    elif case == ord('1'):
        task211_main()

    elif case == ord('2'):
        task221_main()

    elif case == ord('3'):
        task231_main()

    elif case == ord('4'):
        task241_main()

    else:
        return

    pause()

def sum_menu_3():
    cls()
    print(
    """
1. 311
2. 321
4. 341
5. 353
6. 363
7. 373
8. 381
0. Выход в главное меню
    """
    )

    case = input() # запись строки
    case = case[0] # взятие первого символа со строки
    case = ord(case) # перевод символа в число

    cls()

    if case == ord('0'):
        return

    elif case == ord('1'):
        task311_main()

    elif case == ord('2'):
        task321_main()

    elif case == ord('4'):
        task341_main()

    elif case == ord('5'):
        task353_main()
        
    elif case == ord('6'):
        task363_main()

    elif case == ord('7'):
        task373_main()

    elif case == ord('8'):
        task381_main()

    else:
        return

    pause()

def sum_menu_4():
    cls()
    print(
    """
1. 411
2. 421
3. 431
4. 44
0. Выход в главное меню
    """
    )

    case = input() # запись строки
    case = case[0] # взятие первого символа со строки
    case = ord(case) # перевод символа в число

    cls()

    if case == ord('0'):
        return

    elif case == ord('1'):
        task411_main()

    elif case == ord('2'):
        task421_main()

    elif case == ord('3'):
        task431_main()

    elif case == ord('4'):
        task44_main()

    else:
        return

    pause()

def sum_menu_6():
    cls()
    print(
    """
1. 61
2. 62
3. 63
4. 64
0. Выход в главное меню
    """
    )

    case = input() # запись строки
    case = case[0] # взятие первого символа со строки
    case = ord(case) # перевод символа в число

    cls()

    if case == ord('0'):
        return

    elif case == ord('1'):
        task61_main()

    elif case == ord('2'):
        task621_main()

    elif case == ord('3'):
        task631_main()

    elif case == ord('4'):
        task641_main()

    else:
        return

    pause()

menu()