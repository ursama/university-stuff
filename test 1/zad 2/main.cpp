#include <iostream>

using namespace std;

int main() {
    // user inputs 10 numbers outside the given interval, outputs the biggest nr
    const int x = 3, y = 10;
    int nr, max, i = 0;

    do {
        cout << "Input a number outside an interval <"<<x<<", "<<y<<">: ";
        cin >> nr;
        
        if (i == 0 && (x > nr || nr > y)) {
            max = nr;
            i++;
        } else if (x > nr || nr > y) {
            if (nr > max) {
                max = nr;
            }
            i++;
        } else {
            cout << "Number within the interval. Try again." << endl;
        }  
    } while (i < 10);

    cout << "The biggest entered number is " << max;

    return 0;
}