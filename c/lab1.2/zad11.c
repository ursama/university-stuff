#include<stdio.h>

int main(void) {
    int powt;
    printf("Podaj ilość powtórzeń: ");
    scanf("%d", &powt);

    for (int i=powt; i>0; i--) {
        for (int j=i; j>0; j--) {
            printf("UŚMIECH!");
        }
        printf("\n");
    }

    return 0;
}
