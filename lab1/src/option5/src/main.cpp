#include "main.hpp"

//Task 1.7
int main()
{
    using namespace std;

    //Task 2.3.a product a("-", "-", 0), b = a;
    //Copy constructor with parametrs
    cout << endl << "Task 2.3.a" << endl
        << "a(\"-\", \"-\", 0), b = a" << endl;
    product task23a_a("Gang Earthed Socket", "920100", 24), task23a_b = task23a_a;

    //Task 2.3.b
    //Copy constructor. Call on function View()
    cout << endl << "Task 2.3.b" << endl
        << "Copy constructor. Call on function View()" << endl;
    View(task23a_a);

    //Task 2.3.c product c = NoName(a);
    //Copy constructor. Return function and initialization.
    cout << endl << "Task 2.3.c" << endl
        << "Copy constructor. Return function and initialization." << endl;
    product task23a_c = NoName(task23a_a);

    //Task 2.4.a
    //Static array
    cout << endl << "Task 2.4.a" << endl
        << "Static memory" << endl;
    product task24a_arr[3];
    task24a_arr[0].SET("Flat Famale Plug", "11110", 1000);
    for (int i = 0; i < 3; i++)
    {
        cout << i << endl;
        task24a_arr[i].print();
    }
    //and so far
    //or
    product task24a_array[3] = {
        product("2 Gang Earthed Socket", "920100", 24),
        product("2 Gand Earthed Socket with 2m Cord", "920102", 12),
        product("2 Gand Earthed Socket with 3m Cord", "920103", 12),
    };
    for (int i = 0; i < 3; i++)
    {
        cout << i << endl;
        task24a_array[i].print();
    }

    //Task 2.4.b
    //Dynamic memory
    cout << endl << "Task 2.4.b" << endl
        << "Dynamic memory" << endl;
    product* task24b_p;
    task24b_p = new product [3];
    task24b_p->SET("Ceiling Globe Luminaire (Lale)", "95005", 40);
    task24b_p[1].SET("Ceiling Globe Luminaire (Yol)", "95006", 40);
    task24b_p[2].SET("Ceiling Globe Luminaire (Ruba)", "95007", 40);
    for (int i = 0; i < 3; i++)
    {
        cout << i << endl;
        task24b_p[i].print();
    }

    //Task 2.5 and Task 1.8
    //Pointer to component function
    cout << endl << "Task 2.5" << endl
        << "Pointer to component function" << endl;
    void (product::*task25_pf)();
    task25_pf = &product::print;
    (task24b_p[1].*task25_pf)();

    //Task 1.8
    //Pointer to object
    cout << endl << "Task 1.8" << endl
        << "Pointer to object" << endl;
    product *objectPointer = &task23a_a;
    cout << "objectPointer->print()" << endl;
    objectPointer->print();

    //Task 1.4

    //GETs methodts: c.getSmth();
    cout << endl << "Task 1.4" << endl
        << "GETs" << endl;
    cout << setw(16) << "task23a_a.getName(); - " << task23a_a.getName() << endl;
    cout << setw(16) << "task23a_a.getCipher(); - " << task23a_a.getCipher() << endl;
    cout << setw(16) << "task23a_a.getQuantity(); - " << task23a_a.getQuantity() << endl;

    //Sets
    cout << "SETs" << endl;
    task23a_a.print();
    task23a_a.setName("Male Plug");
    task23a_a.setCipher("11104");
    task23a_a.setQuantity(500);
    task23a_a.print();

    //Destructor for dynamic memory
    delete [] task24b_p;

    return 0;
}

void View(product a)
{
    a.print();
}

product NoName(product& a)
{
    product temp(a);
    temp.SET("British Goliath", "11118", 180);
    return temp;
}
