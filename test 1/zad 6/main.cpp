#include <iostream>

using namespace std;

int main() {
    int n, nr, first, quan = 0;
    double sum = 0;
    cout << "Enter the amount of number to input: ";
    cin >> n;

    for (int i = 0; i < n; i++) {
        if (i == 0) {
            cin >> first;
        } else {
            cin >> nr;
            if (nr > first) {
                sum += nr;
                quan++;
            }
        }
    }

    cout << "Average of numbers bigger than " << first << ": " << sum/quan;

    return 0;
}