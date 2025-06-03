#include<stdio.h>

int max(int a, int b, int c);

int main(void) {
    int a, b, c, max_nr;
    printf("Podaj 3 liczby całkowite: ");
    scanf("%d %d %d", &a, &b, &c);

    max_nr = max(a, b, c);
    printf("\nNajwiększa liczba: %d\n", max_nr);

    return 0;
}

int max(int a, int b, int c) {
    int max_nr = a;

    if (b > max_nr) {
        max_nr = b;
    }
    if (c > max_nr) {
        max_nr = c;
    }

    return max_nr;
}
