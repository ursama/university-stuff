#include<stdio.h>

void dekompozycja(double x, int *cz_calkowita, double *cz_ulamkowa);

int main() {
    int cz_c;
    double cz_u, x;
    printf("Podaj liczbe rzeczywista: ");
    scanf("%lf", &x);
    dekompozycja(x, &cz_c, &cz_u);

    printf("\nCzesc calkowita: %d \nCzesc ulamkowa: %lf \n", cz_c, cz_u);

    return 0;
}

void dekompozycja(double x, int *cz_calkowita, double *cz_ulamkowa) {
    *cz_calkowita = (int) x;
    *cz_ulamkowa = x - *cz_calkowita;
}
