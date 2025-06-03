#include<stdio.h>

int main(void) {
    int wiek;
    printf("Podaj swój wiek w latach: ");
    scanf("%d", &wiek);

    int wiek_dni = wiek * 365;
    printf("\nTwój wiek w dniach: %d", wiek_dni);

    return 0;
}
