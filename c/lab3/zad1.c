#include<stdio.h>

void print(int n, int tab[]);
void f1a(int n, int tab[]);
void f1b(int n, int tab[]);
void f1c(int n, int tab[]);
void f1d(int n, int tab[]);

int main(void) {
    int tablica[] = {1, 2, 3, 4, 5};
    print(5, tablica);
    f1a(5, tablica);
    print(5, tablica);
    f1b(5, tablica);
    print(5, tablica);
    f1c(5, tablica);
    print(5, tablica);
    f1d(5, tablica);
    print(5, tablica);

    return 0;
}

void print(int n, int tab[]) {
    for (int i=0; i<n; i++) printf("%d ", tab[i]);
    printf("\n");
}

void f1a(int n, int tab[]) {
    for (int i=0; i<n; i++) tab[i] = 0;
}

void f1b(int n, int tab[]) {
    for (int i=0; i<n; i++) tab[i] = i;
}

void f1c(int n, int tab[]) {
    for (int i=0; i<n; i++) tab[i] = tab[i] * 2;
}

void f1d(int n, int tab[]) {
    for (int i=0; i<n; i++) {
        if (tab[i] < 0) {
            tab[i] = -tab[i];
        }
    }
}
