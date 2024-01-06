#include <iostream>

using namespace std;

int main() {
    int k, first, nr;

    cout << "Enter the ammount of numers to input: ";
    cin >> k;

    for (int i = 0; i < k; i++) {
        if (i == 0) {
            cout << "Enter the first number, that we will compare the rest to: ";
            cin >> first;
        } else {
            cout << "Enter a numer: ";
            cin >> nr;
            if (nr > first) {
                cout << "Number " << nr << " is bigger than " << first << endl; 
            }
        }
    } 

    return 0;
}