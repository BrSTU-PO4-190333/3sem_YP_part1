#ifndef __MYMATHOPERATORS__HPP__
    #define __MYMATHOPERATORS__HPP__

    #include <iostream>

    class MyMathOperators
    {
        protected:
            double argument;
            double value;
        public:
            static MyMathOperators* head; //глобальная переменная в классе, которая указывает на голову
            static int length; //глобальная переменная в классе, которая говорит сколько элементов в списке
            MyMathOperators(); //конструктор, который управляет хвостом и голвой списка
            void printListAtHead();
            MyMathOperators* pointerLeft;
            MyMathOperators* pointerRight;
            friend bool operator==(const MyMathOperators& left, const MyMathOperators& right)
            {
                std::cout << left.value << " ";
                left.value == right.value? std::cout << "=": std::cout << "!=";
                std::cout << " " << right.value << std::endl;
                return left.value == right.value;
            }
            friend bool operator!=(const MyMathOperators& left, const MyMathOperators& right)
            {
                std::cout << left.value << " ";
                left.value != right.value? std::cout << "!=": std::cout << "=";
                std::cout << " " << right.value << std::endl;
                return left.value != right.value;
            }
            void operator=(const MyMathOperators& right);
            MyMathOperators* operator[](int index);
    };
#endif // __MYMATHOPERATORS__HPP__
