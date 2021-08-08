#ifndef __MYCOS__HPP__
    #define __MYCOS__HPP__

    #include <iostream>
    #include <cmath>

    #include "../MyMathOperators.hpp"

    class MyCos: public MyMathOperators
    {
        public:
            MyCos(double argument);
            void printValue();
            void operator=(const MyCos& right);
    };
#endif // __MYCOS__HPP__
