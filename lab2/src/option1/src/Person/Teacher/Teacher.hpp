#ifndef __TEACHER_HPP__
    #define __TEACHER_HPP__

    #include <iostream>
    #include <cstring>
    using namespace std;

    #include "../Person.hpp"

    class Teacher: public Person
    {
        private:
            char* subject;
        public:
            Teacher(char* name, char* surname, char* subject);
            ~Teacher();
            void show();
    };
#endif // __TEACHER_HPP__
