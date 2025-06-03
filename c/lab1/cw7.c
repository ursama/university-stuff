#include<stdio.h>

int main(void) {
    int a, b, max;
    printf("Podaj a: ");
    scanf("%d", &a);
    printf("Podaj b: ");
    scanf("%d", &b);

    max = (a > b)?a:b;
    printf("Wieksza liczba to %d\n", max);

    return 0;
}
