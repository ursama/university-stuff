#include<stdio.h>

int main(void) {
    int x, y;
    printf("Podaj współrzędne x i y: ");
    scanf("%d %d", &x, &y);

    if (x > 0 && y > 0) {
        printf("\nPierwsza ćwiartka\n");
    } else if (x < 0 && y > 0) {
        printf("\nDruga ćwiartka\n");
    } else if (x < 0 && y < 0) {
        printf("\nTrzecia ćwiartka\n");
    } else if (x > 0 && y < 0) {
        printf("\nCzwarta ćwiartka\n");
    } else {
        printf("\nNa osi\n");
    }

    return 0;
}
