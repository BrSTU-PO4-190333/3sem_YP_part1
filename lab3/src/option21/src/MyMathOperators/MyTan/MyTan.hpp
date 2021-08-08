#ifndef __MYTAN__HPP__
    #define __MYTAN__HPP__

    #include <iostream>
    #include <cmath>

    #include "../MyMathOperators.hpp"

    class MyTan: public MyMathOperators
    {
        public:
            MyTan(double argument);
            void printValue();
            void operator = (const MyTan& right);
    };
#endif // __MYTAN__HPP__
