#include<stdio.h>

int main(void) {
    int a, b, c, max;
    printf("Podaj a, b, c: ");
    scanf("%d %d %d", &a, &b, &c);

    if (a > b) {
        max = (a > c)?a:c;
    } else {
	max = (b > c)?b:c;
    }

    printf("Najwieksza liczba to %d", max);

    return 0;
}
