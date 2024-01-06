#include <iostream>
#include <cmath>
#include <utility>

using namespace std;

int main() {
    string name;
    const int n_points = 2, n_sides = 3; 
    int A[n_points], B[n_points], C[n_points], sides[n_sides];
    bool triangle = false;

    cout << "Wprowadz swoje imie: ";
    cin >> name;
    cout << "\nMilo cie widziec, " + name << endl;

    cout << "\nWprowadz x punktu A: ";
    cin >> A[0];
    cout << "\nWprowadz y punktu A: ";
    cin >> A[1];

    cout << "\nWprowadz x punktu B: ";
    cin >> B[0];
    cout << "\nWprowadz y punktu B: ";
    cin >> B[1];

    cout << "\nWprowadz x punktu C: ";
    cin >> C[0];
    cout << "\nWprowadz y punktu C: ";
    cin >> C[1];

    sides[0] = sqrt(pow((B[0] - A[0]), 2) + pow((B[1] - A[1]), 2));
    sides[1] = sqrt(pow((C[0] - A[0]), 2) + pow((C[1] - A[1]), 2));
    sides[2] = sqrt(pow((C[0] - B[0]), 2) + pow((C[1] - B[1]), 2));

    for (int i = 0; i < n_sides - 1; i++) {
        if (sides[i] > sides[i + 1]) {
            swap(sides[i], sides[i + 1]);
        }
    } // dzieki temu wartosc najdluzszego boku znajdzie sie na koncu tablicy

    if ((sides[0] + sides[1]) > sides[2]) triangle = true;
    if (triangle) {
        int perimeter = sides[0] + sides[1] + sides[2];
        cout << "\nObwod trojkata: " << perimeter;
        // do obliczenia pola uzyje metody z wektorami
        int AB[2] = {B[0] - A[0], B[1] - A[1]}, AC[2] = {C[0] - A[0], C[1] - A[1]};
        int d_AB_AC = AB[0] * AC[1] - AC[0] * AB[1];
        double area = 0.5 * d_AB_AC;
        cout << "\nPole trojkata: " << area;
        // srodek ciezkosci
        int S[2] = {(A[0] + B[0] + C[0])/3, (A[1] + B[1] + C[1])/3};
        cout << "\nWspolrzedne srodka ciezkosci: " << S;
        // promien okregu opisanego
        cout << "\nPromien okregu opisanego na tym trojkacie: " << perimeter / 4 * area;
    } else {+
        cout << "\nNie da się utworzyć takiego trójkąta.";
    }

    return 0;
}
