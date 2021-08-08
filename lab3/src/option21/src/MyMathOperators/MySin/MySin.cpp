#include "MySin.hpp"

MySin::MySin(double argument)
{
    this->argument = argument;
    this->value = sin(argument);
}

void MySin::printValue()
{
    std::cout << "sin(" << this->argument << ") = "
        << this->value << std::endl;
}

void MySin::operator=(const MySin& right)
{
    this->argument = right.argument;
    this->value = sin(this->argument);
}
