#include "main.hpp"

MyMathOperators* MyMathOperators::head = NULL; //глобальная переменная в классе, которая указывает на голову
int MyMathOperators::length = 0; //глобальная переменная в классе, которая говорит сколько элементов в списке

int main()
{
    MyTan obj1(111.111);
    MyTan obj2(222.222);

    printLine();
    std::cout << "obj1.printValue();" << std::endl;
    obj1.printValue();

    printLine();
    std::cout << "obj2.printValue();" << std::endl;
    obj2.printValue();

    printLine();
    std::cout << "Test operator==" << std::endl;
    std::cout << "obj1 == obj2 ?" << std::endl;
    std::cout << (obj1 == obj2) << std::endl;

    printLine();
    std::cout << "Test operator!=" << std::endl;
    std::cout << "obj1 != obj2 ?" << std::endl;
    std::cout << (obj1 != obj2) << std::endl;

    printLine();
    std::cout << "Test operator=" << std::endl;
    std::cout << "MyTan obj3 = obj1;" << std::endl;
    MyTan obj3 = obj1;

    printLine();
    std::cout << "obj3.printValue();" << std::endl;
    obj3.printValue();

    printLine();
    std::cout << "Test my OOP list" << std::endl;
    obj3.printListAtHead();
    MyTan obj4(4);
    MyTan obj5(5);
    MyTan obj6(6);
    MyCos obj7(7.7);
    MyCos obj8(8.8);
    MyCos obj9(9.9);
    MySin obj10(10);
    MySin obj11(11);
    MySin obj12(12);
    obj6.printListAtHead();

    printLine();
    std::cout << "Test operator[]" << std::endl;

    std::cout << obj6[0] << std::endl;
    for (int i = 0; i < 15; i++)
    {
        std::cout << i << "\t" << obj6[i] << std::endl;
    }

    return 0;
}

void printLine()
{
    std::cout << std::endl;
    for (int i = 0; i < 16; i++)
    {
        std::cout << " = ";
    }
    std::cout << std::endl << std::endl;
}
