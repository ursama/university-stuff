#include <iostream>

using namespace std;

int main() {
    const int N = 5, D = 2; 
    int array[N];

    cout << "Enter " << N << " integers:" << endl;
    for (int i = 0; i < N; ++i) {
        cout << "Enter " << i + 1 << ". number: ";
        cin >> array[i];
    }

    cout << "Entered array: ";
    for (int i = 0; i < N; i++) {
        cout << array[i] << " ";
    }
    cout << endl;

    int sum = 0;  // Sum of numbers divisible by D
    int quan = 0;  // Amount of numbers divisible by D

    for (int i = 0; i < N; i++) {
        if (array[i] % D == 0) {
            sum += array[i];
            quan++;
        }
    }

    cout << "Average of numbers divisible by " << D << ": " << sum/quan << endl;

    return 0;
}
