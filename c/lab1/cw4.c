#include<stdio.h>

int main(void) {
    int i;
    printf("Podaj dowolna liczbe: ");
    scanf("%d", &i);

    /* switch (i) {
        case (i >= 0): printf("Wartosc bezwzgledna to %d\n", i); break;
	case (i < 0): printf("Wartosc bezwzgledna to %d\n", -i); break;
    } */

    if (i >= 0) {
        printf("Wartosc bezwzgledna to %d\n", i);
    } else {
	printf("Wartosc bezwzgledna to %d\n", -i);
    }

    return 0;
}
