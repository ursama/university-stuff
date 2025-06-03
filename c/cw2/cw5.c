#include<stdio.h>

void print(const int t[], int n);
void wprint(const int *t, int n);

int main(void) {
    int tablica[] = {1,2,3,4,5};
    const int n = sizeof(tablica)/sizeof(tablica[0]);
    print(tablica, n);
    wprint(tablica, n);

    return 0;
}

void print(const int t[], int n) {
    for (int i=0; i<n; i++) {
        printf("t[%d]=%d ", i, t[i]);
    }
    printf("\n");
}

void wprint(const int *t, int n) {
    const int *koniec = t + n;
    for (; t<koniec; t++) {
        printf("%d ", *t);
    }
    printf("\n");
}
