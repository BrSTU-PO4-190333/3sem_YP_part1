#include "lib.hpp"

// constructors

product::product()
{
    using namespace std;
    cout << this << " - product::product()" << endl;

    this->nameSize = 1;
    this->name = new char [this->nameSize];
    strcpy(this->name, "-");

    this->cipherSize = 1;
    this->cipher = new char [this->cipherSize];
    strcpy(this->cipher, "-");

    this->quantity = 0;
}

product::product(const char name[], const char cipher[], int quantity)
{
    using namespace std;

    cout << this << " - product::product(const char name[], const char cipher[], int quantity)" << endl;
    this->nameSize = strlen(name);
    this->name = new char [this->nameSize];
    strcpy(this->name, name);

    this->cipherSize = strlen(cipher);
    this->cipher = new char [this->cipherSize];
    strcpy(this->cipher, cipher);

    this->quantity = quantity;
}

product::product(const product& element)
{
    using namespace std;

    cout << this << " - product::product(const product& element)" << endl;

    this->nameSize = element.nameSize;
    this->name = new char [this->nameSize];
    strcpy(this->name, element.name);

    this->cipherSize = element.cipherSize;
    this->cipher = new char [this->cipherSize];
    strcpy(this->cipher, element.cipher);

    this->quantity = element.quantity;
}

// destructor

product::~product()
{
    using namespace std;

    cout << this << " - " << "product::~product()" << endl;

    delete [] this->name;
    delete [] this->cipher;
}

// methods

void product::print()
{
    using namespace std;

    cout << this << " - product::print()" << endl;

    cout << setw(16) << "nameSize: " << this->nameSize << endl;
    cout << setw(16) << "name: " << this->name << endl;
    cout << setw(16) << "cipherSize: " << this->cipherSize << endl;
    cout << setw(16) << "cipher: " << this->cipher << endl;
    cout << setw(16) << "quantity: " << this->quantity << endl;
    cout << endl;
}

// = = = = = sets

void product::SET(const char name[], const char cipher[], int quantity)
{
    this->nameSize = strlen(name);
    //delete [] this->name;
    this->name = new char [this->nameSize];
    strcpy(this->name, name);

    this->cipherSize = strlen(name);
    //delete [] this->cipher;
    this->cipher = new char [this->cipherSize];
    strcpy(this->cipher, cipher);

    this->quantity = quantity;
}

void product::setName(const char name[])
{
    this->nameSize = strlen(name);
    //delete [] this->name;
    this->name = new char [this->nameSize];
    strcpy(this->name, name);
}

void product::setCipher(const char cipher[])
{
    this->cipherSize = strlen(cipher);
    //delete [] this->cipher;
    this->cipher = new char [this->cipherSize];
    strcpy(this->cipher, cipher);
}

void product::setQuantity(int quantity)
{
    this->quantity = quantity;
}

// = = = = = gets

char* product::getName()
{
    return this->name;
}

char* product::getCipher()
{
    return this->cipher;
}

int product::getQuantity()
{
    return this->quantity;
}
