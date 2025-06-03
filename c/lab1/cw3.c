#include<stdio.h>

int main(void) {
    int wiek;
    printf("Podaj swoj wiek: ");
    scanf("%d", &wiek);

    int dni = wiek * 365;
    printf("Masz %d dni.\n", dni);

    return 0;
}
