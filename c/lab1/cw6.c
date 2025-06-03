#include<stdio.h>

int main(void) {
    int suma = 0;
    for (int i=1; i<=20; i++) {
        if (i%5 == 0 || i%3 == 0) {
            suma = suma + i;
        }
    }

    printf("Suma wyniosla %d\n", suma);

    return 0;
}
