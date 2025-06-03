#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int generuj();

int main() {
    srand(time(0));

    int n;
    printf("Podaj n: ");
    scanf("%d", &n);

    int *tab = calloc(n, sizeof(int));

    if (tab != NULL) {
        for (int x=0; x<n; x++) {
            *(tab + x) = generuj();
            printf("%d \n", *(tab + x));
        }
        free(tab);
    } else {
        printf("Alokacja nie powiodła sie \n");
        return 1;
    }
}

int generuj() {
    return (rand() % (99 + 1 - (-99)) + (-99));
}
