#include <iostream>

using namespace std;

int main() {
    int nr;

    do {
        cout << "Enter an integer, even, two-digit and positive number: ";
        cin >> nr;
    } while (nr % 2 != 0 || nr < 10 || nr > 99);

    return 0;
}