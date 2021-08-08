#ifndef __STUDENT_HPP__
    #define __STUDENT_HPP__

    #include <iostream>
    #include <cstring>
    using namespace std;

    #include "../Person.hpp"

    class Student: public Person
    {
        private:
            char* group;
        public:
            Student(char* name, char* surname, char* group);
            ~Student();
            void show();
    };
#endif // __STUDENT_HPP__
