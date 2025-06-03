#include<stdio.h>

int main(void) {
    int a, dziel;
    printf("Podaj liczbe: ");
    scanf("%d", &a);

    printf("Podaj dzielnik: ");
    scanf("%d", &dziel);

    if ((a % dziel) == 0) {
        printf("Liczba dzieli sie przez dzielnik\n");
    } else {
        printf("Liczba NIE dzieli sie przez dzielnik\n");
    }

    return 0;
}
