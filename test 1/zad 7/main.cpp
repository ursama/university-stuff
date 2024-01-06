#include <iostream>

using namespace std;

int main() {
    const int N = 5;
    int nr_arr[N];
    int sum = 0, quan = 0;

    for (int i = 0; i < N; i++) {
        cout << "Enter the " << i + 1 << ". number: ";
        cin >> nr_arr[i];
        if (nr_arr[i] > 9 && nr_arr[i] < 100) {
            sum += nr_arr[i];
            quan++;
        }
    }

    cout << "Average of two-digit numbers: " << sum/quan;

    return 0;
}