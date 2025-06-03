#include<stdio.h>

double f2a(int n, int tab[]);
int f2b(int n, int tab[]);
int f2c(int n, int tab[]);

int main(void) {
    int tablica[] = {1, 2, 3, 4, 5, 6};
    printf("Średnia arytmetyczna: %.2lf \n", f2a(6, tablica));
    printf("Suma: %d \n", f2b(6, tablica));
    printf("Suma kwadratów: %d \n", f2c(6, tablica));

    return 0;
}

double f2a(int n, int tab[]) {
    return f2b(n, tab)/n;
}

int f2b(int n, int tab[]) {
    int suma = 0;
    for (int i=0; i<n; i++) suma += tab[i];

    return suma;
}

int f2c(int n, int tab[]) {
    for (int i=0; i<n; i++) tab[i] *= tab[i];

    return f2b(n, tab);
}
