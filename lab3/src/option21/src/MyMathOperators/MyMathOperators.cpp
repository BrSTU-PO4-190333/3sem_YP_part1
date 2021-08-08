#include "MyMathOperators.hpp"

void MyMathOperators::operator=(const MyMathOperators& right)
{
    this->argument = right.argument;
}

MyMathOperators::MyMathOperators()
{
    //при добавлении объекта в список, мы его добавляем в голову как в стеке
    this->pointerLeft = head;
    head = this;
    length += 1;
}

void MyMathOperators::printListAtHead()
{
    std::cout << std::endl << "MyMathOperators::printListAtHead()" << std::endl;
    int i = 0;
    for (MyMathOperators* temp = head; temp != NULL; temp = temp->pointerLeft, i += 1)
    {
        std::cout << "-> {" << std::endl
            << "\t" << "index: " << i << "," << std::endl
            << "\t" << "address: " << temp << "," << std::endl
            << "\t" << "argumnet: " << temp->argument << "," << std::endl
            << "\t" << "value: " << temp->value << "," << std::endl
            << "} -> pointerLeft ->" << std::endl;
    }
    std::cout << "length: " << length << std::endl;
    std::cout << std::endl;
}

MyMathOperators* MyMathOperators::operator[](int index)
{
    int i = 0;
    for (MyMathOperators* temp = head; temp != NULL; temp = temp->pointerLeft, i += 1)
    {
        if (index == i)
        {
            return temp;
        }
    }
    return NULL;
}
