#include "MyCos.hpp"

MyCos::MyCos(double argument)
{
    this->argument = argument;
    this->value = cos(argument);
}

void MyCos::printValue()
{
    std::cout << "cos(" << this->argument << ") = "
        << this->value << std::endl;
}

void MyCos::operator=(const MyCos& right)
{
    this->argument = right.argument;
    this->value = cos(this->argument);
}
