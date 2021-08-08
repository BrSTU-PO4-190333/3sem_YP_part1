#ifndef _LIB_H_
    #define _LIB_H_

    #include <iostream>
    #include <iomanip>
    #include <cstring>

    //Task 1.1
    class product
    {
    private:
        int nameSize;
        char* name;

        int cipherSize;
        char* cipher;

        int quantity;

    public:
        //Task 1.2
        // = = = = = constructor
        product();
        product(const char name[], const char cipher[], int quantity);
        product(const product& element);
        //Task 1.3
        // = = = = = destructor
        ~product();

        // = = = = = methods
        void print();

        //Task 1.4
        // = = = = = set
        void SET(const char name[], const char cipher[], int quantity);
        void setName(const char name[]);
        void setCipher(const char cipher[]);
        void setQuantity(int quantity);
        // = = = = = get
        char* getName();
        char* getCipher();
        int getQuantity();
    };
#endif // _LIB_H_
