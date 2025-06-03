#include<stdio.h>

int main(void) {
    int wybor = 0;
    printf("Podaj liczbe od 1 do 3: ");
    scanf("%d", &wybor);

    switch (wybor) {
        case 1: printf("Podales 1\n"); break;
	case 2: printf("Podales 2\n"); break;
	case 3: printf("Podales 3\n"); break;

	default: printf("debil\n");
    }
    return 0;
}
