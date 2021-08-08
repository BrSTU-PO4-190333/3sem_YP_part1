#ifndef __MYSIN__HPP__
    #define __MYSIN__HPP__

    #include <iostream>
    #include <cmath>

    #include "../MyMathOperators.hpp"

    class MySin: public MyMathOperators
    {
        public:
            MySin(double argument);
            void printValue();
            void operator=(const MySin& right);
    };
#endif // __MYSIN__HPP__
