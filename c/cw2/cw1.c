#include<stdio.h>

int main(void) {
    int suma = 0;
    for (int i=1;i<=100;i++) suma += i;
    printf("suma wynosi %d\n", suma);

    suma = 0;
    licznik = 100;
    while (licznik > 0) {
        suma += licznik;
        licznik--;
    }

    return 0;
}
