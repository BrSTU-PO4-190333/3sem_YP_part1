#include "MyTan.hpp"

MyTan::MyTan(double argument)
{
    this->argument = argument;
    this->value = tan(argument);
}

void MyTan::printValue()
{
    std::cout << "tg(" << this->argument << ") = "
        << this->value << std::endl;
}

void MyTan::operator=(const MyTan& right)
{
    this->argument = right.argument;
    this->value = tan(this->argument);
}
