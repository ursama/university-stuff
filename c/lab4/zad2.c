#include<stdio.h>

int f2(int *a, int *b);

int main(void) {
    int x=2, y=5;
    int *a=&x, *b=&y;

    printf("Większa liczba to: %d \n", f2(a, b));

    return 0;
}

int f2(int *a, int *b) {
   return ((*a > *b)?*a:*b);
}
