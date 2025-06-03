#include<stdio.h>

void print(const int tab[], int rozmiar)

int main(void) {
    int i = 0, tab[5];
    int rozmiar = sizeof(tab)/sizeof(tab[0]);
    printf("rozmiar: %d\n", rozmiar);
    while (i<rozmiar) {
        printf("Wprowadz liczbe: ");
        scanf("%d", &tab[i]);
        i++;
    }

    double srednia = 0;
    for (int i=0; i<rozmiar; i++) {
        srednia += tab[i];
    }

    srednia = srednia / rozmiar;
    printf("Srednia arytm.: %.2lf", srednia);

    print(tab, rozmiar);

    return 0;
}

void print(const int tab[], int rozmiar) {
    for (int i=0; i<rozmiar; i++) printf("tab[%d]=%d\n", i, tab[i]);
}
